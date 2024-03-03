"""ILI9341 demo (bouncing boxes)."""
from machine import Pin, SoftSPI
import random
from ili9341 import Display, color565
from utime import sleep_us, ticks_cpu, ticks_us, ticks_diff
from time import sleep

#----------------INITS-----------
left = Pin(12, Pin.IN, Pin.PULL_UP)
right = Pin(27, Pin.IN, Pin.PULL_UP)
red = Pin(25, Pin.OUT)
green = Pin(26, Pin.OUT)
spi = SoftSPI(sck=Pin(5), mosi=Pin(19), miso=Pin(12))
display = Display(spi, cs=Pin(15), dc=Pin(32), rst=Pin(33))

W = 240
H = 320

items = ['food', 'glass', 'plastic bottle', 'can', 'paper', 'battery']
recycle = [0,1,1,1,1,0]
#---------------FALLING ITEM CLASS-----------
class fallingitem(object):
    def __init__(self, screen_width, screen_height, size, display, color, left, right):
        self.size = size
        self.w = screen_width
        self.h = screen_height
        self.display = display
        self.color = color
        self.left = left
        self.right = right

        self.x = int(self.w /3.0)
        self.y = 3 #start with y at the top
        self.prev_x = self.x
        self.prev_y = self.y

    def update_pos(self):
        """Update box position and speed."""
        x = self.x
        y = self.y       

        self.prev_x = x
        self.prev_y = y

        if(not left.value()):
            self.prev_x = x
            self.x += 5
        if(not right.value()):
            self.prev_x = x
            self.x -= 5
        
        
        self.prev_y = y
        self.y += 5
        
        if(self.y + self.size > 230):
            self.y = 0
        if(self.x + self.size > self.w):
            self.x = self.w
        if(self.x < 0):
            self.x = 0

    def draw(self):
        x = int(self.x)
        y = int(self.y)
        size = self.size
        prev_x = int(self.prev_x)
        prev_y = int(self.prev_y)
        self.display.fill_hrect(prev_x - size,
                                prev_y - size,
                                size, size, 0)
        self.display.fill_hrect(x - size,
                                y - size,
                                size, size, self.color)



#--------------------GAME--LOGIC--------------------
display.clear()
trash = fallingitem(W, H, 20, display, color565(0, 255, 0), left, right) 

#draw trash cans
display.fill_hrect(140,230,80, 90, color565(128, 128, 128))
display.fill_hrect(20,230,80, 90, color565(0, 250, 0))
display.fill_ellipse(60, 230, 40, 10, color565(0, 170, 0))
display.fill_ellipse(180, 230, 40, 10, color565(100, 100, 100))

while True:
    timer = ticks_us()
    win = 0
    green.value(0)
    red.value(0)
    if(trash.y < 10):
        i = random.randrange(6)
    color = recycle[i]
    check = recycle[i]
    
    if(color):
        trash.color = color565(0, 255, 0)
    elif(color == 0):
        trash.color = color565(255,0, 0)
    
    if(check == 1):
        if(trash.x < 120 and trash.y > 200):
            win = 1
            green.value(1)
            sleep(1)
        elif(trash.y > 200):
            red.value(1)
            sleep(1)
    elif(not check):
        if(trash.x > 120 and trash.y > 200):
            win = 1
            green.value(1)
            sleep(1)
        elif(trash.y > 200):
            red.value(1)
            sleep(1)
    
    
    trash.update_pos()
    trash.draw()
    
    timer_dif = 33333 - ticks_diff(ticks_us(), timer)
    if timer_dif > 0:
        sleep_us(timer_dif)


