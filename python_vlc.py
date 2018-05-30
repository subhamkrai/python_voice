#!/usr/bin/python3

import pafy
import vlc
#import os
import urllib.request
import urllib.parse
import re

query_string = urllib.parse.urlencode({"search_query" : input()})
html_content = urllib.request.urlopen("https://www.youtube.com/results?" + query_string)
search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
url="https://www.youtube.com/watch?v=" + search_results[0]
print(url)


#Instance = vlc.Instance()
#player = Instance.media_player_new()
#Media = Instance.media_new(url)
#Media.get_mrl()
#player.set_media(Media)
#player.play()








#os.system("vlc "+url)


video = pafy.new(url)
print(video)
best = video.getbest()
print(best)
playurl = best.url
print(playurl)

Instance = vlc.Instance()
print(Instance)
player = Instance.media_player_new()
print(player)
Media = Instance.media_new(playurl)
print(Media)
Media.get_mrl()
player.set_media(Media)
player.play()


