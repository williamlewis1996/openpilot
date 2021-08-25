Installation may or may not compile if installed directly via the URL on the device.   
  
SSH Install on the Comma Three:  
`cd /data; cp -rf ./openpilot ./openpilot.bak; rm -rf ./openpilot; git clone https://github.com/Aragon7777/openpilot.git openpilot; cd openpilot; git checkout 0.8.8-shane-spektor-honda-toyota-coasting && git submodule update --init --recursive && sudo reboot`  
  
SSH Install on the Comma Two:  
`cd /data; cp -rf ./openpilot ./openpilot.bak; rm -rf ./openpilot; git clone https://github.com/Aragon7777/openpilot.git openpilot; cd openpilot; git checkout 0.8.8-shane-spektor-honda-toyota-coasting && git submodule update --init --recursive && reboot`  
  
If you already installed but it fails to compile (Comma Three):   
`git submodule update --init --recursive && sudo reboot`   
  
If you already installed but it fails to compile (Comma Two):   
`git submodule update --init --recursive && reboot`  
