import os
import cv2
import time
import subprocess

directory = os.path.dirname(os.path.abspath(__file__))

def path(name):
    return os.path.join(directory, name)

vid = cv2.VideoCapture(0)
vid.set(cv2.CAP_PROP_FPS, 10)

width = 480
height = 360

x = None
record = False
output = None
record_start = 0.0
frame_num = 0

while True:
    ret, new = vid.read()

    raw = cv2.resize(new, (480, 360))

    small = cv2.resize(raw, (32, 24))
    ismovement = 0
    grayscale = cv2.cvtColor(small, cv2.COLOR_BGR2GRAY)

    blur = cv2.GaussianBlur(grayscale, (3, 3), 0)

    if x is None:
       x = blur.copy()
       continue

    if frame_num % 4 == 0:

       framediff = cv2.absdiff(x, blur)
       threshold = cv2.threshold(framediff, 20, 255, cv2.THRESH_BINARY)[1]
       dialate = cv2.dilate(threshold, None, iterations = 1)
       motion_pix = cv2.countNonZero(dialate)

       if motion_pix >= 10 and not record:
          fourcc = cv2.VideoWriter_fourcc(*"avc1")
          output = cv2.VideoWriter(path("newvid.mp4"), fourcc, 10.0, (width, height))
          record = True
          record_start = int(time.time())

    if record:
          output.write(raw)

    if time.time() - record_start >= 10.5 and record:
       output.release()
       output = None
       record = False
       frame_num = 0

       os.remove(path("video4.mp4"))
       os.rename(path("video3.mp4"), path("video4.mp4"))
       os.rename(path("video2.mp4"), path("video3.mp4"))
       os.rename(path("video1.mp4"), path("video2.mp4"))
       os.rename(path("newvid.mp4"), path("video1.mp4"))
       subprocess.run(["python3", path("time.py")])

    frame_num = frame_num + 1
    x = blur.copy()

vid.release()
