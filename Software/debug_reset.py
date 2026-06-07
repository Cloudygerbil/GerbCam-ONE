import os
import shutil

os.remove("video1.mp4")
os.remove("video2.mp4")
os.remove("video3.mp4")
os.remove("video4.mp4")

shutil.copy2("vidbackup.mp4", "video1.mp4")
shutil.copy2("vidbackup.mp4", "video2.mp4")
shutil.copy2("vidbackup.mp4", "video3.mp4")
shutil.copy2("vidbackup.mp4", "video4.mp4")