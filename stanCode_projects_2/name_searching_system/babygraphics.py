"""
File: babygraphics.py
Name: Johnson
--------------------------------
SC101 Baby Names Project
Adapted from Nick Parlante's Baby Names assignment by
Jerry Liao.
"""

import tkinter
import babynames
import babygraphicsgui as gui

FILENAMES = [
    'data/full/baby-1900.txt', 'data/full/baby-1910.txt',
    'data/full/baby-1920.txt', 'data/full/baby-1930.txt',
    'data/full/baby-1940.txt', 'data/full/baby-1950.txt',
    'data/full/baby-1960.txt', 'data/full/baby-1970.txt',
    'data/full/baby-1980.txt', 'data/full/baby-1990.txt',
    'data/full/baby-2000.txt', 'data/full/baby-2010.txt'
]
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 600
YEARS = [1900, 1910, 1920, 1930, 1940, 1950,
         1960, 1970, 1980, 1990, 2000, 2010]
GRAPH_MARGIN_SIZE = 20
COLORS = ['red', 'purple', 'green', 'blue']
TEXT_DX = 2
LINE_WIDTH = 2
MAX_RANK = 1000


def get_x_coordinate(width, year_index):
    """
    Given the width of the canvas and the index of the current year
    in the YEARS list, returns the x coordinate of the vertical
    line associated with that year.

    Input:
        width (int): The width of the canvas
        year_index (int): The index where the current year is in the YEARS list
    Returns:
        x_coordinate (int): The x coordinate of the vertical line associated
                            with the current year.
    """
    x_coordinate = GRAPH_MARGIN_SIZE + year_index*(width-2*GRAPH_MARGIN_SIZE)/len(YEARS)
    return x_coordinate


def get_y_coordinate(height, rank):
    """
    Given the height of the canvas and the index of the current rank
    in the name_data dic, returns the y coordinate of the line associated with that rank.

    Input:
        height (int): The height of the canvas
        rank (str): The index where the current rank is in the name_data dic
    Returns:
        y_coordinate (int): The y coordinate of the line associated
                            with the current rank.
    """
    y_coordinate = GRAPH_MARGIN_SIZE+(height-2*GRAPH_MARGIN_SIZE)/MAX_RANK*int(rank)
    return y_coordinate


def draw_fixed_lines(canvas):
    """
    Draws the fixed background lines on the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
    """
    canvas.delete('all')            # delete all existing lines from the canvas

    # ----- Write your code below this line ----- #
    canvas.create_line(GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE,
                       CANVAS_WIDTH-GRAPH_MARGIN_SIZE, GRAPH_MARGIN_SIZE,
                       width=LINE_WIDTH)
    canvas.create_line(GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE,
                       CANVAS_WIDTH-GRAPH_MARGIN_SIZE, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE,
                       width=LINE_WIDTH)
    n = 0
    for year in YEARS:
        x_coordinate = get_x_coordinate(CANVAS_WIDTH, n)
        canvas.create_line(x_coordinate, GRAPH_MARGIN_SIZE,
                           x_coordinate, CANVAS_HEIGHT,
                           width=LINE_WIDTH)
        canvas.create_text(x_coordinate+TEXT_DX, CANVAS_HEIGHT-GRAPH_MARGIN_SIZE+TEXT_DX,
                           text=year, anchor=tkinter.NW)
        n += 1


def draw_names(canvas, name_data, lookup_names):
    """
    Given a dict of baby name data and a list of name, plots
    the historical trend of those names onto the canvas.

    Input:
        canvas (Tkinter Canvas): The canvas on which we are drawing.
        name_data (dict): Dictionary holding baby name data
        lookup_names (List[str]): A list of names whose data you want to plot

    Returns:
        This function does not return any value.
    """
    draw_fixed_lines(canvas)        # draw the fixed background grid

    # ----- Write your code below this line ----- #
    color = 0
    for name in lookup_names:
        n = 0
        for year in YEARS[:len(YEARS)-1]:
            if str(year) in name_data[name]:
                rank = name_data[name][str(year)]
                x_coordinate = get_x_coordinate(CANVAS_WIDTH, n)
                y_coordinate = get_y_coordinate(CANVAS_HEIGHT, rank)
            else:
                rank = '*'
                x_coordinate = get_x_coordinate(CANVAS_WIDTH, n)
                y_coordinate = CANVAS_HEIGHT-GRAPH_MARGIN_SIZE
            if str(YEARS[n+1]) in name_data[name]:
                next_rank = name_data[name][str(YEARS[n+1])]
                next_x = get_x_coordinate(CANVAS_WIDTH, n+1)
                next_y = get_y_coordinate(CANVAS_HEIGHT, next_rank)
            else:
                rank = '*'
                next_x = get_x_coordinate(CANVAS_WIDTH, n+1)
                next_y = CANVAS_HEIGHT-GRAPH_MARGIN_SIZE
            canvas.create_line(x_coordinate, y_coordinate, next_x, next_y
                               , width=LINE_WIDTH, fill=COLORS[color])
            canvas.create_text(x_coordinate+TEXT_DX, y_coordinate,
                               text=(name, rank), anchor=tkinter.SW, fill=COLORS[color])
            n += 1
        if color == 3:
            color = 0
        else:
            color += 1


# main() code is provided, feel free to read through it but DO NOT MODIFY
def main():
    # Load data
    name_data = babynames.read_files(FILENAMES)

    # Create the window and the canvas
    top = tkinter.Tk()
    top.wm_title('Baby Names')
    canvas = gui.make_gui(top, CANVAS_WIDTH, CANVAS_HEIGHT, name_data, draw_names, babynames.search_names)

    # Call draw_fixed_lines() once at startup so we have the lines
    # even before the user types anything.
    draw_fixed_lines(canvas)

    # This line starts the graphical loop that is responsible for
    # processing user interactions and plotting data
    top.mainloop()


if __name__ == '__main__':
    main()
