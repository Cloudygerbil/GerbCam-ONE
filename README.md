# GerbCam ONE

This is A tool to keep an eye on my pet gerbils while I'm away on holiday. It is designed to run on a Raspberry Pi and any old webcam you have collecting dust.

## Hardware

The hardware on this is a simple battery PCB which converts the 12V from 8 AA batteries to 5V for the Raspberry Pi. It could work with 3.7 V lithium-ion cells but is untested.

<img width="872" height="562" alt="image" src="https://github.com/user-attachments/assets/024a25f1-4ee8-463d-b62b-fd61b5e7c149" />

## Software

The Raspberry Pi runs the motion detecting algorithm which scans every 4th frame for movement and records when motion is found. The Pi also hosts the website

## Instructions

- Make sure to put in your site a password into ddns.sh as I obviously haven't added mine
- Case should be assembled with M3 heat inserts and M3 6mm bolts
- Configure cron to run startup.sh

Onshape URL: https://cad.onshape.com/documents/b9b5efc3e67051879257010d/w/97c2399b92ab84e6df797935/e/d288fcda08a8171d0bd35e9a

BOM:

| Material | Qty | Value |
| --- | --- | --- |
| PLA | 200g | White and Orange |
| LM2596S-5 | 1 | none |
| Inductor | 1 | 33 µH |
| Screw Terminal | 1 | Screw_Terminal_2_P5.00mm |
| Diode | 1 | SR503 |
| Capacitor | 1 | 220 µF |
| Capacitor | 1 | 680 µF |
| AA Batteries holder | 4 | 2 Batteries |
| M3 Bolts | 4 | 6 mm depth |
| M3 Heat inserts | 4 | 4 mm depth |
| Webcam | 1 | USB connector |
| Raspberry Pi Zero W | 1 | null |
| AA Batteries holder | 8 | Should be rechargable |
| USB Female to USB micro male converter | 1 | preferably low profile |
Thank you to hack club for keeping me motivated to finish this.
