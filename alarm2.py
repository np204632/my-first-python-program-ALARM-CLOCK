import datetime
from playsound import playsound

alarm_hour = int(input('enter the alarm hour:'))
alarm_minute = int(input('enter the alarm minute:'))
alarm_seconds = int(input('enter the alarm second:'))
alarm_timing = input('enter the alarm timing in AM/PM:')



if alarm_timing == 'PM':
    alarm_hour += 12
    while True:
        if alarm_hour == datetime.datetime.now().hour and alarm_minute == datetime.datetime.now().minute and alarm_seconds == datetime.datetime.now().second:
            print('playing ....')
            playsound("C:\\Users\\nishant\\Desktop\\AudioCutter_yt5s.com - Hall of Fame __ Feat script __ N.C.S (128 kbps).mp3")
            break

elif alarm_timing == 'AM':
    while True:
        if alarm_hour == datetime.datetime.now().hour and alarm_minute == datetime.datetime.now().minute and alarm_seconds == datetime.datetime.now().second:
            print('playing ....')
            playsound("C:\\Users\\nishant\\Desktop\\AudioCutter_yt5s.com - Hall of Fame __ Feat script __ N.C.S (128 kbps).mp3")
            break
