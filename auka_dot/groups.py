import math
import sys
import numpy as np
import pygame
from pygame.locals import *


# set up the colors (RGB - red-green-blue values)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0,255,0)


class Circle:
    def __init__(self, x, y, radius, color):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color

    def display(self):
        pygame.draw.circle(windowSurface, self.color, (self.x, self.y), self.radius, 1)

class Groups:
    def __init__(self):
        self.landsvaedi = []
        self.infected = []

    def append(self, person):
        self.landsvaedi.append(person)

    def covid(self, infect):
        self.infected.append(infect)

    def collision(self, person):
        if pygame.sprite.spritecollideany(person, self.infected) is not None:

#append er til að setja einstaklinga/bolta í landsvæði
#smitaðir fara í infected lista í covid fallinu
#person er undirfall þar sem hann collide-ar í smitaða hópinn - því bætum við þeim einstakling við hópinn og breytum um lit
#það er fjögur object - suður, vestur, austur og norður

# set up pygame
pygame.init()

# set up the window
xmax = 600
ymax = 400
windowSurface = pygame.display.set_mode((xmax, ymax))
pygame.display.set_caption('Covid-19 hermir')

FRAMES_PER_SECOND = 30
fpsClock = pygame.time.Clock()

n = 20 # Number of points
speed = 0.01
radius = 5

# Initial coordinates are uniformly random in (0, 1)
x = np.random.rand(n)
y = np.random.rand(n)
color = np.zeros(n, dtype = object)
color[0] = GREEN
for i in range(1,n):
    color[i] = BLUE



# Point velocity is uniformly random in (0, speed)
vx = speed * np.random.rand(n)
vy = speed * np.random.rand(n)

# run the main loop
while True:
    # Clear screen
    windowSurface.fill(WHITE)

    # Update positions
    for i in range(n):
        windowSurface.fill(WHITE)
        
        # Reverse directon if point hits the boundary
        if x[i] < 0 or x[i] > 1:
            vx[i] = -1 * vx[i]
        if y[i] < 0 or y[i] > 1:
            vy[i] = -1 * vy[i]
        x[i] += vx[i]
        y[i] += vy[i]

    for i in range(n):
        for j in range(i+1,n):
            distance = math.hypot(int(x[i] * xmax) - int(x[j] * xmax), int(y[i] * ymax)- int(y[j]* ymax))
            if distance <= radius*2:
                vx[i] = -1 * vx[i]
                vy[i] = -1 * vy[i]
                vx[j] = -1 * vy[j]
                vx[j] = -1 * vy[j]
                if color[i] == GREEN:
                    color[j] = GREEN
                elif color[j] == GREEN:
                    color[i] = GREEN

    # Redraw
    
    for i in range(n):
        pygame.draw.circle(windowSurface, color[i], \
                           (int(xmax * x[i]), int(ymax * y[i])), radius, 0)
    
       
    # Event handling
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    fpsClock.tick(FRAMES_PER_SECOND)
