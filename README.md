sturo
=====
**An attempt to automate the RC-Car Traxxas Summit using a Raspberry Pi.**

##Overview

Sturo provides a framework allowing to automatically drive a RC-Car, specifically the Traxxas Summit (but trying to be configurable so it can be used with other models, too).
It uses the [Adafruit PWM-driver](http://www.adafruit.com/products/815) to control the servos and a Raspberry Pi to execute the code.


##Helpful / Technical Documentation

by Pascal Ernst, FH Ostfalia Suderburg;
pascal.cc.ernst@gmail.com, p.ernst@ostfalia.de

Used for modifications to the control system of the Traxxas Summit

###Beginning from scratch

####Where to start

A good place to start how the radio control works:
	http://www.rc-airplane-world.com/radio-control-gear.html


####General terms

Tx / radio : Transmitter
Rx : Receiver (for example Traxxas Link)


####Servos

Servo-connectors have three wires:

 * +
 * -
 * S

Servos are controlled by PWM (Pulse width modulation). Two wires supply the
Servo with a DC power supply and one (The "Signal" or S) controls the Servo
with PWM.

The neutral position of a Servo normally is around 1.5 ms of the PWM.
Higher or lower values change the position of the servo.
Generally the minimum pulse will be about 1 ms wide and the maximum pulse will be 2 ms wide.


###Traxxas Link servo-channels

 * Channel 5 - Rear locker (Summit), also supplies power to Led-lights front and back
 * Channel 4 - Front locker (Summit)
 * Channel 3 - Transmission control
 * Channel 2 - Esc-control; Forward / reverse-movement
 * Channel 1 - Steering servo(s)
 * Channel 1 - Same as above (parallel port; eliminates need for Y harness)

###Connection with Raspberry Pi

The connection is made possible with connecting the Raspberry Pi to a PWM driver, preferably the [Adafruit one](http://www.adafruit.com/products/815).
For more information on how to use the Chip with the Raspberry Pi, visit the [Adafruit documentation](http://learn.adafruit.com/adafruit-16-channel-servo-driver-with-raspberry-pi).
You will also need a power-converter to supply the Raspberry Pi with power, since the Raspberry Pi needs 5V, but the Batteries have 8,6V.

Useful Information for the Adafruit PWM Driver:

 * Maximum Current flowing through: 5 Amp
 	(For comparison: The two big servos in charge for steering the Summit need roundabout 1.5A to work properly)
 * The esc build into the Summit (EVX-2) has built-in bec, so there is no need for an additional power-cycle to control     the servos
 * esc and all servos are controlled by standard 50 Hz pwm. Be careful: some servos do not want / need the full range of    pwm-control, especially the front-locker! *TODO: Give some estimated ranges for the servos* 

##Contact
by Pascal Ernst, FH Ostfalia Suderburg;
pascal.cc.ernst@gmail.com, p.ernst@ostfalia.de
