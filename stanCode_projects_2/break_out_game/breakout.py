"""
stanCode Breakout Project
Adapted from Eric Roberts's Breakout by
Sonja Johnson-Yu, Kylie Jue, Nick Bowman,
and Jerry Liao.

YOUR DESCRIPTION HERE
"""

from campy.gui.events.timer import pause
from breakoutgraphics import BreakoutGraphics

FRAME_RATE = 10         # 100 frames per second
NUM_LIVES = 3	        # Number of attempts


def main():
    graphics = BreakoutGraphics()

    # Add the animation loop here!
    count = 0
    eliminated_bricks = 0
    while True:
        pause(FRAME_RATE)
        if graphics.clicked:
            dx = graphics.get_dx()
            dy = graphics.get_dy()
            while True:
                graphics.ball.move(dx, dy)
                pause(FRAME_RATE)
                for i in range(2):
                    for j in range(2):
                        is_object = graphics.window.get_object_at(graphics.ball.x + graphics.ball.width * i,
                                                                  graphics.ball.y + graphics.ball.height * j)
                        if is_object is not None:
                            if is_object.y > graphics.window.height/2:
                                dy = graphics.set_dy()
                                graphics.ball.move(dx, dy)
                                graphics.ball.move(dx, dy)
                                graphics.ball.move(dx, dy)
                            else:
                                dy = graphics.set_dy()
                                graphics.window.remove(is_object)
                                eliminated_bricks += 1
                                graphics.ball.move(dx, dy)
                if graphics.ball.x <= 0 or graphics.ball.x + graphics.ball.width >= graphics.window.width:
                    dx = graphics.set_dx()
                if graphics.ball.y <= 0:
                    dy = graphics.set_dy()
                if graphics.ball.y + graphics.ball.height >= graphics.window.height:
                    graphics.reset_ball()
                    count += 1
                    break
        if count == NUM_LIVES or eliminated_bricks == graphics.brick_amount:
            break


if __name__ == '__main__':
    main()
