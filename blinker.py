
seconds = 1
minutes = 60

blinkEvery = 12 * seconds
blinkFor = 0.1 * seconds
pauseAfter = 20 * minutes
pauseAtLeastFor = 10 * seconds

import os
import platform
import time
from pynput.mouse import Listener

def darken():
	if platform.system() == "Linux":
		os.system("redshift -O 3000 -b 0.1")

def brighten():
	if platform.system() == "Linux":
		os.system("redshift -O 3000 -b 0.8")

movedMouse = False
def on_move(x, y):
	global movedMouse
	movedMouse = True
Listener(on_move=on_move).start()

while True:
	brighten()
	tStartWork = time.time()
	while time.time() < tStartWork + pauseAfter:
		brighten()
		time.sleep(blinkEvery - blinkFor)
		darken()
		time.sleep(blinkFor)
	darken()
	time.sleep(pauseAtLeastFor)
	movedMouse = False
	while not movedMouse:
		time.sleep(0.1)
