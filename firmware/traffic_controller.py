# Kinshasa Smart Traffic Light - Firmware
# Grande voie - 100% solar + 4G
# Author: Blackdolph12

import time
from datetime import datetime

class KinshasaTrafficLight:
    def __init__(self):
        print("Kinshasa Smart Light Started")
    
    def green(self):
        print(f"[{datetime.now().strftime('%H:%M:%S')}] VERT - KENDE!")
    
    def yellow(self):
        print(f"[{datetime.now().strftime('%H:%M:%S')}] JAUNE - KEBELA!")
    
    def red(self):
        print(f"[{datetime.now().strftime('%H:%M:%S')}] ROUGE - BOTELEMA!")

if __name__ == "__main__":
    light = KinshasaTrafficLight()
    while True:
        light.green()
        time.sleep(90)
        light.yellow()
        time.sleep(5)
        light.red()
        time.sleep(120)