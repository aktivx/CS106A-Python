import tkinter
import time

CANVAS_HEIGHT = 100
CANVAS_WIDTH = 500

DX = -4
DY = 0
DELAY = 0.01


def main():
    canvas = make_canvas(CANVAS_WIDTH, CANVAS_HEIGHT, "News Ticker")
    user_text_list = get_user_text()


    for i in user_text_list:
        text_to_scroll = canvas.create_text(CANVAS_WIDTH - 1, CANVAS_HEIGHT // 2, anchor='w', fill='black', text= i)
        full_scroll_text_once(canvas, text_to_scroll)

    canvas.mainloop()


def full_scroll_text_once(canvas, text_to_scroll):
    while get_right_x(canvas, text_to_scroll) > 0:
        canvas.move(text_to_scroll, DX, DY)
        canvas.update()
        time.sleep(DELAY)


def get_user_text():
    user_text_list = []
    user_text = input('Type a message here or press enter to finish:')
    while user_text:
        user_text_list.append(user_text)
        user_text = input('Type a message here or press enter to finish:')
    return user_text_list



"""
Youdon't need to modify code below here
"""


def get_right_x(canvas, object):
    bbox = canvas.bbox(object)
    return bbox[2]


def make_canvas(width, height, title):
    """
    Creates and returns a drawing canvas
    of the given int size with a blue border,
    ready for drawing.
    """
    top = tkinter.Tk()
    top.minsize(width=width, height=height)
    top.title(title)
    canvas = tkinter.Canvas(top, width=width + 1, height=height + 1)
    canvas.pack()
    return canvas


if __name__ == "__main__":
    main()
