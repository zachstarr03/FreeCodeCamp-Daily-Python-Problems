# 3/07:

""" Directions: Given a window size, the width of an element in viewport width "vw" units, and the height of an element in viewport height "vh" units, determine the size of the element in pixels.

The given window size and returned element size are strings in the format "width x height", "1200 x 800" for example.

"vw" units are the percent of window width. "50vw" for example, is 50% of the width of the window.

"vh" units are the percent of window height. "50vh" for example, is 50% of the height of the window.
"""

""" Time Complexity: O(1) -> as each operation runs in constant time since the parameters are tiny and fixed 
Space Complexity: O(1) -> .split() creates a small list which are always the same size, regardless of input, so memory is not growing with input size 
"""

''' O(1) time complexity, O(1) space complexity '''
def get_element_size(window_size, element_vw, element_vh):

    # split window_size to get width and height, type cast to int
    width = int(window_size.split(" ")[0])
    height = int(window_size.split(" ")[2])

    # split element_vw and element_vh, type cast to int
    vw = int(element_vw.split("v")[0])
    vh = int(element_vh.split("v")[0])

    # Divide by 100 to convert the percentage to a decimal
    vw = vw / 100
    vh = vh / 100

    # Calculate the new window size
    new_window_size_width = int(width * vw)
    new_window_size_height = int(height * vh)

    # type cast to str for return format
    new_window_size_width_str = str(new_window_size_width)
    new_window_size_height_str = str(new_window_size_height)

    # full string
    new_window_size = new_window_size_width_str + " x " + new_window_size_height_str

    return new_window_size

if __name__ == "__main__":
    print(get_element_size("1200 x 800", "50vw", "50vh"))       # 600 x 400
    print(get_element_size("320 x 480", "25vw", "50vh"))        # 80 x 240
    print(get_element_size("1000 x 500", "7vw", "3vh"))         # 70 x 5
    print(get_element_size("1920 x 1080", "95vw", "100vh"))     # 1824 x 1080
    print(get_element_size("1200 x 800", "0vw", "0vh"))         # 0 x 0
    print(get_element_size("1440 x 900", "100vw", "114vh"))     # 1440 x 1026

"""
''' I didn't use an LLM at all for help throughout the problem '''

''' Optimal solution from ChatGPT: '''
def get_element_size(window_size, element_vw, element_vh):

    width, _, height = window_size.split()
    width = int(width)
    height = int(height)

    vw = int(element_vw[:-2]) / 100
    vh = int(element_vh[:-2]) / 100

    element_width = int(width * vw)
    element_height = int(height * vh)

    return f"{element_width} x {element_height}"
"""