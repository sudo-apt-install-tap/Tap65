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

# 1/14/2026 12 PM - Taps65

_Time spent: 3h_

Hey keyboard lovers!!
## Intro
Through this project I aim to create a keyboard that is capable of replacing my current daily driver. I am going to be following ai03's guide throughout the entirity of this project if you want to follow through with me you should reffer to his guide for any info that you do not understand. Also I am open to help you make any type of keyboard you want, just shoot me a dm on slack **@taps** or email me at work.tapishnud@gmail.com.

## 14 January 2026
 Today I worked on the schematic, mainly focusing on the MCU and the USB port.

ai03’s guide uses a USB Type-B connector, but I decided to switch to USB Type-C instead. Mostly for convenience—and also because I really don’t want to carry a Type-B cable around just for my keyboard. It’s 2026, we deserve better.

So far, I’ve completed the MCU section and the USB-C implementation. I’ll be iterating on this and adding protection components later, but this felt like a solid first step.

Below are the schematics I worked on today: 

![image](https://blueprint.hackclub.com/user-attachments/blobs/proxy/eyJfcmFpbHMiOnsiZGF0YSI6ODI1MjIsInB1ciI6ImJsb2JfaWQifX0=--26a4db1f35223cf6965914c0c246d84a4caa20a2/image.png)
MCU Schematic  
![image](https://blueprint.hackclub.com/user-attachments/blobs/proxy/eyJfcmFpbHMiOnsiZGF0YSI6ODI1MjMsInB1ciI6ImJsb2JfaWQifX0=--00a4724328d05804050f3cda232ec35b5a40bab3/image.png)
USB C Schematic

![image](https://blueprint.hackclub.com/user-attachments/blobs/proxy/eyJfcmFpbHMiOnsiZGF0YSI6ODI1MjIsInB1ciI6ImJsb2JfaWQifX0=--26a4db1f35223cf6965914c0c246d84a4caa20a2/image.png)
![image](https://blueprint.hackclub.com/user-attachments/blobs/proxy/eyJfcmFpbHMiOnsiZGF0YSI6ODI1MjMsInB1ciI6ImJsb2JfaWQifX0=--00a4724328d05804050f3cda232ec35b5a40bab3/image.png)
