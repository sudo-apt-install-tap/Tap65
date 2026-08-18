---
title: "Tap65"
author: "Tap"
description: "A simple 68 key based layout!"
created_at: "2026-05-17"
---

# May 17: Worked on the new pico based schematic and did the PCB layout!

So I did work on the schematic and the some of the pcb layout for the keyboard. I ended up scraping the old stm32 based embedded design.

![image](https://stasis.hackclub-assets.com/images/1779013710119-1deiqt.png)

![image](https://stasis.hackclub-assets.com/images/1779013739489-byjv19.png)

![image](https://stasis.hackclub-assets.com/images/1779013710119-1deiqt.png)
![image](https://stasis.hackclub-assets.com/images/1779013739489-byjv19.png)

into this

**Total time spent: 4hour**

# May 18: Finished the layout!

So I put the neopixles and the diodes in the place! It was monotonus but i liked doing it!!

Also the SK6812 Mini are really fricking expensive!

![image](https://stasis.hackclub-assets.com/images/1779088134619-7v1hrd.png)

![image](https://stasis.hackclub-assets.com/images/1779088152512-lwlarg.png)

![image](https://stasis.hackclub-assets.com/images/1779088134619-7v1hrd.png)
![image](https://stasis.hackclub-assets.com/images/1779088152512-lwlarg.png)

**Total time spent: 1.5hour**

# May 19: Neopixeles! Again!!

So I think I messed something up during the schematic phase and when i went to connect neopixles in a chain, Well the chain wasnt present, it was gone!

I decided to again make a new chain, this forced me to delete and start the routing from ground up again!

This time i did it properly and my routing is also much more cleaner, so I guess it should work properly.

Also I found a listing of the neopixels @ $17 for 200!

![image](https://stasis.hackclub-assets.com/images/1779187263683-8v3pmr.png)

I will have to start routing the neopixels again but never the less its great!

![image](https://stasis.hackclub-assets.com/images/1779187263683-8v3pmr.png)

**Total time spent: 3h**

# May 19: Finished PCB Routing!

Finished the full layout and routing! So it took FOREVER but I finally finished it and i used a hatched ground fill cuz why not!!

![image](https://stasis.hackclub-assets.com/images/1779211990352-ldjo9p.png)

![image](https://stasis.hackclub-assets.com/images/1779212011161-lxvwva.png)

Will work on the art/silkscreen the next time!

![image](https://stasis.hackclub-assets.com/images/1779211990352-ldjo9p.png)
![image](https://stasis.hackclub-assets.com/images/1779212011161-lxvwva.png)

**Total time spent: 4.5h**

# June 19: Added stabalizers and changed other stuff!

So I Added stabalizers as I did not want to use plate mounted ones because they tend to suck. Also i removed the hatched paturn and did a full GND pour, this makes it much more heavier and will probly make it feel pretty premium. Also as this is a 68 key layout I will be using a standard tray mount as it is much easier to design and opporate than a gasket mount. Did not go plateless as that wouldve made it more fragile. Anyways looks pretty good, will move on to case design the next day and yeah we will be done!

![image](https://github.com/user-attachments/assets/d9337de5-0cd0-451c-8f7c-92222b012bb2" />
![image](https://github.com/user-attachments/assets/452edccd-a6e3-44a7-af94-e941d1c5f72b" />
![image](https://github.com/user-attachments/assets/c220d1da-27cd-4909-875c-2eee7fe110d6" />
![image](https://github.com/user-attachments/assets/8d150a7d-dae7-4e11-9229-790d00debb39" />
![image](https://github.com/user-attachments/assets/de928ac4-1ee6-4eb2-9295-9bba2961d62c" />
![image](https://github.com/user-attachments/assets/a52f4ddf-1c62-45aa-880a-6c35d43a6e29" />

**Total time spent: 1h**

# June 19: Added stabalizers and changed other stuff!

So today I finally got around to designing the case in Onshape!! I decided to keep it pretty simple and went with a standard 2 piece PLA tray mount case since the PCB was already designed around tray mounting. I also added a 7° typing angle because flat keyboards just don't feel that great to type on.I also filleted the edges around the plate so it doesn't look like a giant brick anymore lol. It honestly made the whole thing look much cleaner than before. Surprisingly I did not have to any major issues! Anyways the case is basically done now! Next thing I'll be working on is the firmware, and after that hopefully I'll be able to get a prototype made!!

![image](https://github.com/user-attachments/assets/19169598-c03d-49da-bbef-be4b6f581756" />
![image](https://github.com/user-attachments/assets/724045fb-e096-4512-8686-6f1963e7329c" />
![image](https://github.com/user-attachments/assets/7eddb9a4-db3f-448d-a123-49751fe3a66d" />
![image](https://github.com/user-attachments/assets/eaaf7925-9af5-44d9-977c-6b78e82492d5" />
![image](https://github.com/user-attachments/assets/9e8b4d8a-e3ff-4ccf-9b2e-bc140cf3d125" />

**Total time spent: 2h**

# July 1: Finished Firmware!

Today I started working on the KMK firmware for the keyboard. I set up the project structure, created the base 68-key keymap, and added a function layer with navigation and function keys. It took a bit of trial and error to understand how KMK handles layers and matrix scanning, but I eventually got a solid starting point. I also cleaned up the Git repository after accidentally committing some generated CAD files that were far too large for GitHub. With the firmware project now set up, the next step is to test the matrix on the actual PCB and begin adding features like RGB lighting and any other quality-of-life improvements.

![image](https://github.com/user-attachments/assets/91caef53-7288-4ed7-a3ee-3bfb27f7796f)

**Total time spent: 1h 30mins**

# July 2: Wrote The Readme!

Today I wrote a proper README for the project, documenting the keyboard's features, design process, bill of materials, and what I learned while building it. I also went back into the CAD model and fixed a few alignment issues between the case, plate, and PCB to make sure everything lines up correctly before manufacturing.

Finished look!

<img width="899" height="382" alt="image" src="https://github.com/user-attachments/assets/9f031004-d081-47d2-af4c-5a91f835d4fa" />
<img width="1366" height="680" alt="image" src="https://github.com/user-attachments/assets/36a34fda-6ab5-4bc1-b7d7-97ea0d03415e" />

**Total time spent: 1h**

# July 16: Got all the parts and test mounted stabs

Today I got all the PCB, keycaps and the switches, diodes and other stuff like stabilizers. The PCB was sponsored  by JLCPCB and i got DHL to deliver it so it was super duper fast. The keycaps and keyboard components were ordered from some local shops so it was very fast too!

heres some pic:

<img width="1600" height="900" alt="PCBs DAY1" src="https://github.com/user-attachments/assets/0de0c390-2553-4075-acc6-e70c41a075bf" />
<img width="1600" height="900" alt="Keycaps" src="https://github.com/user-attachments/assets/6d85a90a-ca88-4e9a-8e91-652078ad4d7a" />
<img width="1600" height="900" alt="PCB Stabalizer Fit" src="https://github.com/user-attachments/assets/3ec04747-76bd-477b-ac93-4c31fa97ecbf" />

**Total time spent: 30mins**

# 17 July: Soldered the hotswap sockets and some neopixles!

So soldering was very mind numbing and tedious, I did take a long time to solder all of them. I also soldered all the hotswap sockets but only a few neopixles in because i just wanted to test it. 

<img width="900" height="1600" alt="cool shot" src="https://github.com/user-attachments/assets/c732544a-0d97-4e0c-8f31-599030cdbc26" />
<img width="1600" height="900" alt="Initial Neopixles" src="https://github.com/user-attachments/assets/cdca4ee8-0114-4658-bedb-9cea7dd13f75" />
<img width="1600" height="900" alt="Half Finished PCB" src="https://github.com/user-attachments/assets/d8ef1d06-9c94-46e2-be34-304911d1ce87" />

> Half soldered sockets

<img width="900" height="1600" alt="Finished PCB" src="https://github.com/user-attachments/assets/2d85ed51-6ea8-4bec-8707-76b5b2c20533" />
<img width="900" height="1600" alt="Soldering" src="https://github.com/user-attachments/assets/98bbec54-bc04-49bf-912b-b66089c27251" />

**Total time spent: 6h**

# 18 July: Got the rubber feet + more images

So I got the rubber feet(they use this in furniture and shit) but it does give grip to stuff regardless so, I used it. Also I took another picture!

<img width="1200" height="1600" alt="PCB" src="https://github.com/user-attachments/assets/a38199e7-320e-447c-9427-5ea7d63b31f7" />
<img width="1600" height="1200" alt="grips" src="https://github.com/user-attachments/assets/8d858ab2-4572-453c-9abd-6140c5b185d9" />

**Total time spent: 30mins**

# 19 July: Soldered the clone pico

I used a clone RPi pico instead of a standard one because the standard one uses a usb-b port. So I turned my head to the widely available pico clones on the market. I eventually got one from makerbazzar for cheaper than the original one.

<img width="1600" height="900" alt="clone soldered on" src="https://github.com/user-attachments/assets/33a6b89a-a98e-4309-b5b8-5ca4e86f5250" />

**Total time spent: 30mins**

# 20 July: Debugged the neopixles.

So I did something very stupid, the neopixles, sk6812 mini-e and normal sk6812 have the same looking symbols in KiCAD, BUT the one and only difference is that the pin numbers, according to the datasheet for the mini-e variant it doesn't match, so the connections and traces are faulty. This leads to a failure in the basic pcb which can not be fixed/patched in anyway after production. But still the keyboard works well enough. This took me longer than it should've to figure it out . And I think that was enough yapping, so, heres some pics!!

<img width="1600" height="1200" alt="Finished(withStabs)" src="https://github.com/user-attachments/assets/84fe773d-b7e4-4218-bb99-b0ddc30a03a5" />
<img width="1200" height="1600" alt="Closeup shot of neopixels" src="https://github.com/user-attachments/assets/757b9129-b660-4c02-9225-6ef90cbbc25f" />

**Total time spent: 2h 30mins**

# 25 July: assembled the board

So I assembled the board, I just had to melt the two pieces of keyboard together. The heat set inserts were inserted by using a tweezers and a soldering iron. Then I just had to screw it into the case.

<img width="1600" height="1200" alt="Build Pt2" src="https://github.com/user-attachments/assets/3fc2e669-8c0b-4ff9-8b21-827e9ad6b6cd" />
<img width="1600" height="900" alt="Finished Build" src="https://github.com/user-attachments/assets/863e78e8-6f74-40eb-930f-797b74f15170" />


# 26 July: Lubed the stabilizers!

I just used a rabbit hair brush no 1 to brush some krytox 2O5g into the housing and the wire to do make it sound better. So yeah that's about it lubing is pretty easy to be honest just takes a while and had to open and close it which tbh takes a bit of time.

<img width="1600" height="1200" alt="Lubed Stabs" src="https://github.com/user-attachments/assets/4883369a-9a92-483c-98d9-cb306199706f" />
<img width="1600" height="900" alt="Keyboard after lubing" src="https://github.com/user-attachments/assets/20f92018-414f-418c-bacf-67087a088dbb" />
https://github.com/user-attachments/assets/0e627ef8-ceec-4c1e-9f21-f2216cf7b69a
