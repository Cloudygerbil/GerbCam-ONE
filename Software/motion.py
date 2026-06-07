import cv2
import time
import os
   
vid = cv2.VideoCapture(0)

width = int(vid.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(vid.get(cv2.CAP_PROP_FRAME_HEIGHT))

x = None
record = False
output = None
record_start = None

while True:
    check, new = vid.read()

    raw = new

    small = cv2.resize(new, (128, 96))

    ismovement = 0
   
    grayscale = cv2.cvtColor(small, cv2.COLOR_BGR2GRAY)
    
    blur = cv2.GaussianBlur(grayscale, (15, 15), 0)
    
    if x is None:
       x = blur.copy()
       continue

    framediff = cv2.absdiff(x, blur)

    threshold = cv2.threshold(framediff, 20, 255, cv2.THRESH_BINARY)[1]
    dialate = cv2.dilate(threshold, None, iterations = 1)

    contours = cv2.findContours(dialate, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    motion_pix = cv2.countNonZero(dialate)

    print(motion_pix)

    if motion_pix >= 75 and not record:
       print("Recording online")
       fourcc = cv2.VideoWriter_fourcc(*"H264")
       output = cv2.VideoWriter("newvid.mp4", fourcc, 20.0, (width, height))
       record = True
       record_start = time.time()
    if record:
       output.write(raw)

       if time.time() - record_start >= 15.0:
          print("Recording offline")
          output.release()
          os.remove("video4.mp4")
          os.rename("video3.mp4", "video4.mp4")
          os.rename("video2.mp4", "video3.mp4")
          os.rename("video1.mp4", "video2.mp4")
          os.rename("newvid.mp4", "video1.mp4")
          output = None
          record = False
      
    cv2.imshow("Video", dialate)
    cv2.imshow("RAW", raw)

    x = blur.copy()
    
    if cv2.waitKey(1) & 0xFF == ord("q"):
       break

vid.release()
cv2.destroyAllWindows()