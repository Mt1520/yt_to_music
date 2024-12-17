# yt-to-music

`yt-to-music` is a Python-based tool that allows users to download audio from YouTube videos and playlists and save them in a specified directory. The tool uses `yt-dlp`, a powerful and flexible tool to download content from YouTube, and supports downloading both individual videos and whole playlists.

## Features

- Download audio from YouTube videos.
- Download entire playlists in audio format.
- Automatically organize files into folders named after the playlist.
- Supports customization of download location and output filenames.

## Requirements

- Python 3.7 or later
- `yt-dlp` (a fork of `youtube-dl` that supports more sites and features)
- `ffmpeg` (for post-processing audio)
  
### Install the dependencies

1. **Install Python 3.x**:
   Ensure that Python 3.7 or higher is installed on your system. You can download it from [here](https://www.python.org/downloads/).

2. **Install `yt-dlp`**:
   You can install `yt-dlp` using `pip`:
   ```bash
   pip install yt-dlp
   
Install ffmpeg: yt-dlp requires ffmpeg for post-processing audio and video files. You can download and install it from FFmpeg's official site.

After installing ffmpeg, make sure it's added to your system's PATH so that yt-dlp can access it.

Setup
Clone or download this repository to your local machine:
```bash
git clone <repository-url>
cd yt-to-music
```

Make sure to install all the necessary Python dependencies if they are listed in requirements.txt.

Usage
1. Download a Single Video
To download the audio from a single YouTube video, simply pass the video URL to the script:

```bash
python main.py <video_url>
```
2. Download an Entire Playlist
To download all audio files from a YouTube playlist, pass the playlist URL:

```bash
python main.py <playlist_url>
The script will:
```
Create a folder with the name of the playlist (if not already created).
Download all video files from the playlist in audio format into that folder.
3. Customize Download Location and Filenames
You can specify the output directory and filename format in the script. By default, the script downloads files into the D:/Downloads folder, but you can modify this in the main.py script by setting the download_path variable.

The output filenames will follow this format: title_of_video.mp3.

Example
Here's an example of how the script can be used:

```bash
python main.py https://www.youtube.com/playlist?list=PL12345ABCDEF
```
This will download all videos in the playlist and store them under D:/Downloads/PL12345ABCDEF/, where each video file will be named according to its title.

Output
The downloaded files will be saved in the format:
```markdown
D:/Downloads/PL12345ABCDEF/
    - Song Title 1.mp3
    - Song Title 2.mp3
    - Song Title 3.mp3
    - ...
```
Troubleshooting
Issue: ffmpeg and ffprobe not found

Solution: Make sure ffmpeg is installed and added to your PATH.
Issue: Error: Postprocessing

Solution: Ensure yt-dlp is installed correctly and that the necessary post-processing tools are available.
Issue: 403 Forbidden

Solution: If you're getting a 403 Forbidden error, make sure the video is publicly available, or if it's age-restricted, you might need to handle that manually.
