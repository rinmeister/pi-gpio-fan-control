#!/usr/bin/env python3

import subprocess
import time
import RPi.GPIO as GPIO

# zet de pinout op BOARD en adresseer pin11 (GPIO17)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.OUT)

# set de drempelwaarden
ondergrens = 59
bovengrens = 61

def meetTemperatuur():
    # Meet de temperatuur van de CPU:
    output = subprocess.run(['cat', '/sys/class/thermal/thermal_zone0/temp'], stdout=subprocess.PIPE)
    # CompletedProcess(args=[   'cat', 
    #                            '/sys/class/thermal/thermal_zone0/temp'], 
    #                            returncode=0, 
    #                            stdout=b'58426\n', 
    #                            stderr=b''
    #                            )
    temp_str = output.stdout.decode()
    # >>> temp_str
    # '58426\n'
    cpu_temp = (int(temp_str.split('\\')[0]))/1000
    print(cpu_temp)
    return cpu_temp

def main():
    while True:
        cpu_temp = meetTemperatuur()
        if cpu_temp >= bovengrens:
            GPIO.output(11, 1)
        elif cpu_temp <= ondergrens:
            GPIO.output(11, 0)
        time.sleep(10)

if __name__ == '__main__':
    main()


