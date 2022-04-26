# Module imports
import arcade as ar
from random import choice, randrange
# File imports
from settings import *

#DOC YOU SUCK YOUR DADS TOES AND THAS KINDA WACK BRO I MEAN IF YOU MAKE MONSY BUT WTF YOUR KINDA POOPY DICKBAGS BUT INSTEAD IS A WASTE OF TIME WHEN THE SUNFLOWER CRIES IN THE MORN AND SHE WAILS THAT THE MOUNTINS OF BLUE ARE TO BE INSTEAD OF NOT TO BE. IT'S FINALLY TIME FOR YOU TO STOP THIS SOPPY MADNESS. NOW GO TO BED ON YOUR FACE BECAUSE YOU DESERVE DUSTY. SHUT UP SLUT I'M NOT DONE TALKING. OKAY NOW I AM.!!!!!

class Sprite:
    alive = True
    def __init__(
        self,
        width=0,
        height=0,
        color=BLACK,
        x=0, y=0,
        speed=0,
        speed_mod=1
        ):

        self.width = width
        self.height = height
        self.color = color
        self.x = x
        self.y = y
        self.speed = speed
        self.speed_mod = speed_mod

    def die(self):
        pass

class Player(Sprite):
    def __init__(self, width, height, color, x, y, speed, speed_mod):
        """Initilize player stats"""
        super().__init__(width, height, color, x, y, speed, speed_mod)
        self.left = False
        self.right = False
        self.up = False
        self.down = False

    def update(self, delta_time):
        """"""
        speed = self.speed*delta_time

        # Border Collision
        if self.x >= WIDTH-self.width:   self.right = False
        if self.x <= 0:                  self.left = False
        if self.y >= HEIGHT-self.height: self.up = False
        if self.y <= 0:                  self.down = False

        # Movement
        if self.right: self.x += speed
        if self.left:  self.x -= speed
        if self.up:    self.y += speed
        if self.down:  self.y -= speed

    def draw(self):
        """Creates player"""
        ar.draw_xywh_rectangle_filled(
            self.x, self.y, self.width, self.height, self.color
        )

    def key(self, mode, key, modifier):
        """
        Check if keys are interacted with 
        and will do something with that key

        mode: 'press' or 'release'
        """
        def press(self, key, mod):
            """Key pressed down"""
            # Start movement
            if key == ar.key.LSHIFT: self.speed *= self.speed_mod
            if key == ar.key.LALT:   self.speed /= self.speed_mod
            if key == ar.key.D: self.right = True
            if key == ar.key.A: self.left = True
            if key == ar.key.W: self.up = True
            if key == ar.key.S: self.down = True

        def release(self, key, mod):
            """Key let go of"""
            # End movement
            if key == ar.key.LSHIFT: self.speed = PLAYER_SPEED
            if mod == ar.key.LALT:   self.speed = PLAYER_SPEED
            if key == ar.key.D: self.right = False
            if key == ar.key.A: self.left = False
            if key == ar.key.W: self.up = False
            if key == ar.key.S: self.down = False
        
        if mode == "press": 
            press(self, key, modifier)
        if mode == "release": 
            release(self, key, modifier)
'''           
    def create_player(self):
        
        self.player_sprite = Player()
        
        self.player_list = ar.SpriteList()
        
        self.player_sprite = ar.Sprite()
'''


