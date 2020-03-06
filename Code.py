import pyb
import machine, time
from machine import Pin

tp = pyb.pin('X6', pyb.Pin.OUT_PP) #trigger out
ep = pyb.Pin(pyb.Pin.board.X5, pyb.Pin.IN) #echo input

class HCSR04(object):
    def __init__(self, trigger_pin, echo_pin, echo_timeout_us=500*2*30):
        self.echo_timeout_us = echo_timeout_us
        self.trigger = Pin(trigger_pin, mode=Pin.OUT, pull=None)
        self.trigger.value(0)
        self.echo = Pin(echo_pin, mode=Pin.IN, pull=None)

    def _send_pulse_and_wait(self):
        self.trigger.value(0)
        time.sleep_us(5)
        self.trigger.value(1)
        time.sleep_us(10)
        self.trigger.value(0)
        try:
            pulse_time = machine.time_pulse_us(self.echo, 1, self.echo_timeout_us)
            return pulse_time
        except OSError as ex:
            if ex.args[0] == 110:
                raise OSError('Out of range')
            raise ex

    def distance_cm(self):
        pulse_time = self._send_pulse_and_wait()
        cms = (pulse_time / 2) / 29.1
        return cms


obj = HCSR04(trigger_pin=tp, echo_pin=ep)

led1 = pyb.Pin('X1', pyb.Pin.OUT_PP)
led2 = pyb.Pin('X2', pyb.Pin.OUT_PP)
sw = pyb.switch()
y = int(input())
r = 2.54 /100
R = 2 * r
rpm = 4000
d = 1
d1 = 1
d2 = 1
d3 = 3
d4 = 3
if y == 1:
    led1.on()
    led2.on()
    x = 0
    p = pyb.millis()
    while pyb.millis() - x - (pyb.millis() - p) < (((d1/(2*rpm*r)))*60*1000):
        flag = 0                                                                        # pyb.millis returns time for which the code has started execution
        while obj.distance_cm() < 5:                                                    # if ultrasonic sensor returns a value less than 5 then we should halt the robo
            if flag == 0:																# turning the flag to 1 if it enters the loop once
                p = pyb.millis()
                flag = 1
            led1.off()																	# if an obstacle is encounterd then we should stop the robo
            led2.off()
    led2.off()
    x = pyb.millis()
    p = pyb.millis()
    flag = 0
    while pyb.millis() - x - (pyb.millis() - p) < (((((R*3.14)/2)/(2*rpm*r)))*60*1000): # Subtracting the time it has stopped due to an obstacle
        flag = 0
        while obj.distance_cm() < 5:                                                    
            if flag == 0:
                p = pyb.millis()
                flag = 1
            led1.off()
            led2.off()
    led1.on()
    led2.on()
    x = pyb.millis()
    p = pyb.millis()
    flag = 0
    while pyb.millis() - x - (pyb.millis() - p)  < (((d/(2*rpm*r)))*60*1000):
        flag = 0
        while obj.distance_cm() < 5:
            if flag == 0:
                p = pyb.millis()
                flag = 1
            led1.off()
            led2.off()
    led1.off()
    led2.off()
    s = pyb.millis()
    while True:
        if sw.value():                                                     # ts is the time which the robo has stopped to take the order
            break
    r = pyb.millis()
    ts = r - s
    led1.on()
    led2.off()
    x = pyb.millis()
    p = pyb.millis()
    flag = 0
    while pyb.millis() - x - ts - (pyb.millis() - p) < (((2*((R*3.14)/2)/(2*rpm*r)))*60*1000):
        flag = 0
        while obj.distance_cm() < 5:
            if flag == 0:
                p = pyb.millis()
                flag = 1
            led1.off()
            led2.off()
    led1.on()
    led2.on()
    x = pyb.millis()
    p = pyb.millis()
    flag = 0
    while pyb.millis() - x - ts - (pyb.millis() - p) < (((d/(2*rpm*r)))*60*1000):
        flag = 0
        while obj.distance_cm() < 5:
            if flag == 0:
                p = pyb.millis()
                flag = 1
            led1.off()
            led2.off()
    led1.off()
    led2.on()
    x = pyb.millis()
    p = pyb.millis()
    flag = 0
    while pyb.millis() - x - ts  - (pyb.millis() - p) < (((((R*3.14)/2)/(2*rpm*r)))*60*1000):
        flag = 0
        while obj.distance_cm() < 5:
            if flag == 0:
                p = pyb.millis()
                flag = 1
            led1.off()
            led2.off()

    led1.on()
    led2.on()
    x = pyb.millis()
    p = pyb.millis()
    flag = 0
    while pyb.millis() - x -  ts  - (pyb.millis() - p) < (((d1/(2*rpm*r)))*60*1000):
        flag = 0
        while obj.distance_cm() < 5:
            if flag == 0:
                p = pyb.millis()
                flag = 1
            led1.off()
            led2.off()
    led1.off()
    led2.off()
elif y == 2:
    led1.on()
    led2.on()
    x = 0
    p = pyb.millis()
    while pyb.millis() - x - (pyb.millis() - p) < (((d2 / (2 * rpm * r))) * 60 * 1000):
        flag = 0
        while obj.distance_cm() < 5:
            if flag == 0:
                p = pyb.millis()
                flag = 1
            led1.off()
            led2.off()
    led1.off()
    x = pyb.millis()
    p = pyb.millis()
    flag = 0
    while pyb.millis() - x - (pyb.millis() - p) < (((((R * 3.14) / 2) / (2 * rpm * r))) * 60 * 1000):
        flag = 0
        while obj.distance_cm() < 5:
            if flag == 0:
                p = pyb.millis()
                flag = 1
            led1.off()
            led2.off()
    led1.on()
    led2.on()
    x = pyb.millis()
    p = pyb.millis()
    flag = 0
    while pyb.millis() - x - (pyb.millis() - p) < (((d / (2 * rpm * r))) * 60 * 1000):
        flag = 0
        while obj.distance_cm() < 5:
            if flag == 0:
                p = pyb.millis()
                flag = 1
            led1.off()
            led2.off()
    led1.off()
    led2.off()
    s = pyb.millis()
    while True:
        if sw.value():
            break
    r = pyb.millis()
    ts = r - s
    led1.off()
    led2.on()
    x = pyb.millis()
    p = pyb.millis()
    flag = 0
    while pyb.millis() - x - ts - (pyb.millis() - p) < (((2 * ((R * 3.14) / 2) / (2 * rpm * r))) * 60 * 1000):
        flag = 0
        while obj.distance_cm() < 5:
            if flag == 0:
                p = pyb.millis()
                flag = 1
            led1.off()
            led2.off()
    led1.on()
    led2.on()
    x = pyb.millis()
    p = pyb.millis()
    flag = 0
    while pyb.millis() - x - ts - (pyb.millis() - p) < (((d / (2 * rpm * r))) * 60 * 1000):
        flag = 0
        while obj.distance_cm() < 5:
            if flag == 0:
                p = pyb.millis()
                flag = 1
            led1.off()
            led2.off()
    led2.off()
    led1.on()
    x = pyb.millis()
    p = pyb.millis()
    flag = 0
    while pyb.millis() - x - ts - (pyb.millis() - p) < (((((R * 3.14) / 2) / (2 * rpm * r))) * 60 * 1000):
        flag = 0
        while obj.distance_cm() < 5:
            if flag == 0:
                p = pyb.millis()
                flag = 1
            led1.off()
            led2.off()

    led1.on()
    led2.on()
    x = pyb.millis()
    p = pyb.millis()
    flag = 0
    while pyb.millis() - x - ts - (pyb.millis() - p) < (((d2 / (2 * rpm * r))) * 60 * 1000):
        flag = 0
        while obj.distance_cm() < 5:
            if flag == 0:
                p = pyb.millis()
                flag = 1
            led1.off()
            led2.off()
    led1.off()
    led2.off()
elif y == 3:
    led1.on()
    led2.on()
    x = 0
    p = pyb.millis()
    while pyb.millis() - x - (pyb.millis() - p) < (((d3 / (2 * rpm * r))) * 60 * 1000):
        flag = 0
        while obj.distance_cm() < 5:
            if flag == 0:
                p = pyb.millis()
                flag = 1
            led1.off()
            led2.off()
    led1.off()
    x = pyb.millis()
    p = pyb.millis()
    flag = 0
    while pyb.millis() - x - (pyb.millis() - p) < (((((R * 3.14) / 2) / (2 * rpm * r))) * 60 * 1000):
        flag = 0
        while obj.distance_cm() < 5:
            if flag == 0:
                p = pyb.millis()
                flag = 1
            led1.off()
            led2.off()
    led1.on()
    led2.on()
    x = pyb.millis()
    p = pyb.millis()
    flag = 0
    while pyb.millis() - x - (pyb.millis() - p) < (((d / (2 * rpm * r))) * 60 * 1000):
        flag = 0
        while obj.distance_cm() < 5:
            if flag == 0:
                p = pyb.millis()
                flag = 1
            led1.off()
            led2.off()
    led1.off()
    led2.off()
    s = pyb.millis()
    while True:
        if sw.value():
            break
    r = pyb.millis()
    ts = r - s
    led1.off()
    led2.on()
    x = pyb.millis()
    p = pyb.millis()
    flag = 0
    while pyb.millis() - x - ts - (pyb.millis() - p) < (((2 * ((R * 3.14) / 2) / (2 * rpm * r))) * 60 * 1000):
        flag = 0
        while obj.distance_cm() < 5:
            if flag == 0:
                p = pyb.millis()
                flag = 1
            led1.off()
            led2.off()
    led1.on()
    led2.on()
    x = pyb.millis()
    p = pyb.millis()
    flag = 0
    while pyb.millis() - x - ts - (pyb.millis() - p) < (((d / (2 * rpm * r))) * 60 * 1000):
        flag = 0
        while obj.distance_cm() < 5:
            if flag == 0:
                p = pyb.millis()
                flag = 1
            led1.off()
            led2.off()
    led2.off()
    led1.on()
    x = pyb.millis()
    p = pyb.millis()
    flag = 0
    while pyb.millis() - x - ts - (pyb.millis() - p) < (((((R * 3.14) / 2) / (2 * rpm * r))) * 60 * 1000):
        flag = 0
        while obj.distance_cm() < 5:
            if flag == 0:
                p = pyb.millis()
                flag = 1
            led1.off()
            led2.off()

    led1.on()
    led2.on()
    x = pyb.millis()
    p = pyb.millis()
    flag = 0
    while pyb.millis() - x - ts - (pyb.millis() - p) < (((d3 / (2 * rpm * r))) * 60 * 1000):
        flag = 0
        while obj.distance_cm() < 5:
            if flag == 0:
                p = pyb.millis()
                flag = 1
            led1.off()
            led2.off()
    led1.off()
    led2.off()
elif y == 4:
    led1.on()
    led2.on()
    x = 0
    p = pyb.millis()
    while pyb.millis() - x - (pyb.millis() - p) < (((d4 / (2 * rpm * r))) * 60 * 1000):
        flag = 0
        while obj.distance_cm() < 5:
            if flag == 0:
                p = pyb.millis()
                flag = 1
            led1.off()
            led2.off()
    led2.off()
    x = pyb.millis()
    p = pyb.millis()
    flag = 0
    while pyb.millis() - x - (pyb.millis() - p) < (((((R * 3.14) / 2) / (2 * rpm * r))) * 60 * 1000):
        flag = 0
        while obj.distance_cm() < 5:
            if flag == 0:
                p = pyb.millis()
                flag = 1
            led1.off()
            led2.off()
    led1.on()
    led2.on()
    x = pyb.millis()
    p = pyb.millis()
    flag = 0
    while pyb.millis() - x - (pyb.millis() - p) < (((d / (2 * rpm * r))) * 60 * 1000):
        flag = 0
        while obj.distance_cm() < 5:
            if flag == 0:
                p = pyb.millis()
                flag = 1
            led1.off()
            led2.off()
    led1.off()
    led2.off()
    s = pyb.millis()
    while True:
        if sw.value():
            break
    r = pyb.millis()
    ts = r - s
    led1.on()
    led2.off()
    x = pyb.millis()
    p = pyb.millis()
    flag = 0
    while pyb.millis() - x - ts - (pyb.millis() - p) < (((2 * ((R * 3.14) / 2) / (2 * rpm * r))) * 60 * 1000):
        flag = 0
        while obj.distance_cm() < 5:
            if flag == 0:
                p = pyb.millis()
                flag = 1
            led1.off()
            led2.off()
    led1.on()
    led2.on()
    x = pyb.millis()
    p = pyb.millis()
    flag = 0
    while pyb.millis() - x - ts - (pyb.millis() - p) < (((d / (2 * rpm * r))) * 60 * 1000):
        flag = 0
        while obj.distance_cm() < 5:
            if flag == 0:
                p = pyb.millis()
                flag = 1
            led1.off()
            led2.off()
    led1.off()
    led2.on()
    x = pyb.millis()
    p = pyb.millis()
    flag = 0
    while pyb.millis() - x - ts - (pyb.millis() - p) < (((((R * 3.14) / 2) / (2 * rpm * r))) * 60 * 1000):
        flag = 0
        while obj.distance_cm() < 5:
            if flag == 0:
                p = pyb.millis()
                flag = 1
            led1.off()
            led2.off()

    led1.on()
    led2.on()
    x = pyb.millis()
    p = pyb.millis()
    flag = 0
    while pyb.millis() - x - ts - (pyb.millis() - p) < (((d4 / (2 * rpm * r))) * 60 * 1000):
        flag = 0
        while obj.distance_cm() < 5:
            if flag == 0:
                p = pyb.millis()
                flag = 1
            led1.off()
            led2.off()
    led1.off()
    led2.off()

