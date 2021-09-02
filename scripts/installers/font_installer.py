#!/usr/bin/env python3
import os

if __name__ == "__main__":
  install_font = False

  if os.path.isfile("/EON"):
    if os.path.islink('/system/fonts/NotoSansTC-Regular.otf'):
      install_font = True
    if not os.path.isfile("/system/fonts/NotoSansTC-Regular.otf"):
      install_font = True
    if install_font:
      os.system("mount -o remount,rw /system")
      os.system("find /system/fonts/NotoSans*.otf -type l -delete")
      os.system("cp -frv /usr/share/fonts/NotoSans* /system/fonts/")
      os.system("cp -fr /data/openpilot/selfdrive/dragonpilot/fonts.xml /system/etc/fonts.xml")
      os.system("chmod 644 /system/etc/fonts.xml")
      os.system("chmod 644 /system/fonts/NotoSans*")
      os.system("mount -o remount,r /system")

  elif os.path.isfile("/TICI"):
    pass
  else:
    pass