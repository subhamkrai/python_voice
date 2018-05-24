import speech_recognition as sr
import apiai
import json 
from os import system
import wikipedia as wiki
import webbrowser as wb
from gtts import gTTS
from pygame import mixer
mixer.init()


CLIENT_ACCESS_TOKEN = "2245d4ab7c99466e806c8986a18234c4"
ai = apiai.ApiAI(CLIENT_ACCESS_TOKEN)

google_search = "https://www.google.com/search?q="
youtube_search = "https://www.youtube.com/results?search_query="
google_drive = "https://drive.google.com"
gmail = "https://mail.google.com"	

while(True==True):
	r = sr.Recognizer()
	with sr.Microphone() as source:
		r.adjust_for_ambient_noise(source, duration=1)
		#print("Say something!")
		tts=gTTS(text="say any thing you want to browse in google or youtube or wikipedia")
		tts.save("a2.mp3")
		mixer.music.load("a2.mp3")
		mixer.music.play()
		audio=r.listen(source,phrase_time_limit=15)

	try:
		query = r.recognize_google(audio)
		
		request = ai.text_request()
		request.query = query  
		response = request.getresponse()
		json_data = (response.read())
		say =  json.loads(json_data.decode('utf-8'))
		#print(say)
		speech = say['result']['fulfillment']['speech']
		search = speech.split(":")
		tts=gTTS(text="you searched for"+str(search[1]+"on google plz wait few minutes while we are loading for you"),lang='en')
		tts.save("a.mp3")
		mixer.music.load("a.mp3")
		mixer.music.play()
		if search[0] == "Google" or search[0] == "Google and Google":
			wb.open_new_tab(google_search+search[1])
			print()
		elif search[0] == "Wiki" :
			try:
				wiki_say = wiki.summary(search[1])
				print(color(BOLD+wiki_say+END+"\n","green"))
			except wiki.exceptions.DisambiguationError:
				print(color(BOLD+"Try to google it because it is very confusing for me"+END,"red"))
		elif search[0] == "Youtube":
			wb.open_new_tab(youtube_search+search[1])
			print("")
		elif search[0] == "Drive":
			wb.open_new_tab(google_drive)
			print("")
		elif search[0] == "Gmail":
			print("")
			wb.open_new_tab(gmail)
		
		
	except KeyboardInterrupt:
		print ("bye")
