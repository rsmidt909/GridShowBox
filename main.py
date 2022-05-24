import os
import json
import time
import random


# name of user
user = "rinzler"

# local variable of schedule home
schedule_home = "/home/" + user + "/GridShowBox/Schedule"

# cached version of localtime in object form on machine
time_object = time.localtime(time.time())
# py object of time with hour, min, and current time. Note: Leading Zero's do not exist. EX. 2:14, 9:3, 16:50,
grid_clock = {
    "hour": time_object.tm_hour,
    "min": time_object.tm_min,
    "current_time": str(time_object.tm_hour) + ":" + str(time_object.tm_min)
}

# length of time currently used by GridStream
grid_length = 0


# Video class params that all videos will be subject to having.
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
    # Below are required
    Title = "",
    Episode = "",
    Season = "",
    Genre = "",
    Commercial = bool

# cached variable of if today is a holiday from list_of_holidays
holiday = False
# Today's date in month/day format. Note: there are no zeros. EX. January = 1, August = 8
today = str(time_object.tm_mon) + "/" + str(time_object.tm_mday)


# cached list of local holidays from /home/rinzler/GridShowBox/TheGrid/Count.txt
list_of_holidays = [
    "3/4",
    "4/5",
    "6/15"
]


# local cache of last video_id used and count
video_id = 0
count = 0

# cached version of the MasterFile in py object form
cached_video_list_py = ()

# list of random numbrs to keep track of possible duplicates.
random_number_list = []

# cached collection of video objects
list_of_videos = []

# cached collection of commercial video objects
list_of_commercial_videos = []

# cached collection of NONcommercial video objects
list_of_non_commercial_videos = []


##########################CALL FUNCTIONS BELOW############################

##########################DEFINE FUNCTIONS BELOW############################
# creates a file names Count.txt and updates the number NEEDS REWORKED
def update_video_count():
    with open('/home/rinzler/GridShowBox/TheGrid/Count.txt' 'w' 'utf-8' ) as file:
        global count
        number_str = file.read()
        number_int = int(number_str)
        new_number_int = number_int + 1
        count = new_number_int
        new_number_str = str(new_number_int)
        file.write(new_number_str)


# makes global variable holiday true or false from list_of_holidays
def is_today_a_holiday():
    for x in list_of_holidays:
        if x == today:
            global holiday
            holiday = True
            break


# check Masterfile exist, if not then make. NEEDS FIXED
def check_masterfile():
    print("MasterFile Check")
        with open('/home/rinzler/TheGridSBox/MasterFile.json' 'w' 'utf-8') as file:


# convert /home/rinzler/GridShowBox/MasterFile.json to an iterable python object and cache
def make_masterfile_py():
    with open('/home/rinzler/GridShowBox/MasterFile.json' 'r' 'utf-8') as file:
        global cached_video_list_py
        video_list_raw = file
        cached_video_list_py = json.load(video_list_raw)


# check if the cached_video_list_py is empty. If so, run make_masterfile
def check_cached_video_py_contents():
    if cached_video_list_py.count == 0:
        make_masterfile_py()



# return one random number from count list with no duplicates
def roll_1_random_number():
    global count
    global random_number_list
    random_number = random.randint(1, count)
    # check for duplicates
    for x in random_number_list:
        if random_number == random_number_list[x]:
            roll_1_random_number
    print(random_number)
    return random_number



# verify video type from list against argument
def check_if_video_commercial(video_object, commercial):
    if video_object.Commercial != type:
        return False



#make list of videos by type Which means commercial property
def add_to_list_of_video_objects_by_type(commercial):
    global list_of_commercial_videos
    global list_of_non_commercial_videos
    # generate one random number
    number = roll_1_random_number
    # make one video object from the ID against the cached_video_list_py
    video = cached_video_list_py[number]
    # Check the video objects type against argument, if not, rerun.
    if not check_if_video_commercial(video, commercial):
        add_to_list_of_video_objects_by_type
    if not commercial:
        list_of_non_commercial_videos.append(video)
    else:
        list_of_commercial_videos.append(video)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(grid_clock)
