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

        self.player = Player(
            100, 100, RED, 300, 300, PLAYER_SPEED, PLAYER_SPEED_MODIFIER)

        self.other = Player(
            100, 100, GREEN, 500, 500, PLAYER_SPEED, PLAYER_SPEED_MODIFIER)

    def on_draw(self):
        """Draws all game graphics on the screen"""
        ar.start_render()

        self.player.draw()
        self.other.draw()

    def on_update(self, delta_time):
        """Game logic and movement"""
        self.player.update(delta_time)
        self.other.update(delta_time)

    def on_key_press(self, key, modifiers):
        """"""
        self.player.key("press", key, modifiers)
        self.other.key("press", key, modifiers)
        
        if key == ar.key.ESCAPE: 
            ar.close_window() # Closes the game

    def on_key_release(self, key, modifiers):
        """"""
        self.player.key("release", key, modifiers)
        self.other.key("release", key, modifiers)
