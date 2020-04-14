import math
import random
import sys
import numpy as np
import pygame
from pygame.locals import *

RADIUS = 5

class Person:

    def __init__(self, health, speed, leftX, rightX, topY, bottomY):
        self.leftX = leftX
        self.rightX = rightX
        self.bottomY = bottomY
        self.topY = topY
        self.x = random.uniform(self.leftX, self.rightX)
        self.y = random.uniform(self.bottomY, self.topY)
        self.speed = speed
        self.vx = speed * random.uniform(0,1)
        self.vy = speed * random.uniform(0,1)
        self.health = health

    def draw(self, windowSurface, xmax, ymax):
        pygame.draw.circle(windowSurface, self.health, (int(xmax * self.x), int(ymax * self.y)), RADIUS, 0)

    def move(self):
        if self.x < 0 or self.x > 1:
            self.vx = -1 * self.vx
        if self.y < 0 or self.y > 1:
            self.vy = -1 * self.vy
        self.x += self.vx
        self.y += self.vy

    


        
    
    
