from function import Polynomial
from matrix import Matrix

import sys
import os
import pygame
import math

FPS = 60
TITLE = "Curve Fitter"
SIZE = (800, 800)
WIDTH = SIZE[0]
HEIGHT = SIZE[1]
GRID = 8
BG_COLOR = (170, 238, 187)


def main():
    pygame.init()
    pygame.display.set_caption(TITLE)
    fps_clock = pygame.time.Clock()
    screen = pygame.display.set_mode(SIZE)
    # font_file = os.path.join(root_dir, FONT_FILENAME)
    # font = pygame.font.Font(font_file, FONT_SIZE)

    # Splash Screen
    screen.fill(BG_COLOR)
    pygame.display.update()

    points = [
            (0, 1),
            (1, 0.36788),
            (2, 0.018316),
            (3, 0.00012341),
            (4, 0),
            (-1, 0.36788),
            (-2, 0.018316),
            (-3, 0.00012341),
            (-4, 0),
            (2.5, 0.0019305)

    ]

    f = get_polynomial(points)


    while True:
        # Event management
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            # Screen resizing
            # if event.type == pygame.VIDEORESIZE: # event attr: size, w, h
            #     screen = pygame.display.set_mode(event.size, pygame.RESIZABLE)

            # if event.type == pygame.KEYDOWN:  # event attr: key, mod, unicode, scancode
            #     if event.key == pygame.K_DOWN:
            #         pass
            # if event.type == pygame.MOUSEMOTION:  # event attr: pos, rel, buttons, touch
            #     pass
            # if event.type == pygame.MOUSEBUTTONDOWN:  # event attr: pos, button, touch
            #     pass

        # Drawing a frame
        # ==== Do Something here ====
        # Draw from back to front; draw background first

        # Draw axes
        pygame.draw.line(screen, (200,0,0), (WIDTH/2,0), (WIDTH/2,HEIGHT), 3)
        pygame.draw.line(screen, (200,0,0), (0,HEIGHT/2), (WIDTH,HEIGHT/2), 3)

        # Draw points
        draw_points(screen, points)
        draw_function(screen, f)
            

        pygame.display.update()  # This should be at the end of each drawing a frame

        # FPS control
        fps_clock.tick(FPS)


def draw_points(screen, points):
    for p in points:
        pygame.draw.circle(screen, (0,0,0), (p[0]*WIDTH/GRID + WIDTH/2, -p[1]*HEIGHT/GRID + HEIGHT/2), 6)

def draw_function(screen, f):
    start = -(GRID/2)
    end = GRID/2

    i = start
    increment = 0.01
    while i <= end:
        #pygame.draw.circle(screen, (0,0,0), (i*WIDTH/GRID + WIDTH/2, -f.compute(i)*HEIGHT/GRID + HEIGHT/2), 6)
        pygame.draw.line(screen, (0,0,0), (i*WIDTH/GRID + WIDTH/2, -f.compute(i)*HEIGHT/GRID + HEIGHT/2), ((i+increment)*WIDTH/GRID + WIDTH/2, -f.compute(i+increment)*HEIGHT/GRID + HEIGHT/2), 2)
        i+=increment


def get_polynomial(points):
    # Define function we want
    f = Polynomial([4, -7, 3, 1], "f")
    
    # Create set of points
    #points = [
    #        (-1.5, 0.22313),
    #        (-1, 0.36788),
    #        (-0.5, 0.60653),
    #        (0, 1),
    #        (0.5, 1.64872),
    #        (1, 2.71828),
    #        (1.5, 4.48169),
    #        (2, 7.38906)
    #]
    n = len(points)

    # Compute set of polynomials
    polynomials = []
    for i in range(n): # iterate through each point in A
        coefficients = []
        for j in range(n+1):
            coefficients.append(points[i][0]**j)
        polynomials.append(Polynomial(coefficients))
    
    # Turn polynomials into system of linear equations
    A = []
    B = []
    for i in range(len(polynomials)):
        A += polynomials[i].coefficients
        B.append(points[i][1])
    M = Matrix(A, B)


    p = Polynomial(M.solve())
    p.print()
    return p



if __name__ == "__main__":
    main()