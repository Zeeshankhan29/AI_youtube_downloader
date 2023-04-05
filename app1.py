from pytube import YouTube
import pytube
import os

playlist = pytube.Playlist('https://www.youtube.com/watch?v=S_F_c9e2bz4&list=PLZoTAELRMXVPS-dOaVbAux22vzqdgoGhG')

#playlist directory
playlist_dir = 'playlist'
os.makedirs(playlist_dir,exist_ok=True)

#working directory
current_dir = os.getcwd()
video_path = os.path.join(current_dir,playlist_dir)

for video in playlist.video_urls:

    # ask user for the YouTube video URL
    video_url = video

    # create a YouTube object with the video URL
    yt = YouTube(video_url)

    # get the highest resolution stream
    stream = yt.streams.get_highest_resolution()

    #title of the video
    title = yt.title

    # download the video
    stream.download(output_path=video_path)
