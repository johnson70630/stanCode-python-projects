"""
File: my_drawing.py
Name: Johnson
----------------------
This program shows a picture "Feels Bad Man."
"""

from campy.graphics.gobjects import GOval, GArc
from campy.graphics.gwindow import GWindow


def main():
    """
    Title: Feels Bad Man

    This is a famous meme expressing bad feelings :(
    """
    window = GWindow(500, 500)

    clothe = GOval(500, 200)
    clothe.filled = True
    clothe.fill_color = 'blue'
    window.add(clothe, -100, 400)

    face = GOval(450, 350)
    face.filled = True
    face.fill_color = 'olivedrab'
    window.add(face, 10, 120)

    right_ear = GArc(250, 700, 0, 180)
    right_ear.filled = True
    right_ear.fill_color = 'olivedrab'
    window.add(right_ear, 220, 10)

    left_ear = GArc(250, 700, 0, 180)
    left_ear.filled = True
    left_ear.fill_color = 'olivedrab'
    window.add(left_ear, 70, 10)

    right_eyelid = GOval(220, 180)
    right_eyelid.filled = True
    right_eyelid.fill_color = 'olivedrab'
    window.add(right_eyelid, 280, 60)

    left_eyelid = GOval(220, 180)
    left_eyelid.filled = True
    left_eyelid.fill_color = 'olivedrab'
    window.add(left_eyelid, 130, 60)

    right_eye = GOval(150, 70)
    right_eye.filled = True
    right_eye.fill_color = 'white'
    window.add(right_eye, 350, 130)

    left_eye = GOval(150, 70)
    left_eye.filled = True
    left_eye.fill_color = 'white'
    window.add(left_eye, 200, 130)

    right_eyeball = GOval(80, 70)
    right_eyeball.filled = True
    right_eyeball.fill_color = 'black'
    window.add(right_eyeball, 390, 130)

    left_eyeball = GOval(80, 70)
    left_eyeball.filled = True
    left_eyeball.fill_color = 'black'
    window.add(left_eyeball, 240, 130)

    right_eyelash = GArc(150, 130, 0, 190)
    window.add(right_eyelash, 350, 100)

    left_eyelash = GArc(160, 130, 0, 210)
    window.add(left_eyelash, 185, 100)

    right_eye_bag = GArc(180, 200, 180, 100)
    window.add(right_eye_bag, 340, 180)

    left_eye_bag = GArc(200, 200, 270, 90)
    window.add(left_eye_bag, 210, 180)

    upper_lip = GArc(300, 100, 0, 180)
    upper_lip.filled = True
    upper_lip.fill_color = 'brown'
    window.add(upper_lip, 150, 350)

    lower_lip = GArc(300, 100, 180, 180)
    lower_lip.filled = True
    lower_lip.fill_color = 'brown'
    window.add(lower_lip, 150, 350)

    corner_mouth = GArc(170, 130, 160, 110)
    window.add(corner_mouth, 130, 330)

    right_tears1 = GOval(15, 50)
    right_tears1.filled = True
    right_tears1.fill_color = 'deepskyblue'
    window.add(right_tears1, 450, 200)

    right_tears2 = GOval(15, 50)
    right_tears2.filled = True
    right_tears2.fill_color = 'deepskyblue'
    window.add(right_tears2, 450, 260)

    right_tears3 = GOval(15, 50)
    right_tears3.filled = True
    right_tears3.fill_color = 'deepskyblue'
    window.add(right_tears3, 450, 320)

    left_tears1 = GOval(15, 50)
    left_tears1.filled = True
    left_tears1.fill_color = 'deepskyblue'
    window.add(left_tears1, 230, 200)

    left_tears2 = GOval(15, 50)
    left_tears2.filled = True
    left_tears2.fill_color = 'deepskyblue'
    window.add(left_tears2, 230, 260)

    left_tears3 = GOval(15, 50)
    left_tears3.filled = True
    left_tears3.fill_color = 'deepskyblue'
    window.add(left_tears3, 230, 320)


if __name__ == '__main__':
    main()
