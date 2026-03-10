import time 
medicine_time = "20:00"
while True:
    current_time = time.strftime("%H:%M")
    if current_time == medicine_time:
        print("Reminder: Take your medicine!")

        time.sleep(60)
    