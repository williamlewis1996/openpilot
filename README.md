[![](https://i.imgur.com/lGnO4Oq.png)](#)

Aragon's Openpilot Fork
------

This fork is a collection of many different features from other forks and some of my own neatly packaged together for an excellent Openpilot experience.

↪️ Lateral Features
------
* Honda: Seperate LKAS and ACC similar to how stock Honda Sensing performs, thanks to Spektor56.
* Engagement in gears other than drive, such as sport and low.
* Nudgeless assisted lane changes above 30MPH. Tune in `selfdrive/controls/lib/lateral_planner.py` on line 126.

↩️ Longitudinal Features
------
* No disengagement when gas is pressed.
* Honda: Custom follow distances. Use the distance button on the steering wheel to cycle through the bars while cruise is engaged.
* Honda: Custom braking profiles. Earlier braking in stop-and-go traffic as well as highway profiles. Tune in `selfdrive/controls/lib/long_mpc.py`.
* (Coasting branch only): Coast over the set speed, then use the regular brakes after meeting a certain threshold. Standard is 10MPH, edit in `selfdrive/controls/lib/longitudinal_planner.py` on line 22. 
* Comma pedal adjustments. For Hondas, this means stock logic of increments of +1MPH and holding for +5MPH.
* Comma pedal tuning. Less jerky from a stop but accelerates faster later on.

🚗 General Features
------
* DevUI thanks to wirelessnet2.
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
