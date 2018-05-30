#!/usr/bin/python3

import os
from os import system
import speech_recognition as sr
from gtts import gTTS
import subprocess

from pygame import mixer
mixer.init()

r = sr.Recognizer()
with sr.Microphone() as source:
	system('clear')
	tts= gTTS(text="Good Morning Subham, any question you want to ask?", lang = 'en')
	tts.save("commands.mp3")
	mixer.music.load('commands.mp3')
	mixer.music.play()
	r.adjust_for_ambient_noise(source,duration=5)
	audio = r.listen(source)
	
query = r.recognize_google(audio)
print(query)
commands = query.split(" ")
list_commands = list(commands)
print(list_commands)
print(len(list_commands))


for i in range(len(list_commands)):
	if list_commands[i] =="date" :
		Date =subprocess.call(["date","+%d-%m-%y | espeak"])
		print(Date)
	elif list_commands[i] == "make": #and  list_commands[i]==" directory" :
		directory = subprocess.call(["mkdir" ,"/home/subham/Desktop/b"])
		sound_prgrm= "/usr/bin/cvlc" #place the path to player here
		sound_file="c.mp3" #alarm tone
		subprocess.call([sound_prgrm, sound_file])		


		#tts= gTTS(text="successfully created your directory", lang = 'en')
		#tts.save("c.mp3")
		#os.startfile('c.mp3')
	#	mixer.music.load('c.mp3')
	#	mixer.music.play()




	else:
		print("wait for valid input")
