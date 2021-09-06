import colorgram


def extract_colors(source, count):
    """
    Extracts colors from a source image and formats each color as (r, g, b). Returns a list of such colors.
    :param source: string
    :param count: int
    :return: []
    """
    extracted_colors = colorgram.extract(source, count)
    colors = []
    for color in extracted_colors:
        # Reformat the current color as a tuple (r, g, b)
        rgb = color.rgb
        r = rgb[0]
        g = rgb[1]
        b = rgb[2]
        rgb = (r, g, b)
        # Add the reformatted color to 'colors'
        colors.append(rgb)
    return colors


colors = extract_colors('img.jpg', 10)
print(colors)