from pytube import YouTube 
from pytube import Playlist
from pytube.cli import on_progress 
import os
import sys
import yt_dlp
import re

def sanitize_filename(filename):
    return re.sub(r'[<>:"/\\|?*]', '', filename)


def main():
    print("Enter the URL of the playlist you want to download: ")
    url = input()
    print("Enter the path to where you want to save the music : ")
    download_path = input()
    ydl_opts = {
        'format': 'bestaudio/best',
        'ffmpeg_location': 'C:/ffmpeg-2024-12-16-git-d2096679d5-essentials_build/bin',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'outtmpl': {'default': os.path.join(download_path, '%(title)s.%(ext)s')},
    }

    if "playlist" in url:
        
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            #get playlist title
            playlist_title = ydl.extract_info(url, download=False)['title']
            playlist_title = sanitize_filename(playlist_title)
            #create folder with playlist title if it doesn't exist, overwrite if it does
            os.makedirs(f'{download_path}/{playlist_title}', exist_ok=True)
            #change download path to the new folder
            playlist_folder = os.path.join(download_path, playlist_title)
            ydl_opts['outtmpl'] = {'default': os.path.join(playlist_folder, '%(title)s.%(ext)s')}
            ydl.download([url])

    else:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

    print("Finished Download and Conversion - Saved in:", download_path)

main()

    