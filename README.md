# GerbCam ONE

This is A tool to keep an eye on my pet gerbils while I'm away on holiday. It is designed to run on a Raspberry Pi and any old webcam you have collecting dust.

## Hardware

The hardware on this is a simple battery PCB which converts the 12V from 8 AA batteries to 5V for the Raspberry Pi. It could work with 3.7 V lithium-ion cells but is untested.

## Software

The Raspberry Pi runs the motion detecting algorithm which scans every 4th frame for movement and records when motion is found. The Pi also hosts the website

## Instructions

- Make sure to put in your site a password into ddns.sh as I obviously haven't added mine
- Case should be assembled with M3 heat inserts and M3 6mm bolts
- Configure cron to run startup.sh

Onshape URL: https://cad.onshape.com/documents/b9b5efc3e67051879257010d/w/97c2399b92ab84e6df797935/e/d288fcda08a8171d0bd35e9a

Thank you to hack club for keeping me motivated to finish this.
