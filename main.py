import colorgram
from turtle import Turtle, Screen


def extract_colors(source, count):
    """
    Extracts colors from a source image and formats each color as (r, g, b). Returns a list of such colors.
    :param source: string
    :param count: int
    :return: []
    """
    extracted_colors = colorgram.extract(source, count)
    final_colors = []
    for color in extracted_colors:
        # Reformat the current color as a tuple (r, g, b)
        rgb = color.rgb
        r = rgb[0]
        g = rgb[1]
        b = rgb[2]
        rgb = (r, g, b)
        # Add the reformatted color to 'colors'
        final_colors.append(rgb)
    return final_colors


def draw_spot_painting(turtle, color_bank, row_count=10, dots_per_row=10, dot_size=25, dot_spacing=50):
    """
    Draws a 10x10 spot painting with dots of size 25, set 50 paces apart.
    Color will be randomly selected from color_bank.
    """
    # Calculate starting coordinate
    painting_width = dots_per_row * (dot_size + dot_spacing)
    painting_height = row_count * (dot_size + dot_spacing)
    starting_x = painting_width/-2.0
    starting_y = painting_height/2.0
    # Iterate through every coordinate and draw a dot:
    curr_x = starting_x
    curr_y = starting_y
    turtle.penup()
    for row in range(row_count):
        for dot in range(dots_per_row):
            turtle.dot(dot_size, 'black')
            turtle.setposition(curr_x, curr_y)
            curr_x += (dot_size + dot_spacing)

colors = extract_colors('img.jpg', 10)
print(colors)

# Create turtle and screen
timmy = Turtle()
my_screen = timmy.getscreen()

# Adjust turtle/screen settings
my_screen.colormode(255)
timmy.speed(0)

# Draw painting
draw_spot_painting(timmy, colors)

# Exit program on click
my_screen.exitonclick()
