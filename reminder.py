import time
from plyer import notification
import datetime
from playsound import playsound


def morning_notification():
     notification.notify (
            title = "**Please Take Your Medicine!!**", 
            message = "It's time for your Antibiotic Medicine",
            app_icon = "C:/Users/User/Desktop/reminder project/medicine.ico",
            timeout=10
            
        )

def noon_notification():
     notification.notify (
            title = "**Please Take Your Medicine!!**", 
            message = "It's time for your Gastric Medicine",
            app_icon = "C:/Users/User/Desktop/reminder project/medicine.ico",
            timeout=10
            
        )

def night_notification():
     notification.notify (
            title = "**Please Take Your Medicine!!**", 
            message = "It's time for your Pain killer Medicine",
            app_icon = "C:/Users/User/Desktop/reminder project/medicine.ico",
            timeout=10
            
        )
  

if __name__ == "__main__":
    while True:
        alarmHour=datetime.datetime.now().hour
        alarmMin= datetime.datetime.now().minute
        if alarmHour == 7 and alarmMin == 30: 
            morning_notification()
            playsound("C:/Users/User/Desktop/reminder project/medialarm.mp3")
            time.sleep(3600*8)
        if alarmHour == 17 and alarmMin == 22: 
            noon_notification()
            playsound("C:/Users/User/Desktop/reminder project/medialarm.mp3")
            time.sleep(3600*8)
        if alarmHour == 22 and alarmMin == 30: 
            night_notification()
            playsound("C:/Users/User/Desktop/reminder project/medialarm.mp3")
            time.sleep(3600*8)


        time.sleep(10)