import mouse
import screeninfo as si

screen_x = si.get_monitors()[0].width
screen_y = si.get_monitors()[0].height

common_x = [0, 0, 0] # List of x coordinates
common_y = [0, 0, 0] # List of y coordinates

def getCommon(x, y):
    common_x.append(x)
    common_y.append(y)
    common_x.pop(0)
    common_y.pop(0)
    return (sum(common_x) / len(common_x), sum(common_y) / len(common_y))

def getX(c):
    if (screen_x * c) > screen_x:
        return screen_x
    if (screen_x * c) < 0:
        return 0
    return screen_x * c

def getY(c):
    if (screen_y * c) > screen_y:
        return screen_y
    if (screen_y * c) < 0:
        return 0
    return screen_y * c

def move(x, y):
    comX, comY = getCommon(x, y)
    mouse.move(getX(comX), getY(comY))

def click():
    mouse.click()