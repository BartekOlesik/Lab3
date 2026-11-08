from gpiozero import AngularServo
from time import sleep

servo = AngularServo(24, min_angle=-90, max_angle=90)

while True:
    servo.angle = -90   # skrajne lewo
    sleep(1)
    servo.angle = 90    # skrajne prawo
    sleep(1)