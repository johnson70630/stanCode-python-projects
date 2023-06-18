"""
File: drawing_line.py
Name: Johnson
-------------------------
This program creates lines on an instance of GWindow class.
There is a circle indicating the user’s first click. A line appears
at the condition where the circle disappears as the user clicks
on the canvas for the second time.
"""

from campy.graphics.gobjects import GOval, GLine
from campy.graphics.gwindow import GWindow
from campy.gui.events.mouse import onmouseclicked

# This constant controls the size of the GOval
SIZE = 10
# Global Variable
window = GWindow()
point = GOval(SIZE, SIZE)
odd = True


def main():
    """
    This program creates lines on an instance of GWindow class.
    There is a circle indicating the user’s first click. A line appears
    at the condition where the circle disappears as the user clicks
    on the canvas for the second time.
    """
    onmouseclicked(draw)


def draw(mouse):
    global odd
    if odd:
        window.add(point, x=mouse.x-SIZE/2, y=mouse.y-SIZE/2)
        odd = False
    else:
        line = GLine(point.x + SIZE/2, point.y + SIZE/2, mouse.x, mouse.y)
        window.add(line)
        window.remove(point)
        odd = True


if __name__ == "__main__":
    main()
