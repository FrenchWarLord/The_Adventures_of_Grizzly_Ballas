import arcade.color as color 

# Colors

BLACK = color.BLACK
WHITE = color.WHITE
DARK_GREY = (65, 65, 65)
GREY = color.DAVY_GREY
LIGHT_GREY = color.BATTLESHIP_GREY

RED = color.RED

BLUE = color.BLUE
GREEN = color.GREEN

COLORS = [
    BLACK,
    WHITE,
    DARK_GREY,
    GREY,
    LIGHT_GREY,
    RED,
    BLUE,
    GREEN,
]

# Key modifiers
L_SHIFT = 1
L_ALT = 4



# Game Window

WIDTH = 1920
HEIGHT = 1080
TITLE = "Hello World!"

BG_COLOR = DARK_GREY

FULLSCREEN = True


# Game Settings

TILESIZE = 64  # Make sure this is a bit size (multiple of 8)

TITLE_HEIGHT = TILESIZE * HEIGHT
TITLE_WIDTH = TILESIZE * WIDTH

EPILEPSY = False


# Player Settings

PLAYER_SPEED = 300
PLAYER_SPEED_MODIFIER = 1.5


# Testing Mode

TESTING = False

if TESTING:
    WIDTH = int(1920 / 2)
    HEIGHT = int(1080 / 2)
    FULLSCREEN = False
