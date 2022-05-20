import os
import json
import time
import random


#name of user
user = "rinzler"

#local variable of schedule home
schedule_home = "/home/" + user +"/GridShowBox/Schedule"


#cached array of videos to play
list_of_videos = []

#cached version of localtime in object form on machine
time_object = time.localtime(time.time())
#py object of time with hour, min, and current time. Note: Leading Zero's do not exist. EX. 2:14, 9:3, 16:50,
grid_clock = {
    "hour": time_object.tm_hour,
    "min": time_object.tm_min,
    "current_time": str(time_object.tm_hour) + ":" + str(time_object.tm_min)
}

#length of time currently used by GridStream
grid_length = 0

#Video class params that all videos will be subject to having.
class Video:
    Running = False,
    Length = "",
    Type = "",
    PreTag = "",
    PostTag = "",
    Tag = "",
    Holiday = "",
    PrimeID = 0,
    Path = "",
    #Below are required
    Title = "",
    Episode = "",
    Season = "",
    Genre = ""

#cached variable of if today is a holiday from list_of_holidays
holiday = False

#Today's date in month/day format. Note: there are no zeros. EX. January = 1, August = 8
today = str(time_object.tm_mon) + "/" + str(time_object.tm_mday)


#cached list of local holidays from /home/rinzler/GridShowBox/TheGrid/Count.txt
list_of_holidays = [
    "3/4",
    "4/5",
    "6/15"
]


#local cache of last video_id used and count
video_id = 0
count = 0

#cached version of the MasterFile in py object form
cached_video_list_py = []

#array of random numbers to choose for non-commercial stream
random_set_list = []



#**********************************************************************************

def update_masterfile(incomingData):
    with open('/home/rinzler/GridShowBox/TheGrid/MasterFile.json' 'r') as file:



#creates a file names Count.txt and updates the number NEEDS REWORKED
def update_video_count():
    with open('/home/rinzler/GridShowBox/TheGrid/Count.txt' 'w' ) as file:
        number_str = file.read()
        number_int = int(number_str)
        new_number_int = number_int + 1
        count = new_number_int
        new_number_str = str(new_number_int)
        file.write(new_number_str)


#makes global variable holiday true or false from list_of_holidays
def is_today_a_holiday():
    for x in list_of_holidays:
        if x == today:
            holiday = True
        else:
            holiday = False



#convert /home/rinzler/GridShowBox/MasterFile.json to an iterable python object and cache
def make_masterfile_py():
    with open('/home/rinzler/GridShowBox/MasterFile.json' 'r' ) as file:
        video_list_raw = json.dumps(file)
        cached_video_list_py = json.load(video_list_raw)

#check if the cached_video_list_py is empty. If so, run make_masterfile
def check_cached_video_py_contents():
    if cached_video_list_py.count == 0:
        make_masterfile_py()


#return video object from ID
def grab_video(primid):
    check_cached_video_py_contents()
    video_object = Video()
        for x in cached_video_list_py:
            video_object = x
            if x.PrimeID == primid:

#call random number 50 times for random_set_list




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(grid_clock)
