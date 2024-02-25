#!/usr/bin/python3
import time

while True:
    print("Here is your reminder to breath")
    time.sleep(3)

    for count in range(3):
        print("Breath in...")
        time.sleep(5)
        print("Breath out...")
        time.sleep(5)

        count += 1

    print("Congratulations, you can go on with your work.")
    time.sleep(3)
    print("I will remind you again in 10 minutes")

    time.sleep(600)
