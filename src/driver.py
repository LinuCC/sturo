import sturo
import time

class Driver(object):

    class Speed(object):
        STOP = 0
        SLOW = 15
        NORMAL = 18
        FAST = 20
        REVERSE = -20

    class Mode(object):
        FORWARD = 1
        SLIGHT_ADJUST_RIGHT = 2
        ADJUST_RIGHT = 3
    	RESET = 4

    def __init__(self):
        self.sturo = sturo.Sturo()
        self.sturo.set_speed(0)
        self.sturo.set_steering(0)
        self.sturo.set_transmission(0)
        self.sturo.set_front_locker(0)
        self.sturo.set_rear_locker(0)
        self.drive_mode = self.Mode.FORWARD

    def auto_drive(self):
        drive_on = True
        while(drive_on):
            mode = self.evaluate()
            self.drive(mode)

    def evaluate(self):
        return self.Mode.FORWARD

    def drive(self, mode):
        if mode == self.Mode.FORWARD:
            self.sturo.set_speed(self.Speed.FAST)
            self.sturo.set_steering(0)
        if mode == self.Mode.SLIGHT_ADJUST_RIGHT:
            self.sturo.set_speed(self.Speed.NORMAL)
            self.sturo.set_steering(20)
        if mode == self.Mode.ADJUST_RIGHT:
            self.sturo.set_speed(self.Speed.SLOW)
            self.sturo.set_steering(45)
        if mode == self.Mode.STOP:
            self.sturo.set_speed(self.Speed.STOP)
            self.sturo.set_steering(0)
        if mode == self.Mode.PAUSE:
            self.sturo.set_speed(self.Speed.STOP)
            self.sturo.set_steering(0)
            time.sleep(5)

    def reset_car(self):
        self.sturo_set_speed(self.Speed.REVERSE)
        self.sturo_set_steering(0)
        time.sleep(2)

driver = Driver()
