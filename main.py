from pytube import YouTube 
from pytube import Playlist
from pytube.cli import on_progress 
import os
import sys
import yt_dlp


def main():
    print("Enter the URL of the video you want to download: ")
    url = input()
    # playlist = Playlist(url)
    download_path = "D:/mtrih/Music"
    # i = 0

    # for video in playlist.videos:
    #     # video_title = video.title if video.title else "default_title" + i
    #     # video.register_on_progress_callback(on_progress)
    #     video.streams.filter(only_audio=True).first().download(output_path=download_path)
    #     i+=1
    # print ("Downloaded all videos in the playlist")

    # video = YouTube(url)
    # download_path = "D:/mtrih/Music"
    # video.streams.filter(only_audio=True).first().download(output_path=download_path)
    # print("Downloaded the video")

################################ switching to yt-dlp ################################

    ydl_opts = {
        'format': 'bestaudio/best',
        'ffmpeg_location': 'C:/ffmpeg-2024-12-16-git-d2096679d5-essentials_build/bin',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': f'{download_path}/%(title)s.%(ext)s',
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        #get playlist title
        playlist_title = ydl.playlist_title(url)
        #create folder with playlist title if it doesn't exist, overwrite if it does
        os.makedirs(f'{download_path}/{playlist_title}', exist_ok=True)
        #change download path to the new folder
        ydl_opts['outtmpl'] = f'{download_path}/{playlist_title}/%(title)s.%(ext)s'

        ydl.download([url])

    print("Downloaded the playlist")



main()

    