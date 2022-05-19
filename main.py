import os
import json
import time
import random

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
encoding="locale"
user = "rinzler"
schedule_home = "/home/" + user +"/GridShowBox/Schedule"
schedule = {}
list_of_videos = {}
time_object = time.localtime(time.time())
grid_clock = {
    "hour": time_object.tm_hour,
    "min": time_object.tm_min,
    "current_time": str(time_object.tm_hour) + ":" + str(time_object.tm_min)
}
grid_length = 0
class Video:
    Running = False,
    Length = "",
    Type = "",
    PreTag = "",
    PostTag = "",
    Tag = "",
    Holiday = "",
    PrimID = 0,
    Path = "",
    #Below are required
    Title = "",
    Episode = "",
    Season = "",
    Genre = ""

holiday = False
list_of_recentVideoIDs = []
count = 0
today = str(time_object.tm_mon) + "/" + str(time_object.tm_mday)
listOfHolidays = [
    "3/4",
    "4/5",
    "6/15"
]

videoID = 0

cached_video_list_py = []

def UpdateMasterFile(incomingData):
    with open('/home/rinzler/GridShowBox/TheGrid/MasterFile.json' 'r') as file:



#creates a file names Count.txt and updates the number
def UpdateVideoCount():
    with open('/home/rinzler/GridShowBox/TheGrid/Count.txt' 'w' ) as file:
        numberStr = file.read()
        numberInt = int(numberStr)
        newNumberInt = numberInt + 1
        count = newNumberInt
        newNumberStr = str(newNumberInt)
        file.write(newNumberStr)

#plays the loaded video in the stream
#def playVideoStream():



def isTodayAHoliday():
    for x in listOfHolidays:
        if x == today:
            holiday = True
        else:
            holiday = False



#convert /home/rinzler/GridShowBox/MasterFile.json to an interable python pbject
def make_masterfile_py():
    with open('/home/rinzler/GridShowBox/MasterFile.json' 'r' ) as file:
        video_list_raw = json.dumps(file)
        cached_video_list_py = json.load(video_list_raw)

#check if the cached_video_list_py is empty. If so, run make_masterfile
def check_cached_video_py_contents():
    if cached_video_list_py.count == 0:
        make_masterfile_py()


#return video object from ID
def grabVideo(primid):
    check_cached_video_py_contents()
    video_object = Video()
        for x in cached_video_list_py:
            video_object = x
            if x.PrimeID == primid:
                

# create the schedule
def createSchedule():
    for x in
    listOfVideos.apend()
    schedule = {
        "Monday": listOfEpisodes
    }

#check if the schedule exists
#def checkSchedule():


#parses schedule and returns the current video and next video data
def parseSchedule():
    currentVideo
    nextVideo




# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(gridClock)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
