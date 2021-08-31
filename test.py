import sda
import scipy.io.wavfile as wav
from PIL import Image

va = sda.VideoAnimator()# Instantiate the animator
fs, audio_clip = wav.read("example/test.wav")
still_frame = Image.open("example/image.bmp")
vid, aud = va(still_frame, audio_clip, fs=fs)
va.save_video(vid, aud, "generated.mp4")
