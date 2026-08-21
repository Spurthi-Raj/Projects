from alarm import AlarmManager
from utils import validate_time,is_future_time
import time

m = AlarmManager()

while True:
    print("\n 1.Add 2.List 3.Delete 4.Run 5.Exit")
    c = input("choice: ")
    if c == "1":
        t = input(" Enter Alarm Time (HH:MM:SS): ").strip()
        if not validate_time(t):
            print("\n Invalid time format.")
            continue
            
        if not is_future_time(t):
            print("\n" + "=" * 45)
            print("     INVALID ALARM TIME")
            print("=" * 45)
            print(f"Entered Time : {t}")
            print("Alarm time must be later than current time.")
            print("=" * 45)
            continue
        m.add(t)
        print(f"\n Alarm added succesfully for {t}")

    elif c=="2":
        [print(i,a.time) for i,a in enumerate(m.alarms)]
    elif c=="3":
        i = int(input("Index: "))
        m.remove(i)
    elif c=="4":
        print("Waiting...")
        while True:
            for a in m.alarms:
                if a.due():
                    print("\n" + "=" *45)
                    print("    ALARM")
                    print("=" * 45)
                    print(f"Alarm Time :{a.time}")
                    print("Wake up! Your alarm is ringing.")
                    print("=" * 45)

                    for _ in range(3):
                        print("\a", end="", flush=True)
                        time.sleep(1)

                    a.active = False
                time.sleep(1)
    
    elif c=="5":
        break






