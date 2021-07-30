[![](https://i.imgur.com/lGnO4Oq.png)](#)

Aragon's Openpilot Fork
------

This fork is a collection of many different features from other forks and some of my own neatly packaged together for an excellent Openpilot experience.

🚗 Core Features
------
* You **must** enable allow gas pressed in the settings for the features to work correctly.
* This fork is based off of [Dragonpilot](https://github.com/dragonpilot-community/dragonpilot) which has is known to have many features.
* If bugs in my fork are the result of Dragonpilot, I will do my best to fix them but cannot guarantee anything.
* If you are looking for a lightweight branch that just has seperate LKAS and ACC, this isn't the branch for you.

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