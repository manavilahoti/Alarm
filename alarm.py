import time
import playsound
import datetime

CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"
option = input("Would you like to set an alarm or timer ")
def timer(second):
    time_elapsed = 0

    while(time_elapsed<second):
        time.sleep(1)
        time_elapsed +=1
        print(CLEAR)
        time_left = second - time_elapsed
        hours_left = time_left // 3600
        time_left = time_left % 3600
        minutes_left = time_left // 60
        second_left = time_left % 60
        
        print(f"{CLEAR_AND_RETURN}Timer in ring in {hours_left:02d}:{minutes_left:02d}:{second_left:02d}")
    playsound.playsound("alarm_sound.mp3")


def alarm(alarm_time):
    while True:
        now = datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S")
        alarm_ring_time = datetime.datetime.strptime(alarm_time, "%m/%d/%Y, %H:%M:%S")

        current_time = datetime.datetime.strptime(now, "%m/%d/%Y, %H:%M:%S")
        remaining_time = alarm_ring_time - current_time

        print(CLEAR)
        print(f"{CLEAR_AND_RETURN}Now: {current_time}, Alarm Time: {alarm_time}, Remaining Time: {remaining_time}")

        current_time = current_time.replace(microsecond=0)
        alarm_ring_time = alarm_ring_time.replace(microsecond=0)

        if now == alarm_time:
            time.sleep(1)
            playsound.playsound("alarm_sound.mp3")
            break

        time.sleep(1)

   
if(option.lower() == "timer"):
    user_input = (input("Enter the time to wait ( HH:MM:SS)\n "))
    hours = int(user_input[0:2])
    minutes = int(user_input[3:5])
    seconds = int(user_input[6:])
    second = (hours*3600) + (minutes*60) + (seconds)

    timer(second)

elif(option.lower() == "alarm"):

    alarm_time = input("Enter the time for the alarm to be set at (mm/dd/yyyy, HH:MM:SS) ")
    alarm(alarm_time)
