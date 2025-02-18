from servo import Servo
import time
import math
import machine
from machine import I2C
from machine import Pin
import ssd1306

# Standard Constants 
L1 = 76.875 #Arm 1 length in mm 
L2 = 106 #Arm 2 length in mm 

def getTheta1(x, y):
    beta = math.atan2(y, x)
    cos_theta2 = (x**2 + y**2 - L1**2 - L2**2) / (2 * L1 * L2)
    sin_theta2 = math.sqrt(1 - cos_theta2**2)
    phi = math.atan2((L2 * sin_theta2), (L1 + L2 * cos_theta2))
    theta1 = beta - phi 
    theta1 = math.degrees(theta1)
    print(-(theta1 - 90))
    return -(theta1 - 90)

def getTheta2(x, y):
    cos_theta2 = (x**2 + y**2 - L1**2 - L2**2) / (2 * L1 * L2) 
    theta2 = math.acos(cos_theta2)
    theta2 = math.degrees(theta2)
    return -theta2

def goToPoint(x, y, s0, s1):
    theta1 = getTheta1(x, y)
    theta2 = getTheta2(x, y)
    s0.write(theta1)
    s1.write(theta2)

def move_in_line(x_start, y_start, x_end, y_end, num_steps, s0, s1):
    for k in range(num_steps + 1):  # +1 to include the endpoint
        # Interpolate intermediate positions 
        x = x_start + k * (x_end - x_start) / num_steps
        y = y_start + k * (y_end - y_start) / num_steps

        # Move servos to the calculated angles
        goToPoint(-x, y, s0, s1)

        # Add a small delay for smooth transition
        time.sleep(0.05)  # Tune the delay as necessary

servo0 = Servo(0)
servo1 = Servo(1)

arm_max = 182.875
x = -100
x = -x

y = 100

#goToPoint(x, y, servo0, servo1)

'''
theta1 = getTheta1(x, y)
theta2 = getTheta2(x, y)
goToPoint(x, y, servo0, servo1)
time.sleep(1)'''

'''
goToPoint(-182.875, 0, servo0, servo1)
time.sleep(0.5)
goToPoint(182.875, 0, servo0, servo1)
'''

'''
move_in_line(-100, 50, -50, 150, 10, servo0, servo1)
time.sleep(0.25)
move_in_line(-50, 150, 0, 100, 10, servo0, servo1)
time.sleep(0.25)
move_in_line(0, 100, 50, 150, 10, servo0, servo1)
time.sleep(0.25)
move_in_line(50, 150, 100, 50, 10, servo0, servo1)
'''

'''
# Makes the letter "M"
goToPoint(175, 50, servo0, servo1)
time.sleep(0.5)
goToPoint(50, 150, servo0, servo1)
time.sleep(0.5)
goToPoint(0, 100, servo0, servo1)
time.sleep(0.5)
goToPoint(0, 150, servo0, servo1)
time.sleep(0.5)
goToPoint(-100, 50, servo0, servo1)
time.sleep(5)
goToPoint(175, 50, servo0, servo1)
#goToPoint(0, arm_max, servo0, servo1)
'''

# test points
# goToPoint(75, 100, servo0, servo1)

# dolpin points 
'''
1 - (50, 125)
2 - (-10, 155)
3 - (-17, 164.5)
4 - (-25, 175)
5 - (-23, 144) 
6 - (-10, 155)
7 - (-60, 113.5)
8 - (-100, 125)
9 - (-75, 100)
10 - (-60, 113.5)
11 - (-75, 100)
12 - (-80, 70)
13 - (-51.5, 105) 
14 - (-75, 100)
15 - (-5, 115)
16 - (-10, 100)
17 - (20, 120)
18 - (-5, 115)
19 - (50, 125)
'''

# dolphin
# Note: x-values flipped bc coordinate system is weird 
goToPoint(-50, 135, servo0, servo1) #1 ✓
time.sleep(0.5)
goToPoint(10, 165, servo0, servo1) #2
time.sleep(0.5)
#goToPoint(17, 169.5, servo0, servo1) #3
#time.sleep(0.25)
goToPoint(25, 175, servo0, servo1) #4
time.sleep(0.5)
goToPoint(23, 154, servo0, servo1) #5
time.sleep(0.5)
goToPoint(10, 165, servo0, servo1) #6
time.sleep(0.5)
goToPoint(60, 123.5, servo0, servo1) #7
time.sleep(0.5)
goToPoint(100, 135, servo0, servo1) #8
time.sleep(0.5)
goToPoint(75, 110, servo0, servo1) #9
time.sleep(0.5)
goToPoint(60, 123.5, servo0, servo1) #10
time.sleep(0.5)
goToPoint(75, 110, servo0, servo1) #11
time.sleep(0.5)
goToPoint(80, 80, servo0, servo1) #12
time.sleep(0.5)
goToPoint(51.5, 115, servo0, servo1) #13
time.sleep(0.5)
goToPoint(75, 110, servo0, servo1) #14
time.sleep(0.5)
goToPoint(5, 125, servo0, servo1) #15
time.sleep(0.5)
goToPoint(10, 110, servo0, servo1) #16
time.sleep(0.5)
goToPoint(-20, 130, servo0, servo1) #17
time.sleep(0.5)
goToPoint(5, 125, servo0, servo1) #18
time.sleep(0.5)
goToPoint(-50, 135, servo0  , servo1) #19
time.sleep(0.5)



'''
# Move from (50, 50) to (150, 150) in a straight line with 100 intermediate steps
move_in_line(-40, 100, -40, 160, 20, servo0, servo1)
time.sleep(0.25)
move_in_line(-40, 160, 20, 160, 20, servo0, servo1)
time.sleep(0.25)
move_in_line(20, 160, -40, 160, 20, servo0, servo1)
time.sleep(0.25)
move_in_line(-40, 160, -40, 150, 20, servo0, servo1)
time.sleep(0.25)
move_in_line(-40, 150, 20, 150, 20, servo0, servo1)
'''

'''
time.sleep(1)
move_in_line(-100, 150, -72.5, 140, 50, servo0, servo1)
time.sleep(1)
move_in_line(-72.5, 140, -60, 167.5, 50, servo0, servo1)
time.sleep(1)
move_in_line(-60, 167.5, -40, 120, 50, servo0, servo1)
'''


'''
x1, y1= -80, 100
x2, y2 = -100, 150
x3, y3 = -72.5, 140
x4, y4 = -60, 167.5
x5, y5 = -40, 120

x6, y6 = 100, 150 
x7, y7 = 60, 170
#x8, y8 = 30, 175
x9, y9 = 70, 135
#x10, y10 = 30, 145
x11, y11 = 40, 130
x12, y12 = 80, 100

goToPoint(-x1, y1, servo0, servo1)
time.sleep(2)
goToPoint(-x2, y2, servo0, servo1)
time.sleep(2)
goToPoint(-x3, y3, servo0, servo1)
time.sleep(2)
goToPoint(-x4, y4, servo0, servo1)
time.sleep(2)
goToPoint(-x5, y5, servo0, servo1)
time.sleep(2)

goToPoint(-x6, y6, servo0, servo1)
time.sleep(2)
goToPoint(-x7, y7, servo0, servo1)
time.sleep(2)
#goToPoint(-x8, y8, servo0, servo1)
#time.sleep(2)
goToPoint(-x9, y9, servo0, servo1)
time.sleep(2)
#goToPoint(-x10, y10, servo0, servo1)
#time.sleep(2)
goToPoint(-x11, y11, servo0, servo1)
time.sleep(2)
goToPoint(-x12, y12, servo0, servo1)
'''

'''
i2c = I2C(scl = Pin(23), sda = Pin(22))
# note you might get a warning here - you can ignore it

display = ssd1306.SSD1306_I2C(128, 64,i2c)

display.rect(10,10,60,50,1)
display.text(str(-theta1) + ' ' + str(-theta2), 0, 0, 1)
display.show()
'''


'''
angle1 = 90
angle2 = 90 
servo0.write(-angle1)
servo1.write(-angle2)
'''
