import os
import json
import time
import random

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
encoding="locale"
user = "rinzler"
scheduleHome = "/home/" + user +"/GridShowBox/Schedule"
schedule = {}
listOfVideos = {}
timeObject = time.localtime(time.time())
gridClock = {
    "Hour": timeObject.tm_hour,
    "Min": timeObject.tm_min,
    "CurrentTime": str(timeObject.tm_hour) + ":" + str(timeObject.tm_min)
}
gridLength = 0
class Video:
    Running = False,
    Length = "",
    Type = "",
    PreTag = "",
    PostTag = "",
    Tag = "",
    Holiday = "",
    ID = 0,
    Path = "",
    #Below are required
    Title = "",
    Episode = "",
    Season = "",
    Genre = ""

holiday = False
listOfRecentVideoIDs = []
count = 0
today = str(timeObject.tm_mon) + "/" + str(timeObject.tm_mday)
listOfHolidays = [
    "3/4",
    "4/5",
    "6/15"
]

videoID = 0

def UpdateMasterFile(incomingData):
    with open('/home/rinzler/GridShowBox/TheGrid/MasterFile.json' 'r') as file:
        parsedData = json.load(file)
        parsedData.


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


def grabVideo():
    videoID = random.randint(0, count)
    os.gr


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
