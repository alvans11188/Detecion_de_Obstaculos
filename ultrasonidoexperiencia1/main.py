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

ultrasonido = UltrasonicSensor(Port.S3)

while True:
    ultrasonidoDetectado = ultrasonido.distance()
    while  ultrasonidoDetectado >= 200:
        ultrasonidoDetectado = ultrasonido.distance()
        md.run(100)
        mi.run(100)
    md.stop()
    mi.run_time(180, 2000)