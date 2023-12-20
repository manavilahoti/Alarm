import time
import playsound

CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"
def alarm(second):
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
        
        print(f"{CLEAR_AND_RETURN}Alarm will sound in {hours_left:02d}:{minutes_left:02d}:{second_left:02d}")
    playsound.playsound("alarm_sound.mp3")
   

user_input = (input("Enter the time to wait (HH:MM:SS)\n "))
hours = int(user_input[0:2])
minutes = int(user_input[3:5])
seconds = int(user_input[6:])
second = (hours*3600) + (minutes*60) + (seconds)

alarm(second)



