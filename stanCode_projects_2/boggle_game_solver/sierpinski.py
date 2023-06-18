"""
File: sierpinski.py
Name: Johnson
---------------------------
This file recursively prints the Sierpinski triangle on GWindow.
The Sierpinski triangle is a fractal described in 1915 by Waclaw Sierpinski.
It is a self similar structure that occurs at different levels of iterations.
"""

from campy.graphics.gwindow import GWindow
from campy.graphics.gobjects import GLine
from campy.gui.events.timer import pause

# Constants
ORDER = 6                  # Controls the order of Sierpinski Triangle
LENGTH = 600               # The length of order 1 Sierpinski Triangle
UPPER_LEFT_X = 150		   # The upper left x coordinate of order 1 Sierpinski Triangle
UPPER_LEFT_Y = 100         # The upper left y coordinate of order 1 Sierpinski Triangle
WINDOW_WIDTH = 950         # The width of the GWindow
WINDOW_HEIGHT = 700        # The height of the GWindow

# Global Variable
window = GWindow(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)  # The canvas to draw Sierpinski Triangle


def main():
	"""
	This function prints The Sierpinski triangle.
	"""
	sierpinski_triangle(ORDER, LENGTH, UPPER_LEFT_X, UPPER_LEFT_Y)


def sierpinski_triangle(order, length, upper_left_x, upper_left_y):
	"""
	:param order: int
	:param length: int
	:param upper_left_x: int
	:param upper_left_y: int
	:return:
	"""
	if order == 0:
		pass
	else:
		# upper left
		upper_left_side1 = GLine(upper_left_x, upper_left_y, upper_left_x + length, upper_left_y)
		upper_left_side2 = GLine(upper_left_x, upper_left_y, upper_left_x + length * 0.5, upper_left_y + length * 0.886)
		upper_left_side3 = GLine(upper_left_x + length, upper_left_y, upper_left_x + length * 0.5, upper_left_y + length * 0.886)
		window.add(upper_left_side1)
		window.add(upper_left_side2)
		window.add(upper_left_side3)
		sierpinski_triangle(order - 1, length / 2, upper_left_x, upper_left_y)
		sierpinski_triangle(order - 1, length / 2, upper_left_x + length * 0.5, upper_left_y)
		sierpinski_triangle(order - 1, length / 2, upper_left_x + length * 0.5/2, upper_left_y + length * 0.886/2)


if __name__ == '__main__':
	main()
