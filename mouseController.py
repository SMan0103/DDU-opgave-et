import mouse
import screeninfo as si

screen_x = si.get_monitors()[0].width
screen_y = si.get_monitors()[0].height

common_x = [0, 0, 0] # List of x coordinates
common_y = [0, 0, 0] # List of y coordinates

def getCommon(x, y): # Get the common x and y coordinates
    common_x.append(x) # Add the x coordinate to the list
    common_y.append(y) # Add the y coordinate to the list
    common_x.pop(0) # Remove the first element of the x list
    common_y.pop(0) # Remove the first element of the y list
    return (sum(common_x) / len(common_x), sum(common_y) / len(common_y)) # Return the average of the x and y coordinates

def getX(c): # Get the x coordinate
    if (screen_x * c) > screen_x:
        return screen_x
    if (screen_x * c) < 0:
        return 0
    return screen_x * c

def getY(c): # Get the y coordinate
    if (screen_y * c) > screen_y:
        return screen_y
    if (screen_y * c) < 0:
        return 0
    return screen_y * c

def move(x, y):
    comX, comY = getCommon(x, y)
    offsetX = 0
    offsetY = 0
    if (getX(comX) < screen_x/2-screen_x/4):
        mouse.move(getX(comX)-offsetX, getY(comY))
    elif (getX(comX) > screen_x/2+screen_x/4) :
        mouse.move(getX(comX)+screen_x/20, getY(comY))
    elif (getY(comY) < screen_y/2-screen_y/4):
        mouse.move(getX(comX), getY(comY)-screen_y/20)
    elif (getY(comY) > screen_y/2+screen_y/4):
        mouse.move(getX(comX), getY(comY)+screen_y/20)
    else:
        mouse.move(getX(comX), getY(comY))
                
    

def click(): # Click the mouse
    mouse.click()