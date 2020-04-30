# importing moviepy module to get editor
import moviepy.editor as ed

# Opening video
video = ed.VideoFileClip("see-you-again.mp4")

# storing audio from video into a variable
audio = video.audio

# writing audio to the current working directory
audio.write_audiofile("see-you-again.mp3")