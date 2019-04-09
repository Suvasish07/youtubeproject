import urllib.request
import urllib.parse
import re
import webbrowser

query_string = urllib.parse.urlencode({"search_query" : input("enter a song name to play in youtube : ")})
html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
webbrowser.open("http://www.youtube.com/watch?v=" + search_results[0])

#youtube app