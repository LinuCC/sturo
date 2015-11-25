import sturo

class Driver(object):

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
            self.sturo.set_speed(10)
            self.sturo.set_steering(0)

driver = Driver()
