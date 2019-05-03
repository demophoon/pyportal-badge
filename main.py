import os
import random
import board
import time


from adafruit_pyportal import PyPortal

pyportal = PyPortal(status_neopixel=board.NEOPIXEL, default_bg="/badge.bmp")
calypso_imgs = []

reset_active = False


def shuffle(l):
    """
    Return a randomly shuffled list given an ordered list.
    """
    final_list = []
    for _ in l:
        final_list.append(l.pop(random.randrange(0, len(l))))
    return final_list


def in_region(region, point):
    """
    Detect if a point exists in a region.

    Region: (x, y, width, height)
    Point: (x, y)

    Returns True or False depending on if the point exists in the region.
    """
    rx, ry, rw, rh = region
    x, y = point

    return (
        x > rx and x < rx + rw and
        y > ry and y < ry + rh
    )

def main_screen():
    """
    Reset PyPortal background to primary screen
    """
    pyportal.set_background('badge.bmp')


def show_twitter():
    """
    Show twitter contact information.
    """
    pyportal.set_background('twitter.bmp')


def show_contact():
    """
    Show contact information.
    """
    pyportal.set_background('contact.bmp')


def show_calypso():
    """
    Randomly pick a picture of your good good kitty and show it on the screen!
    :3
    """
    global calypso_imgs
    if len(calypso_imgs) == 0:
        calypso_imgs = shuffle(os.listdir('/calypso'))
    img = calypso_imgs.pop()
    pyportal.set_background('/calypso/{}'.format(img))


touchpoints = {
    'twitter': {
        'region': (180, 65, 131, 51),
        'action': show_twitter,
    },
    'contact': {
        'region': (180, 122, 131, 51),
        'action': show_contact,
    },
    'calypso': {
        'region': (180, 180, 131, 51),
        'action': show_calypso,
    },
}

# main loop
while True:
    touch = pyportal.touchscreen.touch_point
    if touch:
        if reset_active:
            reset_active = False
            main_screen()
        for k, touchpoint in touchpoints.items():
            if in_region(touchpoint['region'], (touch[0], touch[1])):
                reset_active = True
                touchpoint['action']()

        # Wait for no touch event to stop duplicate touchs
        while pyportal.touchscreen.touch_point:
            time.sleep(0.3)
