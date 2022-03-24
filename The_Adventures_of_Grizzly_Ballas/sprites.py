# Module imports
import arcade as ar
from random import choice, randrange
# File imports
from settings import *


class Player:
    def __init__(self):
        """Initilize player stats"""
        self.width = 100
        self.height = 100

        self.color = RED

        self.x = 300
        self.y = 300

        self.speed = PLAYER_SPEED
        self.speed_modifier = PLAYER_SPEED_MODIFIER

        self.left = False
        self.right = False
        self.up = False
        self.down = False
        self.player_sprite_list = ar.SpriteList()

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
        def press(self, key, modifier):
            """Key pressed down"""
            # Start movement
            if key == ar.key.LSHIFT: self.speed *= self.speed_modifier
            if key == ar.key.LALT:   self.speed /= self.speed_modifier

            if key == ar.key.D: self.right = True
            if key == ar.key.A: self.left = True
            if key == ar.key.W: self.up = True
            if key == ar.key.S: self.down = True

        def release(self, key, modifier):
            """Key let go of"""
            # End movement
            if key == ar.key.LSHIFT: self.speed = PLAYER_SPEED
            if key == ar.key.LALT:   self.speed = PLAYER_SPEED

            if key == ar.key.D: self.right = False
            if key == ar.key.A: self.left = False
            if key == ar.key.W: self.up = False
            if key == ar.key.S: self.down = False
        
        if mode == "press": 
            press(self, key, modifier)
        if mode == "release": 
            release(self, key, modifier)


