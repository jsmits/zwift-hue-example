# some example code

from phue import Bridge

host = '192.168.1.178'
b = Bridge(host)
b.connect()

data = b.get_api()
light_names = b.get_light_objects('name')

light_names['Werkkamer'].hue = 65500
light_names['Werkkamer'].on = False
light_names['Werkkamer'].on = True

import random
import time

for i in range(1000):
    light_names['Werkkamer'].xy = [random.random(),random.random()]
    time.sleep(0.2)
    
