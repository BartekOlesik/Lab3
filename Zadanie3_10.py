from gpiozero import LED, AngularServo
from time import sleep

led = LED(23)
servo = AngularServo(24, min_angle=-90, max_angle=90)

def migaj(czas, ile_razy):
    """Miga diodą: 'czas' = długość włączenia/wyłączenia, 'ile_razy' = liczba mignięć."""
    for _ in range(ile_razy):
        led.on()
        sleep(czas)
        led.off()
        sleep(czas)

while True:
    # Ruch w lewo – LED miga wolno
    servo.angle = -90
    migaj(1, 2)        # 2 mignięcia po 1 s  -> 4 s

    # Ruch w prawo – LED miga szybko
    servo.angle = 90
    migaj(0.2, 10)     # 10 mignięć po 0,2 s -> 4 s