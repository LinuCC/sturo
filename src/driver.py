import car_attributes
import time
import lib.usonic as usonic

class Driver(object):

    class Speed(object):
        STOP = 0
        SLOW = 15
        NORMAL = 25
        FAST = 35
        REVERSE = -15

    class Mode(object):
        FORWARD = 1
        SLIGHT_ADJUST_RIGHT = 2
        ADJUST_RIGHT = 3
    	RESET = 4

    def __init__(self):
        self.car_attributes = car_attributes.CarAttributes()
        self.car_attributes.set_speed(0)
        self.car_attributes.set_steering(0)
        self.car_attributes.set_transmission(0)
        self.car_attributes.set_front_locker(0)
        self.car_attributes.set_rear_locker(0)
        self.drive_mode = self.Mode.FORWARD
        self.figure_eight()

    def auto_drive(self):
        drive_on = True
        while(drive_on):
            mode = self.evaluate()
            self.drive(mode)

    def evaluate(self):
        # Read a value from the ultrasonic sensor
        uval = usonic.reading(0)
        if uval > 40:
            return self.Mode.FORWARD
        elif uval > 30:
            return self.Mode.SLIGHT_ADJUST_RIGHT
        elif uval > 12:
            return self.Mode.ADJUST_RIGHT
        else:
            return self.Mode.REVERSE

    def drive(self, mode):
        if mode == self.Mode.FORWARD:
            self.car_attributes.set_speed(self.Speed.FAST)
            self.car_attributes.set_steering(0)
        if mode == self.Mode.SLIGHT_ADJUST_RIGHT:
            self.car_attributes.set_speed(self.Speed.NORMAL)
            self.car_attributes.set_steering(20)
        if mode == self.Mode.ADJUST_RIGHT:
            self.car_attributes.set_speed(self.Speed.SLOW)
            self.car_attributes.set_steering(45)
        if mode == self.Mode.STOP:
            self.car_attributes.set_speed(self.Speed.STOP)
            self.car_attributes.set_steering(0)
        if mode == self.Mode.PAUSE:
            self.car_attributes.set_speed(self.Speed.STOP)
            self.car_attributes.set_steering(0)
            time.sleep(5)
        if mode == self.Mode.REVERSE:
            self.reset_car()

    def reset_car(self):
        self.car_attributes.set_speed(0)
        time.sleep(1)
        self.car_attributes.set_speed(self.Speed.REVERSE)
        self.car_attributes.set_steering(0)
        time.sleep(3)

    def figure_eight(self):
    	while(True):
            self.car_attributes.set_speed(self.Speed.FAST)
            self.car_attributes.set_steering(45)
            time.sleep(3.3)
            self.car_attributes.set_steering(0)
            time.sleep(1)
            self.car_attributes.set_steering(-45)
            time.sleep(3.3)
            self.car_attributes.set_steering(0)
            time.sleep(1)
            self.car_attributes.set_speed(self.Speed.STOP)
            time.sleep(5)

driver = Driver()
