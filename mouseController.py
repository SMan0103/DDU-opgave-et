import mouse
import screeninfo as si

screen_x = si.get_monitors()[0].width
screen_y = si.get_monitors()[0].height

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
    mouse.move(getX(x), getY(y))