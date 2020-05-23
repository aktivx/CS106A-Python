import tkinter

FRIENDS_FILE = 'users.txt'
COORDINATES_FILE = 'coords.txt'


def main():
    canvas = make_canvas(800, 800)
    draw_friend_graph(canvas, FRIENDS_FILE, COORDINATES_FILE)
    canvas.mainloop()


def draw_friend_graph(canvas, friends_file, coordinates_file):

    with open(coordinates_file) as f:
        coordinates_dic = {}
        for line in f:
            line = line.strip()
            line = line.split(': ')
            coordinates_dic[line[0]] = line[1].split(', ')

    for name in coordinates_dic:
        coordinates_list = coordinates_dic[name]
        x = int(coordinates_list[0])
        y = int(coordinates_list[1])
        x1 = int(coordinates_list[0]) + 10
        y1 = int(coordinates_list[1]) + 10
        canvas.create_oval(x, y, x1, y1, outline='red')
        canvas.create_text(x, y, anchor='w', text=name)

    with open(friends_file) as f:
        friends_dic = {}
        for line in f:
            line = line.strip()
            line = line.split(': ')
            friends_dic[line[0]] = line[1].split(', ')


    for name in friends_dic:
        coordinates_list = coordinates_dic[name]
        x = int(coordinates_list[0])
        y = int(coordinates_list[1])
        following_list = friends_dic[name]

        for name_following in following_list:
            coordinates_list = coordinates_dic[name_following]
            x1 = int(coordinates_list[0])
            y1 = int(coordinates_list[1])

            canvas.create_line(x, y, x1, y1, arrow='last', fill='red')


    # canvas.create_line(0, 0, 0, height - 1, width=1, fill='blue')




# provided function, this code is complete (Nick's Code from lecture for make_canvas)
def make_canvas(width, height):
    """
    Creates and returns a drawing canvas
    of the given int size with a blue border,
    ready for drawing.
    """
    top = tkinter.Tk()
    top.minsize(width=width + 10, height=height + 10)

    canvas = tkinter.Canvas(top, width=width, height=height)
    canvas.pack()
    canvas.xview_scroll(6, "units")  # hack so (0, 0) works correctly
    canvas.yview_scroll(6, "units")

    # draw blue boundaries - sides
    canvas.create_line(0, 0, 0, height-1, width=1, fill='blue')
    canvas.create_line(width-1, 0, width-1, height-1, width=1, fill='blue')
    # top bottom
    canvas.create_line(0, 0, width - 1, 0, width=1, fill='blue')
    canvas.create_line(0, height - 1, width - 1,
                       height - 1, width=1, fill='blue')

    return canvas


if __name__ == "__main__":
    main()
