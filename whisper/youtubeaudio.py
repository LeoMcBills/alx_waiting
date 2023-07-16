import pytube

video = pytube.YouTube("https://www.youtube.com/watch?v=9bZkp7q19f0")

# which youtube link did we choose?
print("Title: ", video.title)

data = pytube.YouTube(video)

audio = video.streams.get_audio_only()
audio.download()

