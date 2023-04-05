from pytube import YouTube
import os
import pytube

video_dir = 'videos'
os.makedirs(video_dir,exist_ok=True)

#working directory
current_dir = os.getcwd()
video_path = os.path.join(current_dir,video_dir)

# ask user for the YouTube video URL
video_url = "https://www.youtube.com/watch?v=Skpu5HaVkOc"

# create a YouTube object with the video URL
yt = YouTube(video_url)

# get the highest resolution stream
stream = yt.streams.get_highest_resolution()

#title of the video
title = yt.title

# download the video
stream.download(output_path=video_path)

