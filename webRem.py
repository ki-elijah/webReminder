import time
import webbrowser

setAlarm = input("Set the website Alarm as H:M:S(all in 2 digits form): ")
url = input("Enter the website url you eant to open: ")
actualTime = time.strftime("%I:%M:%S")

while (actualTime != setAlarm):
    print("The time is " + actualTime)
    actualTime = time.strftime("%I:%M:%S")
    time.sleep(1)
if(actualTime == setAlarm):
    print("You should see your webpage now")
    webbrowser.open(url)