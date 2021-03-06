import math
import random
import sys
import numpy as np
import pygame
import pygame_gui
import time
from pygame.locals import *
from Svaedi import *

WHITE = (255, 255, 255)
SICK = (255, 0, 0)

pygame.init()

xmax = 800
ymax = 600
windowSurface = pygame.display.set_mode((xmax, ymax))
pygame.display.set_caption('Covid-19 hermir')


background = pygame.Surface((xmax, ymax))
background.fill(WHITE)

manager = pygame_gui.UIManager((xmax, ymax))

caption = pygame_gui.elements.ui_label.UILabel(relative_rect = pygame.Rect((10,20),(400,40)), text = 'Hermun eftir Covid-19 í mismunandi aðstæðum: ',manager = manager)


button_1 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((25, 120), (200,50)), text = 'Ef ekkert væri gert!', manager = manager)
button_2 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((25, 260), (200,50)), text = 'Flutning á milli 4 svæða', manager = manager)
button_3 = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((25, 440), (200,50)), text = 'Sóttkví', manager = manager)

slider = pygame_gui.elements.ui_label.UILabel(relative_rect = pygame.Rect((260,110),(200,20)), text = 'Veldu fjölda: ',manager = manager)
horiz_slider = pygame_gui.elements.UIHorizontalSlider(relative_rect=pygame.Rect((260, 130), (210, 30)),start_value = 30, value_range=(2,70),manager=manager)

slider1 = pygame_gui.elements.ui_label.UILabel(relative_rect = pygame.Rect((260,230),(170,20)), text = 'Fjöldi fyrir Svæði 1:',manager = manager)
slider2 = pygame_gui.elements.ui_label.UILabel(relative_rect = pygame.Rect((500,230),(170,20)), text = 'Fjöldi fyrir Svæði 2:',manager = manager)
slider3 = pygame_gui.elements.ui_label.UILabel(relative_rect = pygame.Rect((260,310),(170,20)), text = 'Fjöldi fyrir Svæði 3:',manager = manager)
slider4 = pygame_gui.elements.ui_label.UILabel(relative_rect = pygame.Rect((500,310),(170,20)), text = 'Fjöldi fyrir Svæði 4:',manager = manager)

horiz_slider1 = pygame_gui.elements.UIHorizontalSlider(relative_rect=pygame.Rect((260, 250), (210, 30)),start_value = 10, value_range=(2,30),manager=manager)
horiz_slider2 = pygame_gui.elements.UIHorizontalSlider(relative_rect=pygame.Rect((500, 250), (210, 30)),start_value = 10, value_range=(2,30),manager=manager)
horiz_slider3 = pygame_gui.elements.UIHorizontalSlider(relative_rect=pygame.Rect((260, 330), (210, 30)),start_value = 10, value_range=(2,30),manager=manager)
horiz_slider4 = pygame_gui.elements.UIHorizontalSlider(relative_rect=pygame.Rect((500, 330), (210, 30)),start_value = 10, value_range=(2,30),manager=manager)

slider5 = pygame_gui.elements.ui_label.UILabel(relative_rect = pygame.Rect((260,430),(170,20)), text = 'Fjöldi heilbrigða: ',manager = manager)
slider6 = pygame_gui.elements.ui_label.UILabel(relative_rect = pygame.Rect((500,430),(170,20)), text = 'Fjöldi í sóttkví: ',manager = manager)

horiz_slider5 = pygame_gui.elements.UIHorizontalSlider(relative_rect=pygame.Rect((260, 450), (210, 30)),start_value = 20, value_range=(2,50),manager=manager)
horiz_slider6 = pygame_gui.elements.UIHorizontalSlider(relative_rect=pygame.Rect((500, 450), (210, 30)),start_value = 5, value_range=(2,10),manager=manager)


FRAMES_PER_SECOND = 30
fpsClock = pygame.time.Clock()


def button1():
    
    Ekkert = Svaedi(int(horiz_slider.get_current_value()), 0, 1, 1, 0)
    Ekkert.persons = np.delete(Ekkert.persons, 1)
    Ekkert.persons = np.append(Ekkert.persons, Person(SICK, Ekkert.speed, 0, 1, 1, 0))

    run = True
    while run:
        windowSurface.fill(WHITE)
        
        Ekkert.move(xmax, ymax)
        Ekkert.draw(windowSurface, xmax, ymax)

        for event in pygame.event.get():
            if event.type == QUIT:
                run = False
            
        pygame.display.update()
        fpsClock.tick(FRAMES_PER_SECOND)

    run_loop()
    
                
def button2():

    n = int(horiz_slider1.get_current_value())
    n1 = int(horiz_slider2.get_current_value())
    n2 = int(horiz_slider3.get_current_value())
    n3 = int(horiz_slider4.get_current_value())

    Rvk = Svaedi(n, 0, 0.5, 0.5, 0)
    Ak = Svaedi(n1, 0.5, 1, 1, 0.5)
    Egils = Svaedi(n2, 0, 0.5, 1, 0.5)
    Isafj = Svaedi(n3, 0.5, 1, 0.5, 0)

    ## Byrja með einn sýktan í Rvk
    Rvk.persons = np.delete(Rvk.persons, 1)
    Rvk.persons = np.append(Rvk.persons, Person(SICK, Rvk.speed, 0, 0.5, 0.5, 0))

    run = True
    while run:
        windowSurface.fill(WHITE)
        
        Rvk.move(xmax, ymax)
        Ak.move(xmax, ymax)
        Egils.move(xmax, ymax)
        Isafj.move(xmax, ymax)
        
        for i in range(Rvk.n):
            if Rvk.next_to_rightBorder(i) and (Rvk.n == n or Rvk.n > n):
                Rvk.persons = np.delete(Rvk.persons, i)
                Rvk.n = Rvk.n-1
                Isafj.n = Isafj.n+1
                Isafj.persons = np.append(Isafj.persons, Person(SICK, Isafj.speed, 0.5, 1, 0.5, 0))

        
        for i in range(Rvk.n):
            if Rvk.next_to_bottomBorder(i) and (Rvk.n == n or Rvk.n > n):
                Rvk.persons = np.delete(Rvk.persons, i)
                Rvk.n = Rvk.n-1
                Egils.n = Egils.n+1
                Egils.persons = np.append(Egils.persons, Person(SICK, Egils.speed, 0, 0.5, 1, 0.5))

        for i in range(Egils.n):
            if Egils.next_to_topBorder(i) and (Egils.n > n2 or Egils.n == n2):
                Egils.persons = np.delete(Egils.persons, i)
                Egils.n = Egils.n-1
                Rvk.n = Rvk.n+1
                Rvk.persons = np.append(Rvk.persons, Person(SICK, Rvk.speed, 0, 0.5, 0.5, 0))

        for i in range(Egils.n):
            if Egils.next_to_rightBorder(i) and (Egils.n > n2 or Egils.n == n2):
                Egils.persons = np.delete(Egils.persons, i)
                Egils.n = Egils.n-1
                Ak.n = Ak.n+1
                Ak.persons = np.append(Ak.persons, Person(SICK, Ak.speed, 0.5, 1, 1, 0.5))

        for i in range(Ak.n):
            if Ak.next_to_leftBorder(i) and (Ak.n > n1 or Ak.n == n1):
                Ak.persons = np.delete(Ak.persons, i)
                Ak.n = Ak.n-1
                Egils.n = Egils.n+1
                Egils.persons = np.append(Egils.persons, Person(SICK, Egils.speed, 0, 0.5, 1, 0.5))

        for i in range(Ak.n):
            if Ak.next_to_topBorder(i) and (Ak.n > n1 or Ak.n == n1):
                Ak.persons = np.delete(Ak.persons, i)
                Ak.n = Ak.n-1
                Isafj.n = Isafj.n+1
                Isafj.persons = np.append(Isafj.persons, Person(SICK, Isafj.speed, 0.5, 1, 0.5, 0))

        for i in range(Isafj.n):
            if Isafj.next_to_bottomBorder(i) and (Isafj.n > n3 or Isafj.n == n3):
                Isafj.persons = np.delete(Isafj.persons, i)
                Isafj.n = Isafj.n-1
                Ak.n = Ak.n+1
                Ak.persons = np.append(Ak.persons, Person(SICK, Ak.speed, 0.5, 1, 1, 0.5))

        for i in range(Isafj.n):
            if Isafj.next_to_leftBorder(i) and (Isafj.n > n3 or Isafj.n == n3):
                Isafj.persons = np.delete(Isafj.persons, i)
                Isafj.n = Isafj.n-1
                Rvk.n = Rvk.n+1
                Rvk.persons = np.append(Rvk.persons, Person(SICK, Rvk.speed, 0, 0.5, 0.5, 0))
        
        Rvk.draw(windowSurface, xmax, ymax)
        Ak.draw(windowSurface, xmax, ymax)
        Egils.draw(windowSurface, xmax, ymax)
        Isafj.draw(windowSurface, xmax, ymax)

        for event in pygame.event.get():
            if event.type == QUIT:
                run = False
            
        pygame.display.update()
        fpsClock.tick(FRAMES_PER_SECOND)

    run_loop()

def button3():
    windowSurface.fill(WHITE)

    n = int(horiz_slider5.get_current_value())
    n1 = int(horiz_slider6.get_current_value())

    Healthy = Svaedi(n, 0, 0.8, 1, 0)
    Sick = Svaedi(n1, 0.8, 1, 0.6, 0.4)
    run = True
    hasTransferedOneToBeSick = False

    for person in Sick.persons:
        person.health = SICK

    for person in Healthy.persons:
        person.health = HEALTHY
    
    while run:
        windowSurface.fill(WHITE)

        Healthy.move(xmax, ymax)
        Sick.move(xmax, ymax)

        Healthy.draw(windowSurface, xmax, ymax)
        Sick.draw(windowSurface, xmax, ymax)

        allSickSick = True
        for person in Sick.persons:
            if person.health != SICK:
                allSickSick = False

        if allSickSick and not hasTransferedOneToBeSick:
            hasTransferedOneToBeSick = True
            Healthy.persons[0].set_sick()
            

        allHealthySick = True
        for person in Healthy.persons:
            if person.health != SICK:
                allHealthySick = False
    
        
    
        run = not allHealthySick
  
        for event in pygame.event.get():
            if event.type == QUIT:
                run = False
            
        pygame.display.update()
        fpsClock.tick(FRAMES_PER_SECOND)

    run_loop()
    
def run_loop():

    is_running = True

    while is_running:
        windowSurface.fill(WHITE)
        time_delta = fpsClock.tick(60)/100.0
   
        for event in pygame.event.get():
            if event.type == QUIT:
                is_running = False
                pygame.quit()
                sys.exit()
            if event.type == pygame.USEREVENT:
                if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                    if event.ui_element == button_1:
                        button1()
                
                    if event.ui_element == button_2:
                        button2()

                    if event.ui_element == button_3:
                        button3()

                if event.user_type == pygame_gui.UI_HORIZONTAL_SLIDER_MOVED:
                    if event.ui_element == horiz_slider:
                        value = int(horiz_slider.get_current_value())
                        print('value = ', value)
                    if event.ui_element == horiz_slider1:
                        value = int(horiz_slider1.get_current_value())
                        print('value = ', value)
                    if event.ui_element == horiz_slider2:
                        value = int(horiz_slider2.get_current_value())
                        print('value = ', value)
                    if event.ui_element == horiz_slider3:
                        value = int(horiz_slider3.get_current_value())
                        print('value = ', value)
                    if event.ui_element == horiz_slider4:
                        value = int(horiz_slider4.get_current_value())
                        print('value = ', value)
                    if event.ui_element == horiz_slider5:
                        value = int(horiz_slider5.get_current_value())
                        print('value = ', value)
                    if event.ui_element == horiz_slider6:
                        value = int(horiz_slider6.get_current_value())
                        print('value = ', value)

                    
                    
            manager.process_events(event)
        manager.update(time_delta)
    
        windowSurface.blit(background, (0,0))
        manager.draw_ui(windowSurface)
    
        pygame.display.update()

run_loop()


