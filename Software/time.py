import os

directory = os.path.dirname(os.path.abspath(__file__))

def path(name):
    return os.path.join(directory, name)

from datetime import datetime

def modify(file):
    timestamp = os.path.getmtime(file)
    return datetime.fromtimestamp(timestamp)

mod_date = modify(path("video1.mp4"))

with open(path("time.txt"), "w") as file:
    file.write(mod_date.strftime("%d/%m/%Y, %H:%M:%S"))
