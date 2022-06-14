# Setup

Steps:

1. Download latest Raspberry Pi OS Lite (https://www.raspberrypi.org/software/operating-systems/)
2. Flash it on the SD card
3. Start the Raspberry Pi, and login with username `pi` and password `raspberry` (https://www.raspberrypi.org/documentation/linux/usage/users.md)
4. Connect to Wi-Fi (https://www.raspberrypi.org/documentation/configuration/wireless/wireless-cli.md)
5. Activate SSH (https://www.raspberrypi.org/documentation/configuration/raspi-config.md)
6. Install pip with `sudo apt install python3-pip` (https://www.raspberrypi.org/documentation/linux/software/python.md)
7. Install Espeak NG with `sudo apt-get install espeak-ng` (https://github.com/espeak-ng/espeak-ng/blob/master/docs/guide.md)
   1. https://github.com/espeak-ng/espeak-ng/blob/master/docs/voices.md
8. 

# Issues

## TTS Engine

### TTS Engines available

- https://mimic.mycroft.ai/
- https://www.knowledgenile.com/blogs/open-source-tts-engine/

### Espeak-NG
Espeak-NG works out of the box, but the voice is quite robotic and it seems to "chew" the words.

Possible solutions:

- use Mbrola voices \
  The installation does not appear straight-forward.
  - https://www.raspberrypi.org/forums/viewtopic.php?t=148096
  - https://forum.dronebotworkshop.com/help-wanted/espeak-espeak-ng-pyttsx3-and-mbrola/paged/2/
  - https://github.com/espeak-ng/espeak-ng/blob/master/docs/mbrola.md
  - https://packages.debian.org/buster/armhf/mbrola/download

# Button Test

Try one of the many tutorials. Example: https://www.makeuseof.com/tag/add-button-raspberry-pi-project/
Usually they involve an LED, but you can skip it.

Steps:

1. On your main pc, copy the file `raspberry_test_button.py` over to the Raspberry Pi \
  `scp raspberry_test_joke.py pi@[RASPBERRYPI IP]:/home/pi/`
2. Run the file `raspberry_test_button.py` \
  `python3 raspberry_test_button.py`

Make sure that when the button is pressed, the output prints the proper result.

# Dial-A-Joke Test

Steps:

1. Install `pyttsx3` with `pip3 install pyttsx3`
2. On your main pc, copy the file `raspberry_test_joke.py` over to the Raspberry Pi \
  `scp raspberry_test_joke.py pi@[RASPBERRYPI IP]:/home/pi/`
2. Connect the hearphones to the Raspberry Pi
3. Run the file `raspberry_test_joke.py` \
  `python3 raspberry_test_joke.py`

Make sure that when the button is pressed, you can hear a joke through the hearphones.