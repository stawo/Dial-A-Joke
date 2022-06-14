import requests
import json
import pyttsx3
import random
import RPi.GPIO as GPIO # Import Raspberry Pi GPIO library
import time

GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
GPIO.setup(10, GPIO.IN, pull_up_down=GPIO.PUD_DOWN) # Set pin 10 to be an input pin and set initial value to be pulled low (off)

print('Start')

# Initialize the TTS
engine = pyttsx3.init()

"""VOLUME"""
volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
print (volume)                          #printing current volume level
engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1

""" RATE"""
rate = engine.getProperty('rate')   # getting details of current speaking rate
print (rate)                        #printing current voice rate
engine.setProperty('rate', 100)     # setting up new voice rate

def get_joke():
    url = "https://rapidapi.p.rapidapi.com/joke/Any"

    querystring = {
        "format":"json"
        ,"blacklistFlags":"racist"
        # ,"idRange":"0-150"
        ,"type":"single,twopart"
        }

    headers = {
        'x-rapidapi-key': "...",
        'x-rapidapi-host': "jokeapi-v2.p.rapidapi.com"
        }
    
    response = requests.request("GET", url, headers=headers, params=querystring)
    print(response.text)
    response_json = json.loads(response.text)
    
    if response_json['type'] == 'single':
        joke = response_json['joke']
    elif response_json['type'] == 'twopart':
        joke = response_json['setup'] + '\n' + response_json['delivery']
    
    return joke

def read_joke(joke):
    engine.say(joke)
    engine.runAndWait()

while True: # Run forever
    if GPIO.input(10) == GPIO.HIGH:
        print("Button was pushed!")
        
        read_joke(get_joke())
        
    else:
        print('.')
    
    time.sleep(1)