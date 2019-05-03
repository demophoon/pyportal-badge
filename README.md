Adafruit PyPortal Badge
=======================

I got tired of fumbling around with my business cards at conferences so I
decided to create an interactive digital business card instead!

![Image of digital business card](https://brittg.com/u/iChz0.png)

This code should get you up and running with a copy of my business card. Feel
free to change up the images if you use this out in the wild!

Installation
------------

Make sure you have a PyPortal and have a recent build of CircuitPython. You can
follow the guide over on Adafruit.

https://learn.adafruit.com/adafruit-pyportal/updating-your-pyportal

Plug your PyPortal into your computer and copy the contents of this repo onto
the CIRCUITPYTHON drive that shows up and your PyPortal will automatically
restart and run the code in main.py.

Customization
-------------

Add buttons to your UI by adding new bounding boxes to the global `touchpoints`
dict.

```python
touchpoints = {
  # ...
  'cat_photo': {
    'region': (x_coord, y_coord, box_width, box_height),
    'action': function_to_be_called,
  },
  # ...
}
```
