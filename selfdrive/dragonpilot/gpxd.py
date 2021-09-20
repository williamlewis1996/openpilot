#!/usr/bin/env python3

import cereal.messaging as messaging
import os
import time
import datetime
import signal
import threading
from common.realtime import Ratekeeper
from common.params import Params

# for uploader
from selfdrive.loggerd.xattr_cache import getxattr, setxattr
import glob
import requests

# customisable values
GPX_LOG_PATH = '/data/media/0/gpx_logs/'
LOG_HERTZ = 10 # 10 hz = 0.1 sec, higher for higher accuracy, 10hz seems fine
LOG_LENGTH = 10 # mins, higher means it keeps more data in the memory, will take more time to write into a file too.
LOST_SIGNAL_COUNT_LENGTH = 30 # secs, output log file if we lost signal for this long

# do not change
LOST_SIGNAL_COUNT_MAX = LOST_SIGNAL_COUNT_LENGTH * LOG_HERTZ # secs,
LOGS_PER_FILE = LOG_LENGTH * 60 * LOG_HERTZ # e.g. 3 * 60 * 10 = 1800 points per file

# uploader
UPLOAD_ATTR_NAME = 'user.upload'
UPLOAD_ATTR_VALUE = b'1'
LOG_PATH = '/data/media/0/gpx_logs/'

# osm api
API_HEADER = {'Authorization': 'Bearer 2pvUyXfk9vizuh7PwQFSEYBtFWcM-Pu7vxApUjSA0fc'}
VERSION_URL = 'https://api.openstreetmap.org/api/versions'
UPLOAD_URL = 'https://api.openstreetmap.org/api/0.6/gpx/create'

class WaitTimeHelper:
  ready_event = threading.Event()
  shutdown = False

  def __init__(self):
    signal.signal(signal.SIGTERM, self.graceful_shutdown)
    signal.signal(signal.SIGINT, self.graceful_shutdown)
    signal.signal(signal.SIGHUP, self.graceful_shutdown)

  def graceful_shutdown(self, signum, frame):
    self.shutdown = True
    self.ready_event.set()

class GpxD():
  def __init__(self, delete_after_upload = False):
    self.log_count = 0
    self.logs = list()
    self.lost_signal_count = 0
    self.wait_helper = WaitTimeHelper()
    self.started_time = datetime.datetime.utcnow().isoformat()
    self._uploader_thread = None
    self._delete_after_upload = delete_after_upload

  def log(self, sm):
    gps = sm['gpsLocationExternal']

    # do not log when no fix or accuracy is too low, add lost_signal_count
    if gps.flags % 2 == 0 or gps.accuracy > 5.:
      if self.log_count > 0:
        self.lost_signal_count += 1
    else:
      self.logs.append([datetime.datetime.utcfromtimestamp(gps.timestamp*0.001).isoformat(), str(gps.latitude), str(gps.longitude), str(gps.altitude)])
      self.log_count += 1
      self.lost_signal_count = 0

  def write_log(self, force = False):
    if self.log_count == 0:
      return

    if force or (self.log_count >= LOGS_PER_FILE or self.lost_signal_count >= LOST_SIGNAL_COUNT_MAX):
      self._write_gpx()
      self.lost_signal_count = 0
      self.log_count = 0
      self.logs.clear()
      self.started_time = datetime.datetime.utcnow().isoformat()

  def _write_gpx(self):
    if len(self.logs) > 0:
      if not os.path.exists(GPX_LOG_PATH):
        os.makedirs(GPX_LOG_PATH)
      filename = self.started_time.replace(':','-')
      str = ''
      str += "<?xml version=\"1.0\" encoding=\"utf-8\" standalone=\"yes\"?>\n"
      str += "<gpx version=\"1.1\" creator=\"dragonpilot https://github.com/dragonpilot-community/dragonpilot\" xmlns=\"http://www.topografix.com/GPX/1/1\" xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\" xsi:schemaLocation=\"http://www.topografix.com/GPX/1/1 http://www.topografix.com/GPX/1/1/gpx.xsd\">\n"
      str += "<trk>\n"
      str += "  <name>" + self.started_time + "</name>"
      str += "  <trkseg>\n"
      for trkpt in self.logs:
        str += self._trkpt_template(trkpt[1], trkpt[2], trkpt[3], trkpt[0])
      str += "  </trkseg>\n"
      str += "</trk>\n"
      str += "</gpx>\n"
      try:
        f = open('%s%sZ.gpx' % (GPX_LOG_PATH, filename), 'w')
        f.write(str)
        f.close()
      except:
        pass

  def _trkpt_template(self, lat, lon, ele, time):
    str = ""
    str += "    <trkpt lat=\"" + lat + "\" lon=\"" + lon + "\">\n"
    str += "      <ele>" + ele + "</ele>\n"
    str += "      <time>" + time + "</time>\n"
    str += "    </trkpt>\n"
    return str

  def upload_log(self):

    def is_online():
      try:
        r = requests.get(VERSION_URL, headers=API_HEADER)
        return r.status_code >= 200
      except:
        return False

    def get_is_uploaded(filename):
      return getxattr(filename, UPLOAD_ATTR_NAME) is not None

    def set_is_uploaded(filename):
      setxattr(filename, UPLOAD_ATTR_NAME, UPLOAD_ATTR_VALUE)

    def get_files():
      return sorted( filter( os.path.isfile, glob.glob(LOG_PATH + '*') ) )

    def get_files_to_be_uploaded():
      files = get_files()
      files_to_be_uploaded = []
      for file in files:
        if not get_is_uploaded(file):
          files_to_be_uploaded.append(file)
      return files_to_be_uploaded

    def do_upload(filename):
      fn = os.path.basename(filename)
      data = {
        'description': 'Routes from dragonpilot.',
        'visibility': 'identifiable'
      }
      files = {
        "file": (fn, open(filename, 'rb'))
      }
      try:
        r = requests.post(UPLOAD_URL, files=files, data=data, headers=API_HEADER)
        return r.status_code == 200
      except:
        return False

    def uploader_main(delete_after_upload):
      files = get_files_to_be_uploaded()
      if not is_online() or len(files) == 0:
        time.sleep(30)
        return

      for file in files:
        successful = do_upload(file)
        if successful:
          if delete_after_upload:
            os.remove(file)
          else:
            set_is_uploaded(file)
      time.sleep(30)
      return

    if self._uploader_thread is not None and self._uploader_thread.is_alive():
      return

    self._uploader_thread = threading.Thread(target=uploader_main, args=(self._delete_after_upload, ))
    self._uploader_thread.start()


def gpxd_thread(sm=None, pm=None):
  if sm is None:
    sm = messaging.SubMaster(['gpsLocationExternal'])

  wait_helper = WaitTimeHelper()
  gpxd = GpxD(not Params().get_bool('dp_gpxd'))
  rk = Ratekeeper(LOG_HERTZ, print_delay_threshold=None)

  while True:
    sm.update(0)
    gpxd.log(sm)
    gpxd.write_log()
    gpxd.upload_log()
    if wait_helper.shutdown:
      gpxd.write_log(True)
      gpxd.upload_log()
      break
    rk.keep_time()

def main(sm=None, pm=None):
  gpxd_thread(sm, pm)

if __name__ == "__main__":
  main()
