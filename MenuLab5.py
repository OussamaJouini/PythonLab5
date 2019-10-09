from gfxhat import lcd, backlight
from joui0004library import VerticalLineAtXCoord, horizontalLineAtYCoord, stairCaseNE, stairCaseNW, stairCaseSW, stairCaseSE, randomP, clearBacklight  


print(""" Hello Everyone and Welcome ....Here are a Menu for some functions you may wish to run.
Could you please pick the correct number of the disired function. (from 1 to 8)
1. #This program displays a vertical line at a given x coordinate on the gfx hat.
2. #This program displays a horizontal line at a given y coordinate on the gfxhat.
These 4 programs below (3,4,5,6) display a staircase starting at a specific coordinate. One stair has a width of w and a height of h.
3. #North East Stair's direction.
4. #North West Stair's direction.
5. #South West Stair's direction.
6. #South East Stair's direction.
7. #This program displays random pixel on the screen for a given period of time specifies in seconds.
8. #This program resets the backlight color.
""")

choice= int(input("Could you please enter the corresponding number to run desired function : "))
if (choice >= 9) or (choice <=0) :
    print("""ERROR !! 
    There is no function correspond to this number ..
    Please choice one of the function above and enter the number corresponding to the desired function <<From 1 to 8 >>. 
    Thanks""")
    break

elif choice == '1':
    x = int(input("Please enter the X Coordinate value: "))
    lcd.clear()
    VerticalLineAtXCoord (x)
    lcd.show()

elif choice == '2':
    y = int(input("Please enter the Y Coordinate value: "))
    lcd.clear()
    VhorizontalLineAtYCoord (y)
    lcd.show()

elif choice == '3':
    x = int(input("Please enter the X Coordinate value for the stairs: "))
    y = int(input("Please enter the Y Coordinate value for the stairs: "))
    w = int(input("Please enter the width value for the stairs: "))
    h = int(input("Please enter the height value for the stairs: "))
    lcd.clear()
    stairCaseNE (x,y,w,h) 
    lcd.show()

elif choice == '4':
    x = int(input("Please enter the X Coordinate value for the stairs: "))
    y = int(input("Please enter the Y Coordinate value for the stairs: "))
    w = int(input("Please enter the width value for the stairs: "))
    h = int(input("Please enter the height value for the stairs: "))
    lcd.clear()
    stairCaseNW (x,y,w,h) 
    lcd.show()

elif choice == '5':
    x = int(input("Please enter the X Coordinate value for the stairs: "))
    y = int(input("Please enter the Y Coordinate value for the stairs: "))
    w = int(input("Please enter the width value for the stairs: "))
    h = int(input("Please enter the height value for the stairs: "))
    lcd.clear()
    stairCaseSw (x,y,w,h) 
    lcd.show()

elif choice == '6':
    x = int(input("Please enter the X Coordinate value for the stairs: "))
    y = int(input("Please enter the Y Coordinate value for the stairs: "))
    w = int(input("Please enter the width value for the stairs: "))
    h = int(input("Please enter the height value for the stairs: "))
    lcd.clear()
    stairCaseSE (x,y,w,h) 
    lcd.show()

elif choice == '7':
    s = int(input("for how many seconds you would like the function to run: "))
    lcd.clear()
    randomP (s)
    lcd.show()

elif choice == '8':
    clearBacklight ()




