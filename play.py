#import vlc
#import pafy

'''
url="https://www.youtube.com/results?search_query=cricket"
video = pafy.new(url)
best = video.getbest()
playurl = best.url
'''
import os
import urllib.request
import urllib.parse
import re

query_string = urllib.parse.urlencode({"search_query" : input()})
html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
url="http://www.youtube.com/watch?v=" + search_results[0]
print(url)
os.system("vlc "+url)
