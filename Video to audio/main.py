import moviepy.editor
import os

video = moviepy.editor.VideoFileClip("short.mp4")
audio = video.audio

for i in range(1):
    if os.path.exists("output.mp3"):
        print("EXISTS")
        break
    else:
        audio.write_audiofile("output.mp3")