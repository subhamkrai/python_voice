import pafy
import vlc
import urllib.request
import urllib.parse
import re

query_string = urllib.parse.urlencode({"search_query" : input()})
html_content = urllib.request.urlopen("https://www.youtube.com/results?" + query_string)
search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
url="https://www.youtube.com/watch?v=" + search_results[0]
print(url)
video = pafy.new(url)
best = video.getbest()
playurl = best.url

Instance = vlc.Instance()
player = Instance.media_player_new()
Media = Instance.media_new(playurl)
Media.get_mrl()
player.set_media(Media)
player.play()
