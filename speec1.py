import speech_recognition as sr
from os import system
import apiai
import wikipedia as wiki
import webbrowser as wb
from gtts import gTTS
from pygame import mixer
mixer.init()


google_search = "https://www.google.com/search?q="
youtube_search = "https://www.youtube.com/results?search_query="
google_drive = "https://drive.google.com"
gmail = "https://mail.google.com"	
wikipedia_search = "https://en.wikipedia.org/wiki/" 

r = sr.Recognizer()
with sr.Microphone() as source:
    system('clear')
    print("Say something!")
    r.adjust_for_ambient_noise(source, duration=1)
    audio = r.listen(source)

'''# Speech recognition using Google Speech Recognition
try:
    # for testing purposes, we're just using the default API key
    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
    # instead of `r.recognize_google(audio)`
    print("You said: " + r.recognize_google(audio))
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError as e:
    print("Could not request results from Google Speech Recognition service; {0}".format(e))'''
print(r.recognize_google(audio))
query = r.recognize_google(audio)
print(query)
words = query.split(" ")
print(list(words))
a=list(words)
#print(a[0])



for i in range(len(a)):
	if a[i] == "Google"  or a[i] == "Google and Google":
		wb.open_new_tab(google_search+a[1])
	#	print("")
	elif a[i] =="YouTube" :
		wb.open_new_tab(youtube_search+a[1])
	#	print("")
	elif a[i] == "Wikipedia" :
		wb.open_new_tab(wikipedia_search+a[i])
		wiki_input = wiki.summary(a[i])
		print(wiki_input)
	else:
		print("not valid input ")
 
