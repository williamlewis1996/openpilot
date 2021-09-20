#!/usr/bin/bash

if [ $1 -eq 1 ]; then
  printf %s "1" > /data/params/d/CommunityFeaturesToggle
  printf %s "1" > /data/params/d/dp_atl
  printf %s "0" > /data/params/d/dp_uploader
  printf %s "0" > /data/params/d/dp_logger
  printf %s "0" > /data/params/d/dp_athenad
fi
if [ $2 -eq 1 ]; then
  printf %s "1" > /data/params/d/dp_atl_op_long
fi

if [ $1 -eq 0 ]; then
  printf %s "0" > /data/params/d/dp_atl
  printf %s "0" > /data/params/d/dp_atl_op_long
  rm -fr /data/openpilot/panda/board/obj/panda.bin
  rm -fr /data/openpilot/panda/board/obj/panda.bin.signed
  cd /data/openpilot || exit
  git reset --hard @{u}
  git clean -xdf
fi

