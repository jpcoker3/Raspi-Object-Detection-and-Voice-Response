# Raspi Object Detection and Voice Response

## Introduction
This project aims to use computer vision to detect when I am at my desk and when my phone is detected, use text-to-voice to remind me to put my phone away.

At some point, I would like to add more functionality so that it can interface with chat gpt and hold conversations. 

This project is primarily based on [this](https://github.com/thyagarajank/Object-Detection-with-Voice-Feedback-using-Raspberry-Pi-4-and-bullseye-OS). At the time of initial creation, Bullseye OS was just released and there were many issues with ML packages, and the new OS had issues with the legacy camera software. The package installation script from the previously mentioned project has fixed most of these issues.  


## Parts :: ~$200
The primary cost of this build is the Raspberry Pi itself as this model is becoming harder and harder to obtain. The HQ camera is also expensive at $50, but a lesser camera should work perfectly fine. \
[Raspberry Pi 4B 8GB ram](https://www.adafruit.com/product/4564) \
[Pi Oled](https://www.adafruit.com/product/3527)\
[Raspberry Pi HQ Camera](https://www.adafruit.com/product/4561)\
[Camera Lens](https://www.amazon.com/dp/B088BLZKRG?psc=1&ref=ppx_yo2ov_dt_b_product_details)\
[Speaker](https://www.amazon.com/gp/product/B07GJ4GH67/ref=ppx_yo_dt_b_asin_title_o00_s00?ie=UTF8&psc=1)\
[Fans Taken from this case](https://www.amazon.com/Raspberry-Model-Aluminum-Cooling-Metal/dp/B07VQLBSNC/ref=asc_df_B07VQLBSNC/?tag=hyprod-20&linkCode=df0&hvadid=633001802341&hvpos=&hvnetw=g&hvrand=746087739099635072&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9014113&hvtargid=pla-809661377459&psc=1) I believe the fans are 25x25x10 mm\
[Microphone](https://www.amazon.com/gp/product/B07SNSY64C/ref=ppx_yo_dt_b_asin_title_o00_s01?ie=UTF8&psc=1)\
[Flex Arm Stand](https://www.amazon.com/dp/B071VR8PWF?psc=1&ref=ppx_yo2ov_dt_b_product_details)\
[Misc Wires and Cables](https://www.amazon.com/dp/B01LZF1ZSZ?psc=1&ref=ppx_yo2ov_dt_b_product_details)


## Case Design
I created a custom case for all these parts to make it seem less thrown together. ( WIP ) 

here is the basic design: \
![case front](https://github.com/jpcoker3/Raspi-Object-Detection-and-Voice-Response/blob/master/Case-Model/case_front.png)
![case back](https://github.com/jpcoker3/Raspi-Object-Detection-and-Voice-Response/blob/master/Case-Model/case_back.png)

## Pins
Pi Oled: 1,2,3,5,6. Note that pin 4 is not used. this pin (5v) is not utilized by the OLED and we will use it for other items later. \
Fans: 4, 14. Power and ground. \
Speaker: 17, 25. The model speaker linked above is able to run on 3.3v, and as that is the only power pin available we will use it. 

![Raspi 4 Pins](https://github.com/jpcoker3/Raspi-Object-Detection-and-Voice-Response/blob/master/images/pinout-corrected.jpg)
