"""
Given an array, colors, which contains a combination of the following three
elements:

* 0 (representing red)
* 1 (representing white)
* 2 (representing blue)

Sort the array in place so that the elements of the same color are adjacent,
with the colors in the order of red, white, and blue.

"""


def sort_colors(colors):
    red, white, blue = 0, 0, len(colors) - 1
    while white <= blue:
        if colors[white] == 0:
            colors[red], colors[white] = colors[white], colors[red]
            red += 1
            white += 1
        elif colors[white] == 1:
            white += 1
        elif colors[white] == 2:
            colors[white], colors[blue] = colors[blue], colors[white]
            blue -= 1
    return colors
