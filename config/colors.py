import random
from neopixel import *

# Initialize random number generator
random.seed()

# Predefined colors
OFF         = Color(0,0,0)
WHITE       = Color(255,255,255)
RED         = Color(255,0,0)
GREEN       = Color(0,255,0)
BLUE        = Color(0,0,255)
PURPLE      = Color(128,0,128)
PINK        = Color(255,204,255)
YELLOW      = Color(255,255,0)
ORANGE      = Color(255,50,0)
TURQUOISE   = Color(64,224,208)
BROWN       = Color(165,42,42)

# Generate a random color
def generate_random_color():
    return Color(random.randint(0,255), random.randint(0,255), random.randint(0,255))

# Color sets
NAMED_COLORS = [WHITE, RED, GREEN, BLUE, PURPLE, YELLOW, ORANGE, TURQUOISE]

STRANGER_THINGS_COLOR_STRAND = [
    YELLOW, GREEN, RED, BLUE, ORANGE, TURQUOISE, GREEN, YELLOW, PURPLE, RED, 
    GREEN, BLUE, YELLOW, RED, TURQUOISE, GREEN, RED, BLUE, GREEN, ORANGE, 
    YELLOW, GREEN, RED, BLUE, ORANGE, TURQUOISE, RED, BLUE, ORANGE, RED, 
    YELLOW, GREEN, PURPLE, BLUE, YELLOW, ORANGE, TURQUOISE, RED, GREEN, YELLOW, 
    PURPLE, YELLOW, GREEN, RED, BLUE, ORANGE, TURQUOISE, GREEN, BLUE, ORANGE]

# RGB bitmasks
REDMASK = 0b111111110000000000000000
GREENMASK = 0b000000001111111100000000
BLUEMASK = 0b000000000000000011111111
