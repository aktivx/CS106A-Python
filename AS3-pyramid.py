"""
File: pyramid.py
----------------
ADD YOUR DESCRIPTION HERE
"""


import tkinter


CANVAS_WIDTH = 600      # Width of drawing canvas in pixels
CANVAS_HEIGHT = 300     # Height of drawing canvas in pixels

BRICK_WIDTH	= 30        # The width of each brick in pixels
BRICK_HEIGHT = 12       # The height of each brick in pixels
BRICKS_IN_BASE = 14     # The number of bricks in the base


def draw_brick(canvas, x, y, width, height):
    """
    ADD YOUR COMMENT
    """
    canvas.create_rectangle(x, y, x + width, y + height)



def draw_pyramid(canvas):
    """
    ADD YOUR COMMENT
    """
    # Your code goes here
    x_start = (CANVAS_WIDTH - (BRICKS_IN_BASE * BRICK_WIDTH)) / 2
    y_start = CANVAS_HEIGHT - BRICK_HEIGHT
    x = x_start
    y = y_start
    for i in range(BRICKS_IN_BASE, 0, -1):
        for a in range(i, 0 , -1):
            draw_brick(canvas, x, y, BRICK_WIDTH, BRICK_HEIGHT)
            x += BRICK_WIDTH

        x = x_start + (BRICK_WIDTH / 2) * (BRICKS_IN_BASE - i + 1)
        y -= BRICK_HEIGHT





######## DO NOT MODIFY ANY CODE BELOW THIS LINE ###########

# This function is provided to you and should not be modified.
# It creates a window that contains a drawing canvas that you
# will use to make your drawings.
def make_canvas(width, height):
    """
    DO NOT MODIFY
    Creates and returns a drawing canvas
    of the given int size with a blue border,
    ready for drawing.
    """
    top = tkinter.Tk()
    top.minsize(width=width + 10, height=height + 10)
    top.title('pyramid')
    canvas = tkinter.Canvas(top, width=width + 1, height=height + 1)
    canvas.pack()
    canvas.xview_scroll(8, 'units')  # This is so (0, 0) works correctly,
    canvas.yview_scroll(8, 'units')  # otherwise it's clipped off

    # Draw blue boundary line at bottom of canvas
    canvas.create_line(0, height, width, height, width=1, fill='blue')

    return canvas


def main():
    """
    This program, when completed, displays a pyramid graphically.
    """
    canvas = make_canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    draw_pyramid(canvas)
    tkinter.mainloop()


if __name__ == '__main__':
    main()
