from pytube import YouTube 
from pytube import Playlist
from pytube.cli import on_progress 
import os
import sys

def main():
    print("Enter the URL of the video you want to download: ")
    url = input()
    # playlist = Playlist(url)
    # download_path = "D:/mtrih/Music"
    # i = 0

    # for video in playlist.videos:
    #     # video_title = video.title if video.title else "default_title" + i
    #     # video.register_on_progress_callback(on_progress)
    #     video.streams.filter(only_audio=True).first().download(output_path=download_path)
    #     i+=1
    # print ("Downloaded all videos in the playlist")

    video = YouTube(url)
    download_path = "D:/mtrih/Music"
    video.streams.filter(only_audio=True).first().download(output_path=download_path)
    print("Downloaded the video")


main()

    