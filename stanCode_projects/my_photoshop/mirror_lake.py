"""
File: mirror_lake.py
Name: Johnson
----------------------------------
This file reads in mt-rainier.jpg and
makes a new image that creates a mirror
lake vibe by placing an inverse image of
mt-rainier.jpg below the original one.
"""
from simpleimage import SimpleImage


def reflect(filename):
    """
    :param filename: str, the file path of the original image
    :return r_img: SimpleImage, the image with mirrored lake
    """
    img = SimpleImage(filename)
    r_img = SimpleImage.blank(img.width, img.height*2)
    for x in range(img.width):
        for y in range(img.height):
            colored_p = img.get_pixel(x, y)

            blank1 = r_img.get_pixel(x, y)
            blank2 = r_img.get_pixel(x, r_img.height-1-y)

            blank1.red = colored_p.red
            blank1.green = colored_p.green
            blank1.blue = colored_p.blue

            blank2.red = colored_p.red
            blank2.green = colored_p.green
            blank2.blue = colored_p.blue
    return r_img


def main():
    """
    The file contains a image processing algorithms:
    reflect
    """
    original_mt = SimpleImage('images/mt-rainier.jpg')
    original_mt.show()
    reflected = reflect('images/mt-rainier.jpg')
    reflected.show()


# DO NOT EDIT CODE BELOW THIS LINE #

if __name__ == '__main__':
    main()
