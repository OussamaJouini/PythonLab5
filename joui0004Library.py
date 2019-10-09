#This program calculates the Area of a circle
from math import pi

def calculAreaOfCircle(radius):
    area = radius * radius * pi
    return area


#This program calculates the MPG of a car

def calculMPG (nbrMiles , nbrGallons) :
     MPG = nbrMiles / nbrGallons
     return MPG

#This program converts temperature from Fahr to Celsuis

def convertFahr (Fahr) :
      ConvCels = round(float((Fahr - 32) * 5/9),5)
      return ConvCels

# This program calculates the distance between points
from math import sqrt
def CalcDist (x1, y1, x2, y2) :
    a=y1-y2
    b=x1-x2

    distance = sqrt((a**2)+(b**2))
    return distance

#This program displays a vertical line at a given x coordinate on the gfx hat.

from gfxhat import lcd
def VerticalLineAtXCoord (x) :
     y=0
     while (y<=63):
        if (x>=0) and (x<=127) :
            lcd.set_pixel(y,x,1)
            y+=1

#This program displays a horizontal line at a given y coordinate on the gfxhat.

from ghxhat import lcd
def horizontalLineAtYCoord (y):
     x=0
     while (x<=127):
        if (y>=0) and (y<=63) :
            lcd.set_pixel(y,x,1)
            x+=1

#This program displays a staircase starting at a specific coordinate. One stair has a width of w and a height of h.
#1.North East Stair's direction.

from gfxhat import lcd
def stairCaseNE (x,y,w,h) :
    while (x+w<127 and y-h>=0) :
         for i in range(h):
             if y >= 0 :
                     lcd.set_pixel(x,y-i,1)
             else:
                     h = i
         for j in range (0,w):
             if x+j <= 127 :
                     lcd.set_pixel(x+j,y-h,1)
             else :
                     w=j
     x,y = x+w,y-h 

#2.North West Stair's direction.

from gfxhat import lcd
 def stairCaseNW(x, y, w, h) :
     while (x-w>=0 and y-h>=0) :
             for i in range(h):
                   if y >= 0 :
                         lcd.set_pixel(x,y-i,1)
                   else :
                         h = i
           for j in range (0,w):
                   if x-j >= 0 :
                         lcd.set_pixel(x-j,y-h,1)
                   else :
                         w=j
        x,y = x-w,y-h

#3.South West Stair's direction.

 from gfxhat import lcd
 def stairCaseSW (x, y, w, h) :
     while (x-w>=0 and y+h<=63) :
             for i in range(h) :
                     if y+i <= 63:
                             lcd.set_pixel(x,y+i,1)
                     else:
                             h = i
             for j in range (0,w):
                     if x-j >= 0:
                             lcd.set_pixel(x-j,y+h,1)
                     else:
                             w=j
             x,y = x-w,y+h

#4.South East Stair's direction.

from gfxhat import lcd
 def stairCaseSE (x, y, w, h) :
     while (x+w<=127 and y+h<=63) :
         for i in range(h):
             if y+i <= 63 :
                     lcd.set_pixel(x,y+i,1)
             else:
                     h = i
         for j in range (0,w):
             if x+j <= 127 :
                     lcd.set_pixel(x+j,y+h,1)
             else :
                     w=j
     x,y = x+w,y+h            

#This program displays random pixel on the screen for a given period of time specifies in seconds.

 from random import randint
 from gfxhat import lcd
 from time import sleep
 def randomP (S):
     x=randint(0,127)
     y=randint(0,63)
     while(x>=0 and x<=127):
             lcd.set_pixel(x,y,1)
             sleep(s)
     while(y>=0 and y<=63):
             lcd.set_pixel(x,y,1)
             sleep(s)

# This program resets the backlight color.
from gfxhat import backlight
def clearBacklight()
r=0
g=0
b=0
backlight.set_all(r,g,b)
backlight.show()

