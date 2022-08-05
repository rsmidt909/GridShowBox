import os
import json
import time
import random
import player

# name of user
user = "rinzler"

# local variable of schedule home
schedule_home = "/home/" + user + "/GridShowBox/Schedule"

# cached version of localtime in object form on machine
time_object = time.localtime(time.time())

'''
# py object of time with hour, min, and current time. Note: Leading Zero's do not exist. EX. 2:14, 9:3, 16:50,
grid_clock = {
    "hour": int(time_object.tm_hour),
    "min": int(time_object.tm_min),
    "current_time": str(time_object.tm_hour) + ":" + str(time_object.tm_min)
}
'''
grid_hour = int(time_object.tm_hour)

grid_min = int(time_object.tm_min)

grid_current_time = str(time_object.tm_hour) + ":" + str(time_object.tm_min)

# length of time currently used by GridStream
grid_length = 0


# Video class params that all videos will be subject to having.
class Video:
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

# list of random numbwrs to keep track of possible duplicates.
random_number_list = []

# current non-commercial video
current_noncommercial_video = Video()

# next non-commercial video
next_noncommercial_video = Video()

# current commercial video
current_commercial_video = Video()

# next commercial video
next_commercial_video = Video()

# is a non-commercial video running
video_playing = False

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
    with open('/home/rinzler/TheGridShowBox/MasterFile.json' 'w' 'utf-8') as file:
        print("MasterFile Check")


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
            roll_1_random_number()
    print(random_number)
    return random_number


# verify video type from list against argument
def check_video_type(video_object, commercial_bool):
    if video_object.Commercial != commercial_bool:
        return False


# make list of videos by commercial bool
def add_to_list_of_video_objects_by_type(commercial_bool):
    global next_noncommercial_video
    global next_commercial_video
    # generate one random number
    number = roll_1_random_number()
    # make one video object from the ID against the cached_video_list_py
    video = cached_video_list_py[number]
    # Check the video objects type against argument, if not, rerun.
    if not check_video_type(video, commercial_bool):
        add_to_list_of_video_objects_by_type(commercial_bool)
    if not commercial_bool:
        # need to change this to holding the original number and recycling the old
        next_noncommercial_video = video
    else:
        # need to change this to holding the original number and recycling the old
        next_commercial_video = video


# need to make method for moving next video to current video and then replacing next video value with new random video
def move_and_replace(commercial_bool):
    global current_commercial_video
    global current_noncommercial_video
    if commercial_bool:
        current_commercial_video = next_commercial_video
        add_to_list_of_video_objects_by_type(commercial_bool)
    else:
        current_noncommercial_video = next_noncommercial_video
        add_to_list_of_video_objects_by_type(commercial_bool)


# Move next video to current video Play Non-commercial video in current video
def play_noncommercial_video():
    global video_playing
    video_playing = True

# Move next video to current video Play Commercial video in current vide
def play_commercial_video():



# Pause the target video
def pause_video():



# unpause the target video
def unpause_video():



# play commercial until the local time minutes are 00 or 30
def commercial_buffer():
    while grid_min != 00 or 30:
        play_commercial_video()


# pause, run commercial_buffer, and then resume video
def commercial_watch():
    pause_video()
    commercial_buffer()
    unpause_video()
# watch for time and if video is playing
def video_watch():
    '''
    while video_playing == True
    wait ... until video_playing == false
    or
    min == 25||30

    if min == 25 ||55
    commercial_watch()

    if video_play == False
    commercial_buffer()
    '''



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    video_watch()
