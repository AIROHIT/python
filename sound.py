from imp import source_from_cache
import pyttsx3

sound = pyttsx3.init()

rate = sound.getProperty('rate')   # getting details of current speaking rate                        #printing current voice rate
sound.setProperty('rate', 150)     
voices = sound.getProperty('voices')
sound.setProperty('voice', voices[1].id)


sound.say("Hello Rohit, welcome to your computer")

sound.runAndWait()