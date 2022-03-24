import arcade as ar
from settings import *
from sprites import *


class Game(ar.Window):
    """
    Main game loop
    The entire game is ran with this class
    """
    def __init__(self):
        """Initilizes game loop and sprites"""
        super().__init__(WIDTH, HEIGHT, TITLE, fullscreen=FULLSCREEN)

        self.player = Player()

    def on_draw(self):
        """Draws all game graphics on the screen"""
        ar.start_render()

        if EPILEPSY: ar.set_background_color(choice(COLORS))
        else: ar.set_background_color(BG_COLOR)

        self.draw_grid()

        self.player.draw()

    def on_update(self, delta_time):
        """Game logic and movement"""
        self.player.update(delta_time)

    def on_key_press(self, key, modifiers):
        """"""
        self.player.key("press", key, modifiers)
        
        if key == ar.key.ESCAPE: 
            ar.close_window() # Closes the game

    def on_key_release(self, key, modifiers):
        """"""
        self.player.key("release", key, modifiers)

    def draw_grid(self):
        """Draws a grid on screen using the tilesize"""
        if EPILEPSY: grid_color = choice(COLORS)
        else: grid_color = GREEN

        for x in range(0, WIDTH, TILESIZE):
            ar.draw_lines([(x, 0), (x, HEIGHT)], grid_color)

        for y in range(0, HEIGHT, TILESIZE):
            ar.draw_lines([(0, y), (WIDTH, y)], grid_color)








