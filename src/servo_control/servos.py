"""Defines the existing servos and their data
"""

class Servo(object):
    """Represents a pwm-controlled servo"""
    def __init__(self):
        self.range_min = 219   # 1ms wide pulse
        self.range_max = 438   # 2ms wide pulse
        self.pwm_port = 0   # The port the servo can be accessed from

    def pwm_range_adjust(self, percmin, percmax):
        """allows to change the pwm-range

        Useful when not the full movement of the servo is used
        Arguments:
        percmin -- percentage of the range minimum. Giving 0.5 as percmin
            would half the range by setting the range_min to the middle of the
            range
        percmax -- percentage-difference of the maximum range. -''-
        """
        pwm_range = self.range_max - self.range_min
        self.range_min = ((1 - percmin) * pwm_range) + self.range_min
        self.range_max = self.range_max - ((1 - percmax) * pwm_range)


class Esc(Servo):
    """The esc of the Summit"""
    def __init__(self):
        super(Esc, self).__init__()
        self.pwm_port = 4


class Steering1(Servo):
    """The steering servos of the Summit"""
    def __init__(self):
        super(Steering1, self).__init__()
        self.pwm_port = 0


class Steering2(Servo):
    """The steering servos of the Summit"""
    def __init__(self):
        super(Steering2, self).__init__()
        self.pwm_port = 1


class RearLocker(Servo):
    """The rear locker servo of the Summit"""
    def __init__(self):
        super(RearLocker, self).__init__()
        self.pwm_port = 10
        # This servos movement is quite restricted
        self.pwm_range_adjust(1, 0.9)


class FrontLocker(Servo):
    """The front locker servo of the Summit"""
    def __init__(self):
        super(FrontLocker, self).__init__()
        self.pwm_port = 9
        # This servos movement is quite restricted
        self.pwm_range_adjust(0.7, 0.9)


class Transmission(Servo):
    """The transmission servo of the Summit"""
    def __init__(self):
        super(Transmission, self).__init__()
        self.pwm_port = 8
        # Not really sure if this keeps the transmission in place even when going fast, but this
        # should do it without putting too much pressure on the servo
        self.pwm_range_adjust(0.9, 0.8)
