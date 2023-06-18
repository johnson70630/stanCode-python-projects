"""
File: blur.py
Name: Johnson
-------------------------------
This file shows the original image first,
smiley-face.png, and then compare to its
blurred image. The blur algorithm uses the
average RGB values of a pixel's nearest neighbors.
"""

from simpleimage import SimpleImage


def blur(img):
    """
    :param img: SimpleImage, Original picture
    :return new_img: SimpleImage, Blurred image
    Function: Blur the imported image
    Principle: Take the surrounding average value for each point and replace it back into the original RBG.
    """
    blurred = SimpleImage.blank(img.width, img.height)
    for x in range(img.width):
        for y in range(img.height):
            r_sum = 0
            g_sum = 0
            b_sum = 0
            count = 0
            for i in range(-1, 2, 1):
                for j in range(-1, 2, 1):
                    pixel_x = x+j
                    pixel_y = y+j
                    if 0 <= pixel_x < img.width:
                        if 0 <= pixel_y < img.height:
                            pixel = img.get_pixel(pixel_x, pixel_y)
                            r_sum += pixel.red
                            g_sum += pixel.green
                            b_sum += pixel.blue
                            count += 1
            new_img = blurred.get_pixel(x, y)
            new_img.red = r_sum/count
            new_img.green = g_sum/count
            new_img.blue = b_sum/count
    return blurred


def main():
    """
    Function: Blur the picture in 5 layers.
    Principle: Take the surrounding average value for each point and replace it back into the original RBG.
    """
    old_img = SimpleImage("images/smiley-face.png")
    old_img.show()

    blurred_img = blur(old_img)
    for i in range(5):
        blurred_img = blur(blurred_img)
    blurred_img.show()


# ---- DO NOT EDIT CODE BELOW THIS LINE ---- #

if __name__ == '__main__':
    main()
