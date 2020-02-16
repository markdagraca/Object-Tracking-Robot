from adafruit_motorkit import MotorKit
import time
robot=MotorKit()


robot.motor1.throttle=1.0
time.sleep(1)
robot.motor1.throttle=0
