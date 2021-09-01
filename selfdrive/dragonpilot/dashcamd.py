#!/usr/bin/env python3.7
import os
import datetime
from common.realtime import sec_since_boot

DASHCAM_VIDEOS_PATH = '/sdcard/dashcam/'
DASHCAM_DURATION = 180 # max is 180
DASHCAM_BIT_RATES = 4000000 # max is 4000000
DASHCAM_MAX_SIZE_PER_FILE = DASHCAM_BIT_RATES/8*DASHCAM_DURATION # 4Mbps / 8 * 180 = 90MB per 180 seconds
DASHCAM_KEPT = DASHCAM_MAX_SIZE_PER_FILE * 240 # 12 hrs of video = 21GB

class Dashcamd():
  def __init__(self):
    self.dashcam_folder_exists = False
    self.dashcam_mkdir_retry = 0
    self.dashcam_next_time = 0
    self.started = False

  def run(self, started):
    if self.started and not started:
      self.stop()
    self.started = started
    self.make_folder()
    if self.dashcam_folder_exists:
      self.start()

  def stop(self):
    os.system("killall -SIGINT screenrecord")
    self.dashcam_next_time = 0

  def make_folder(self):
    if not self.dashcam_folder_exists and self.dashcam_mkdir_retry <= 5:
      # create dashcam folder if not exist
      try:
        if not os.path.exists(DASHCAM_VIDEOS_PATH):
          os.makedirs(DASHCAM_VIDEOS_PATH)
        else:
          self.dashcam_folder_exists = True
      except OSError:
        self.dashcam_folder_exists = False
        self.dashcam_mkdir_retry += 1

  def start(self):
    # start recording
    if self.started:
      ts = sec_since_boot()
      if ts >= self.dashcam_next_time:
        now = datetime.datetime.now()
        file_name = now.strftime("%Y-%m-%d_%H-%M-%S")
        os.system("LD_LIBRARY_PATH= screenrecord --bit-rate %s --time-limit %s %s%s.mp4 &" % (DASHCAM_BIT_RATES, DASHCAM_DURATION, DASHCAM_VIDEOS_PATH, file_name))
        self.dashcam_next_time = ts + DASHCAM_DURATION - 1
    else:
      self.dashcam_next_time = 0