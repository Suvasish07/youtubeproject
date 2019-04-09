import urllib.request
import urllib.parse
import re
import webbrowser
import pytube 

query_string = urllib.parse.urlencode({"search_query" : input("enter a song to download from youtube: ")})
html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())

SAVE_PATH = "/home/jeevan/Videos"

link = "https://www.youtube.com/watch?v=hF8MjhyN2Yg" 
yt = pytube.YouTube(link)
stream = yt.streams.first()
stream.download(SAVE_PATH)

print("your song has been downloaded find it in :"+ SAVE_PATH)