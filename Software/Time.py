import ffmpeg
from datetime import datetime

def info(vid_path):
    probe = ffmpeg.probe(vid_path)
    format = probe["format"]


