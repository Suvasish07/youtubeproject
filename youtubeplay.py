# from time import sleep;

# song_name = input("enter a song name ")


# def start_song(song_name):
#     words = song_name.split()

#     url = "http://www.youtube.com/results?search_query="

#     for word in words:
#         url += word + "+"

#     time.sleep(1)   #Sleeps for a second
#     webbrowser.open_new(url[:-1]) 


# start_song(song_name)


import webbrowser

webbrowser.open("https://www.youtube.com")
