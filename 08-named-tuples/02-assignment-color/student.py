from collections import namedtuple
Color = namedtuple('Color', ['r', 'g', 'b'])

def valid_color(color):
    # Check if each color component is between 0 and 255
    return 0 <= color.r <= 255 and 0 <= color.g <= 255 and 0 <= color.b <= 255

def clamp_color(color):
    # Clamp each component between 0 and 255
    clamped_r = min(255, max(0, color.r))
    clamped_g = min(255, max(0, color.g))
    clamped_b = min(255, max(0, color.b))
    # Return a new Color with clamped values
    return Color(clamped_r, clamped_g, clamped_b)
