import mouse
import screeninfo as si

screen_x = (si.get_monitors()[0].width)
screen_y = (si.get_monitors()[0].height)

common_x = [0, 0, 0] # List of x coordinates
common_y = [0, 0, 0] # List of y coordinates

def getCommon(x, y): # Get the common x and y coordinates
    common_x.append(x) # Add the x coordinate to the list
    common_y.append(y) # Add the y coordinate to the list
    common_x.pop(0) # Remove the first element of the x list
    common_y.pop(0) # Remove the first element of the y list
    return (sum(common_x) / len(common_x), sum(common_y) / len(common_y)) # Return the average of the x and y coordinates

def getX(c): # Get the x coordinate
    c = c*2-1
    c = c*1.8
    c = (c+1)/2
    return screen_x * c

def getY(c): # Get the y coordinate
    c = c*2-1
    c = c*1.8
    c = (c+1)/2
    return screen_y * c

def move(x, y):
    comX, comY = getCommon(x, y)
    mouse.move(getX(comX), getY(comY))

def click(): # Click the mouse
    mouse.click()