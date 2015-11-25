from servo_control.summit_pwm import SummitPWM
import servo_control.servos as servos


class Sturo(object):

    def __init__(self):
        self.pwm = SummitPWM()
        # Servo-data
        self.servo_transmission = servos.Transmission()
        self.servo_rear_locker = servos.RearLocker()
        self.servo_front_locker = servos.FrontLocker()
        self.servo_steering1 = servos.Steering1()
        self.servo_steering2 = servos.Steering2()
        self.servo_esc = servos.Esc()

    def set_speed(self, val):
        """Changes the speed of the car

        Arguments:
        val -- between -100 and 100
        """
        self.pwm.servo_set(self.servo_esc, (float(val) + 100) / 200)

    def set_steering(self, angle):
        """Changes the angle of the wheels

        Arguments:
        angle -- between -45 and 45
        """
        val = (float(angle) + 45) / 90
        self.pwm.servo_set(self.servo_steering1, val)
        self.pwm.servo_set(self.servo_steering2, val)

    def set_transmission(self, val):
        """Sets the transmission
Arguments:
        val -- either 0 for first or 1 for second gear
        """
    	self.pwm.servo_set(self.servo_transmission, val)

    def set_front_locker(self, val):
        """Sets the front locker

        Arguments:
        val -- True for activated, false for not activated
        """
        if val:
            self.pwm.servo_set(self.servo_front_locker, 0)
        else:
            self.pwm.servo_set(self.servo_front_locker, 1)

    def set_rear_locker(self, val):
        """Sets the rear locker

        Arguments:
        val -- True for activated, false for not activated
        """
        if val:
            self.pwm.servo_set(self.servo_rear_locker, 0)
        else:
            self.pwm.servo_set(self.servo_rear_locker, 1)
