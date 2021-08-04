[![](https://i.imgur.com/lGnO4Oq.png)](#)

🚗 Read before installing!
------
To increase the probability that you have an excellent experience and chose the right branch for your car, it is recommended to read this before proceeding.

🚗 Branch Definitions
------
* Shane: Includes some or all of Shane's fork abilities: https://github.com/sshane/openpilot
* DP: Includes Dragonpilot as the core. Dragonpilot has many different customization options accessible from the UI: https://github.com/dragonpilot-community/dragonpilot
* Spektor: Lane keeping assist can be activatrd indepently of adaptive cruise control. Only for Hondas before 0.8.6, Toyota support added recently.
* Honda: Honda-specific branch that utilizes the follow distance selector on the steering wheel to specific profiles. Not recommended for other cars.
* Coasting: Only works well on Hondas & GMs. Branch has the functionality to coast beyond the set speed (including downhills) instead of using the brakes.
* Devel: Branches in development. Check the commit history to see what's being worked on. No stability guarantees.
* Personal: Branches used on my own fleet of cars. No stability guarantees.

🚗 Installation
------
* Some branches (especially DP) are known to not work well without a factory reset first. Failing to do so may have errors or conflicts later on. [Check this video for instructions on how to factory reset.](https://youtu.be/0MPv_hSH3hk?t=98)
* If using the Dragonpilot branch, enable "Allow Gas Pressed" in the controls settings to work with the standalone LKAS function properly.
* Install via URL: https://smiskol.com/fork/aragon7777/REPLACE_WITH_BRANCH_NAME
* Install via SSH: `cd /data; cp -rf ./openpilot ./openpilot.bak; rm -rf ./openpilot; git clone https://github.com/Aragon7777/openpilot.git openpilot; cd openpilot; git checkout REPLACEWITHBRANCHNAME && reboot`

↪️ Lateral Features
------
* Honda and Toyota: Behavior like stock Honda Sensing, thanks to Spektor56. 
*      LKAS and ACC are two seperate functions that can be used independently.
*           LKAS is activated using the LKAS button the steering wheel.
*           LKAS is active when the built in HUD lanelines are solid. 
*           LKAS is inactive when the built in HUD lanelines are outlined.
*           LKAS will disengage on brake, but automatically come back.
*           LKAS will disengage below the Auto Lane Change (ALC) speed with blinker.
*           LKAS will stay disengaged briefly after blinkers, this helps driver recenter wheel.
*           LKAS will stay disengaged if seatbelt unlatched, door open, or unsupported gear.
*           ACC is activated using the SET or RES(ume) button on the steering wheel.
*           ACC will disengage on brake, and never automatically come back until reset by the driver.
*           ACC can be adjusted in increments of 1MPH or +5MPH by holding, even with a (Honda) comma pedal.
*           ACC will not engage if seatbelt unlatched, door open, or unsupported gear.

* Engagement in gears other than drive, such as sport and low.
* Nudgeless assisted lane changes above 30MPH. Tune in `selfdrive/controls/lib/lateral_planner.py` on line 126.

↩️ Longitudinal Features
------
* All of Dragonpilot goodies. 
* In order to get follow and acceleration profiles, you must enable them in the settings. Only then will there be buttons after turning the car on.
* Coast over the set speed instead of using the brake pads, this time with less bugs.

🚗 General Features
------
* All of Dragonpilot goodies.
* Alerts have mostly been rewritten. Better grammar and more details on specific events. Some sounds like torque alerts have been muted.
* Update prompt forcing an internet connection to check for updates has been disabled.
* Reduced the potentional for false driving model lagging alerts.
* Tesla warning sound effect under specific situations.

🏆 Special Thanks
------
[Spektor56](https://github.com/spektor56/openpilot)   
[eisenheim](https://github.com/eyezenheim/openpilot)  
[ShaneSmiskol](https://github.com/ShaneSmiskol/openpilot)    
[wirelessnet2](https://github.com/wirelessnet2/openpilot)    
[kegman](https://github.com/kegman/openpilot)    
[cfranhonda](https://github.com/cfranhonda/openpilot)    
[doktor](https://github.com/doktorsleepelss)    
[qadmus](https://github.com/qadmus/openpilot)  
[reddn](https://github.com/reddn)

📬 If you'd like to reach out to me, message `Aragon#7777` on Discord, or tag me in #custom-forks on the official Comma server regarding this branch.
