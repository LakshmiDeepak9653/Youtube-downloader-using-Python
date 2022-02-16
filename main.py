"""YouTube videos downloader using Python"""

import os

from pytube import YouTube
from pytube import Playlist
count=1
def In():
    a=input("Enter your Corresponding option👇:-")
    return a
def videoDownload(link):
    link=link
    yt = YouTube(x)
    yt.bypass_age_gate()
    yt.check_availability()
    yt.streams.get_lowest_resolution().download()
    print("Downloaded 👍!!")
def convert(link):
    link=link
    yt=YouTube(link)
    yt.bypass_age_gate()
    yt.check_availability()
    yt.streams.get_audio_only().download()
    print("Downloaded 👍!!")
    print("Kindly rename the extension from .mp4 to mp3.")
def playlist_download(link):
    link = link
    p = Playlist(link)
    title = p.title
    os.makedirs(title)
    for url in p.video_urls:
        try:
            yt = YouTube(url)
        except VideoUnavailable:
            print(f"Video {url} is unavilable")
        else:
            yt.bypass_age_gate()
            yt.check_availability()
            yt.streams.get_lowest_resolution().download(output_path=title)
            print("Downloaded 👍!!")






print("\033[1;32m Thanks for using me 😃!!\n\n")
def options():
    print("\033[1;34m Select an Option for Downloading your videos\n a. YouTube video with Url\n b. A YouTube Playlist videos with Url\n c. Convert YouTube video to mp3 with Url\033[1;0m")
options()

A = In()
while (count > 0):
    if A == 'a':
        x=input("Enter the YouTube video link🔗 here:-")
        videoDownload(x)
        print("\033[1;36m Do you want to continue to download more [y/n]:-\033[1;0m")
        B=input("")
        if B=="y":
            options()
            A = In()
        elif B=='n':
            print("")
            count =0
        else:
            print("Press correct option")
    elif A == 'b':
        x = input("Enter the PlayList link🔗 here:-")
        playlist_download(x)
        print("\033[1;36m Do you want to continue to download more [y/n]:-\033[1;0m")
        B = input("")
        if B == "y":
            count = 1
            options()
            A = In()
        elif B == 'n':
            print("")
            count = 0
        else:
            print("Press correct option")
    elif A == 'c':
        x = input("Enter the Youtube video link to convert🔗 here:-")
        convert(x)
        print("\033[1;36m Do you want to continue to download more [y/n]:-\033[1;0m")
        B = input("")
        if B == "y":
            options()
            A = In()
        elif B == 'n':
            print("")
            count = 0
        else:
            print("Press Enter correct option")
    else:
        print("Press correct option")
        A = In()



