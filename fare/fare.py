from pynput.mouse import Button, Controller
import random
import time
import sys


def move(timeout_min):
    mouse = Controller()
    print('The current pointer position is {0}'.format(mouse.position))
    timeout = time.time() + 60*timeout_min
    print('{0} sec'.format(60*timeout_min))

    while time.time() <= timeout:
        # Set pointer position
        x = random.randint(5,1000)
        y = random.randint(5,1000)
        mouse.position = (x, y)

        print('Now we have moved it to {0}'.format(mouse.position))
        time.sleep(45)


if __name__ == "__main__":
    min = int(sys.argv[1])
    move(min)
