#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

ev3 = EV3Brick()
md = Motor(Port.C)
mi = Motor(Port.B)
robot = DriveBase(mi,md,55.5,104)
sonido = '/home/robot/ultrasonidoexperiencia2/sonido/shouting.wav'

ultrasonido = UltrasonicSensor(Port.S3)

while True:
    ultrasonidoDetectado = ultrasonido.distance()
    while  ultrasonidoDetectado >= 200:
        ev3.light.on(Color.GREEN)
        ultrasonidoDetectado = ultrasonido.distance()
        md.run(100)
        mi.run(100)
    ev3.light.on(Color.RED)
    md.stop()
    mi.stop()
    ev3.speaker.set_volume(500, which='_all_')
    ev3.speaker.play_file(sonido)
    ev3.light.on(Color.YELLOW)
    robot.straight(-100)
    robot.stop()
    mi.run_time(200, 2000)