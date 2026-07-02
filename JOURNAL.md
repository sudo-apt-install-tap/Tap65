# 7/2/2026 12:45 PM - Wrote The Readme!

*Time spent: 1h*

Today I wrote a proper README for the project, documenting the keyboard's features, design process, bill of materials, and what I learned while building it. I also went back into the CAD model and fixed a few alignment issues between the case, plate, and PCB to make sure everything lines up correctly before manufacturing.

Finished look!

<img width="899" height="382" alt="image" src="https://github.com/user-attachments/assets/9f031004-d081-47d2-af4c-5a91f835d4fa" />
<img width="1366" height="680" alt="image" src="https://github.com/user-attachments/assets/36a34fda-6ab5-4bc1-b7d7-97ea0d03415e" />


# 7/1/2026 4 PM - Finished Firmware!

*Time spent: 1h 30mins*

Today I started working on the KMK firmware for the keyboard. I set up the project structure, created the base 68-key keymap, and added a function layer with navigation and function keys. It took a bit of trial and error to understand how KMK handles layers and matrix scanning, but I eventually got a solid starting point. I also cleaned up the Git repository after accidentally committing some generated CAD files that were far too large for GitHub. With the firmware project now set up, the next step is to test the matrix on the actual PCB and begin adding features like RGB lighting and any other quality-of-life improvements.

<img width="689" height="584" alt="image" src="https://github.com/user-attachments/assets/91caef53-7288-4ed7-a3ee-3bfb27f7796f" />


# 6/19/2026 11 PM - Added stabalizers and changed other stuff!

_Time spent: 2h_

So today I finally got around to designing the case in Onshape!! I decided to keep it pretty simple and went with a standard 2 piece PLA tray mount case since the PCB was already designed around tray mounting. I also added a 7° typing angle because flat keyboards just don't feel that great to type on.I also filleted the edges around the plate so it doesn't look like a giant brick anymore lol. It honestly made the whole thing look much cleaner than before. Surprisingly I did not have to any major issues! Anyways the case is basically done now! Next thing I'll be working on is the firmware, and after that hopefully I'll be able to get a prototype made!!

<img width="843" height="413" alt="image" src="https://github.com/user-attachments/assets/19169598-c03d-49da-bbef-be4b6f581756" />
<img width="843" height="413" alt="image" src="https://github.com/user-attachments/assets/724045fb-e096-4512-8686-6f1963e7329c" />
<img width="654" height="203" alt="image" src="https://github.com/user-attachments/assets/7eddb9a4-db3f-448d-a123-49751fe3a66d" />
<img width="809" height="320" alt="image" src="https://github.com/user-attachments/assets/eaaf7925-9af5-44d9-977c-6b78e82492d5" />
<img width="809" height="320" alt="image" src="https://github.com/user-attachments/assets/9e8b4d8a-e3ff-4ccf-9b2e-bc140cf3d125" />

# 6/19/2026 11 PM - Added stabalizers and changed other stuff!

_Time spent: 1h_

So I Added stabalizers as I did not want to use plate mounted ones because they tend to suck. Also i removed the hatched paturn and did a full GND pour, this makes it much more heavier and will probly make it feel pretty premium. Also as this is a 68 key layout I will be using a standard tray mount as it is much easier to design and opporate than a gasket mount. Did not go plateless as that wouldve made it more fragile. Anyways looks pretty good, will move on to case design the next day and yeah we will be done!

<img width="909" height="326" alt="image" src="https://github.com/user-attachments/assets/d9337de5-0cd0-451c-8f7c-92222b012bb2" />
<img width="909" height="326" alt="image" src="https://github.com/user-attachments/assets/452edccd-a6e3-44a7-af94-e941d1c5f72b" />
<img width="939" height="282" alt="image" src="https://github.com/user-attachments/assets/c220d1da-27cd-4909-875c-2eee7fe110d6" />
<img width="939" height="282" alt="image" src="https://github.com/user-attachments/assets/8d150a7d-dae7-4e11-9229-790d00debb39" />
<img width="939" height="282" alt="image" src="https://github.com/user-attachments/assets/de928ac4-1ee6-4eb2-9295-9bba2961d62c" />
<img width="939" height="282" alt="image" src="https://github.com/user-attachments/assets/a52f4ddf-1c62-45aa-880a-6c35d43a6e29" />

# 5/19/2026 5 PM - Finished PCB Routing!

_Time spent: 4.5h_

Finished the full layout and routing! So it took FOREVER but I finally finished it and i used a hatched ground fill cuz why not!!


![image](https://stasis.hackclub-assets.com/images/1779211990352-ldjo9p.png)

![image](https://stasis.hackclub-assets.com/images/1779212011161-lxvwva.png)

Will work on the art/silkscreen the next time!

![image](https://stasis.hackclub-assets.com/images/1779211990352-ldjo9p.png)
![image](https://stasis.hackclub-assets.com/images/1779212011161-lxvwva.png)

# 5/19/2026 10 AM - Neopixeles! Again!!

_Time spent: 3h_

So I think I messed something up during the schematic phase and when i went to connect neopixles in a chain, Well the chain wasnt present, it was gone!

I decided to again make a new chain, this forced me to delete and start the routing from ground up again! 

This time i did it properly and my routing is also much more cleaner, so I guess it should work properly. 

Also I found a listing of the neopixels @ $17 for 200!


![image](https://stasis.hackclub-assets.com/images/1779187263683-8v3pmr.png)

I will have to start routing the neopixels again but never the less its great!

![image](https://stasis.hackclub-assets.com/images/1779187263683-8v3pmr.png)

# 5/18/2026 7 AM - Finished the layout!

_Time spent: 1.5h_

So I put the neopixles and the diodes in the place! It was monotonus but i liked doing it!!

Also the SK6812 Mini are really fricking expensive!

![image](https://stasis.hackclub-assets.com/images/1779088134619-7v1hrd.png)

![image](https://stasis.hackclub-assets.com/images/1779088152512-lwlarg.png)

![image](https://stasis.hackclub-assets.com/images/1779088134619-7v1hrd.png)
![image](https://stasis.hackclub-assets.com/images/1779088152512-lwlarg.png)

# 5/17/2026 10 AM - Worked on the new pico based schematic and did the PCB layout!

_Time spent: 4h_

So I did work on the schematic and the some of the pcb layout for the keyboard. I ended up scraping the old stm32 based embedded design.


![image](https://stasis.hackclub-assets.com/images/1779013710119-1deiqt.png)

![image](https://stasis.hackclub-assets.com/images/1779013739489-byjv19.png)

![image](https://stasis.hackclub-assets.com/images/1779013710119-1deiqt.png)
![image](https://stasis.hackclub-assets.com/images/1779013739489-byjv19.png)
