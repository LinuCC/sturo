from lib.adafruit_servo_driver.adafruit_servo_driver import PWM
import servos


class SummitPWM(PWM):
    """Sets values allowing to control the Traxxas Summits servos"""
    def __init__(self):
        #super(SummitPWM, self).__init__(0x40, debug=False)
        PWM.__init__(self, address=0x40, debug=False)
        self.setPWMFreq(50)

    def servo_set(self, servo, range_percentage):
        diff = (servo.range_max - servo.range_min) * range_percentage
        val = servo.range_min + diff
        self.setPWM(servo.pwm_port, 0, int(val))
