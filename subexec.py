import threading

from pynput.keyboard import Key, Controller
import datetime
import time
keyboard: Controller = Controller()



def execute_key(key):
	tiemstamp = datetime.datetime.now()
	wait = 20
	while True:
		keyboard.press(key)
		time.sleep(0.2)
		keyboard.release(key)
		if (datetime.datetime.now() - tiemstamp).total_seconds() > wait:
			break




import sys

print(sys.argv)
command = sys.argv[1]

command_fun = {
	'up': Key.up,
	'down': Key.down,
	'right': Key.right,
	'left': Key.left,
	'forward': 'w',
	'backward': 's'
}

execute_key(command_fun[command])
