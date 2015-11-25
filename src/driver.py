import sturo

class Driver(object):

    class Mode(Object):
        FORWARD = 1
        SLIGHT_ADJUST_RIGHT = 2
        ADJUST_RIGHT = 3

    def __init__(self):
        self.sturo = Sturo()
        self.sturo.set_speed(0)
        self.sturo.set_steering(0)
        self.sturo.set_transmission(0)
        self.sturo.set_front_locker(0)
        self.sturo.set_rear_locker(0)
        self.drive_mode =

    def auto_drive(self):
        drive_on = True
        while(drive_on):
            mode = self.check_sensors()
            self.drive(mode)

    def evaluate(self):
        return Mode.FORWARD

    def drive(self, mode):
        if mode == Mode.FORWARD:
            self.sturo.set_speed(10)
            self.sturo.set_steering(0)

driver = Driver()
