import car_attributes
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
        self.car_atributes = car_atributes.Sturo()
        self.car_atributes.set_speed(0)
        self.car_atributes.set_steering(0)
        self.car_atributes.set_transmission(0)
        self.car_atributes.set_front_locker(0)
        self.car_atributes.set_rear_locker(0)
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
            self.car_atributes.set_speed(self.Speed.FAST)
            self.car_atributes.set_steering(0)
        if mode == self.Mode.SLIGHT_ADJUST_RIGHT:
            self.car_atributes.set_speed(self.Speed.NORMAL)
            self.car_atributes.set_steering(20)
        if mode == self.Mode.ADJUST_RIGHT:
            self.car_atributes.set_speed(self.Speed.SLOW)
            self.car_atributes.set_steering(45)
        if mode == self.Mode.STOP:
            self.car_atributes.set_speed(self.Speed.STOP)
            self.car_atributes.set_steering(0)
        if mode == self.Mode.PAUSE:
            self.car_atributes.set_speed(self.Speed.STOP)
            self.car_atributes.set_steering(0)
            time.sleep(5)

    def reset_car(self):
        self.car_atributes.set_speed(self.Speed.REVERSE)
        self.car_atributes.set_steering(0)
        time.sleep(2)

driver = Driver()
