from pynput.keyboard import Key, Controller

keyboard: Controller = Controller()


def execute_forward():
	msg = "GOING FORWARD!!!"
	print(msg)
	keyboard.press('w')


def execute_backward():
	msg = "GOING BACKWARD!!!"
	print(msg)
	keyboard.press('s')


def execute_left():
	msg = "GOING LEFT!!!"
	print(msg)
	keyboard.press(Key.left)


def execute_right():
	msg = "GOING RIGHT!!!"
	print(msg)
	keyboard.press(Key.right)

def execute_up():
	msg = "GOING UP!!!"
	print(msg)
	keyboard.press(Key.up)


def execute_down():
	msg = "GOING DOWN!!!"
	print(msg)
	keyboard.press(Key.down)


import sys

print(sys.argv)
command = sys.argv[1]

command_fun = {
	'up': execute_up,
	'down': execute_down,
	'right': execute_right,
	'left': execute_left,
	'forward': execute_forward,
	'backward': execute_backward
}

command_fun[command]()
