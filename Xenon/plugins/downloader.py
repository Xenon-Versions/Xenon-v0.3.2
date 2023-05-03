import os
from pytube import YouTube
import funcs
import vars_setup

def yt_download(user):
    url = user[6:]
    yt = YouTube(url)
    stream = yt.streams.get_highest_resolution()
    stream.download()
    funcs.printAndSay(f"Downloaded: {yt.title}\n| Check:{os.getcwd()}")
    new_file = vars_setup.newPath(os.getcwd(),f"{yt.title}.mp4")
    os.startfile(new_file)

def music_download(user):
    url = user[9:]
    yt = YouTube(url)
    stream = yt.streams.get_audio_only()
    stream.download()

