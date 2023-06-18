"""
File: fire.py
Name: Johnson
---------------------------------
This file contains a method called
highlight_fires which detects the
pixels that are recognized as fire
and highlights them for better observation.
"""
from simpleimage import SimpleImage


HURDLE_FACTOR = 1.05


def highlight_fires(filename):
    """
    :param filename: str, the file path of the original image
    :return fire: SimpleImage, the image with highlighted fires
    """
    fire = SimpleImage(filename)
    for pixel in fire:
        avg = (pixel.red+pixel.green+pixel.blue)/3
        if pixel.red > avg * HURDLE_FACTOR:
            pixel.red = 255
            pixel.green = 0
            pixel.blue = 0
        else:
            pixel.red = avg
            pixel.green = avg
            pixel.blue = avg
    return fire


def main():
    """
    The file contains a image processing algorithms:
    highlight_fires
    """
    original_fire = SimpleImage('images/greenland-fire.png')
    original_fire.show()
    highlighted_fire = highlight_fires('images/greenland-fire.png')
    highlighted_fire.show()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
