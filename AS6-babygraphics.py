"""
File: babygraphics.py
---------------------
Add your comments here
"""

import tkinter
import babynames
import babygraphicsgui as gui


# Provided constants to load and draw the baby data
FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 600

YEARS = [1900, 1910, 1920, 1930, 1940, 1950, 1960, 1970, 1980, 1990, 2000, 2010]
SPACE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000
GRAPH_MARGIN_SIZE = 20

def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index of the current year in the YEARS list
    Returns:
        x_coordinate (float): The x coordinate of the vertical line associated
                              with the specified year.
    >>> round(get_x_coordinate(1000, 0), 1)
    20.0
    >>> round(get_x_coordinate(1000, 2), 1)
    180.0
    >>> round(get_x_coordinate(1000, 11), 1)
    900.0
    """
    year_graph_width = (width - 2 * GRAPH_MARGIN_SIZE) / len(YEARS)
    x = GRAPH_MARGIN_SIZE + year_index * year_graph_width
    return x

def draw_fixed_lines(canvas):
    """
    Erases all existing information on the given canvas and then
    draws the fixed background lines on it.

    Input:
        canvas (tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')            # delete all existing lines from the canvas
    width = canvas.winfo_width()    # get the width of the canvas
    height = canvas.winfo_height()  # get the height of the canvas
    y1 = height - GRAPH_MARGIN_SIZE
    y2 = GRAPH_MARGIN_SIZE
    canvas.create_line(GRAPH_MARGIN_SIZE, y2, width - GRAPH_MARGIN_SIZE, y2 )
    canvas.create_line(GRAPH_MARGIN_SIZE, y1, width - GRAPH_MARGIN_SIZE, y1 )


    for i in range(len(YEARS)):
        x = get_x_coordinate(width, i)
        canvas.create_line(x, height, x, 0)
        canvas.create_text(x + TEXT_DX, y1, anchor = 'nw', text = YEARS[i])


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dictionary of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (tkinter Canvas): The canvas on which we are drawing.
        name_data (dictionary): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot
    """
    draw_fixed_lines(canvas)
    width = canvas.winfo_width()
    height = canvas.winfo_height()
    # add your code here

    color_counter = 0
    y_delta_rank = (height - 2 * GRAPH_MARGIN_SIZE) / (MAX_RANK - 1)

    for name in lookup_names:
        color = COLORS[color_counter % len(COLORS)]
        dict_year_rank = name_data[name]

        x1 = get_x_coordinate(width, 0)

        for i in range(len(YEARS)):
            if YEARS[i] in dict_year_rank:
                rank = dict_year_rank[YEARS[i]]
            else:
                rank = MAX_RANK

            x2 = get_x_coordinate(width, i)


            if x2 == x1:
                y1 = GRAPH_MARGIN_SIZE + (rank - 1) * y_delta_rank

            y2 = GRAPH_MARGIN_SIZE + (rank - 1) * y_delta_rank

            if x1 != x2:

                canvas.create_line(x1, y1, x2, y2, width = LINE_WIDTH, fill = color)

            if rank == MAX_RANK:
                name_rank = name + '*'
            else:
                name_rank = name + ' ' + str(rank)

            canvas.create_text(x2 + TEXT_DX, y2, anchor = 'sw', text = name_rank, fill = color)
            x1 = x2
            y1 = y2
        color_counter += 1


















# main() code is provided for you
def main():
    import sys
    args = sys.argv[1:]
    global WINDOW_WIDTH
    global WINDOW_HEIGHT
    if len(args) == 2:
        WINDOW_WIDTH = int(args[0])
        WINDOW_HEIGHT = int(args[1])
    else:
        WINDOW_WIDTH = 1000
        WINDOW_HEIGHT = 600
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Make window
    top = tkinter.Tk()
    top.wm_title('Baby Names Solution')
    canvas = gui.make_gui(top, WINDOW_WIDTH, WINDOW_HEIGHT, name_data, draw_names, babynames.search_names)

    # draw_fixed once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This needs to be called just once
    top.mainloop()


if __name__ == '__main__':
    main()
