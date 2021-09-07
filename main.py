import random
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
    # Hide the turtle and its lines
    turtle.hideturtle()
    turtle.penup()
    # Calculate starting coordinates
    dot_total_pixels = dot_size + dot_spacing
    starting_x = (dots_per_row/2) * dot_total_pixels * -1
    starting_y = (row_count/2) * dot_total_pixels
    # Move the turtle to every coordinate and draw a dot:
    curr_y = starting_y
    for row in range(row_count):
        curr_x = starting_x
        for dot in range(dots_per_row):
            turtle.setposition(curr_x, curr_y)
            turtle.dot(dot_size, random.choice(color_bank))
            curr_x += dot_total_pixels
        curr_y -= dot_total_pixels
    return


# Extract colors from desired image
colors = extract_colors('sisyphus.jpg', 10)
print(colors)

# Create Turtle and Screen
timmy = Turtle()
my_screen = timmy.getscreen()

# Adjust turtle/screen settings
my_screen.colormode(255)
timmy.speed(0)

# Draw painting
draw_spot_painting(timmy, colors)

# Exit program on click
my_screen.exitonclick()
