#!/usr/bin/python

from sdl2 import *
from OpenGL.GL import *
import ctypes

def draw_background():
    """
    Draws a fullscreen grey gradient quad as a background
    """
    glLoadIdentity()
    glBegin(GL_QUADS)
    glColor(0.2, 0.2, 0.2, 1.0)
    glVertex3f(1.0, -1.0, 0.0)
    glVertex3f(1.0, 1.0, 0.0)
    glColor(0.6, 0.6, 0.6, 1.0)
    glVertex3f(-1.0, 1.0, 0.0)
    glVertex3f(-1.0, -1.0, 0.0)
    glEnd()

def draw_quad(size, rotation):
    """
    Draws a quad centered to the screen with a given size and rotation

    Args:
        size     (float): the size of the quad, ranging from 0.0 to 1.0 (fullscreen-sized)
        rotation (float): the rotation of the quad in degrees
    """
    glLoadIdentity()
    glRotatef(rotation, 0.0, 0.0, 1.0)
    glBegin(GL_QUADS)
    glVertex3f(size, -size, 0.0)
    glVertex3f(size, size, 0.0)
    glVertex3f(-size, size, 0.0)
    glVertex3f(-size, -size, 0.0)
    glEnd()

def main():
    SDL_Init(SDL_INIT_VIDEO)
    window = SDL_CreateWindow(b"Fun little effects", SDL_WINDOWPOS_CENTERED, SDL_WINDOWPOS_CENTERED, 800, 800, SDL_WINDOW_OPENGL)
    context = SDL_GL_CreateContext(window)
    glMatrixMode(GL_MODELVIEW)

    x = 0
    running = True

    while running:
        draw_background()

        # draw quads
        for y in range(20):
            glColor((20 - y) * 0.05, 0.5, 0.0, 1.0)
            draw_quad(0.025 * (20 - y) + 0.006, x * (y + 1) / 10.0)
            glColor((20 - y) * 0.05, 0.0, 0.0, 1.0)
            draw_quad(0.025 * (20 - y), x * (y + 1) / 10.0)

        SDL_GL_SwapWindow(window)

        # handle exiting on window close / keyboard event
        event = SDL_Event()
        while SDL_PollEvent(ctypes.byref(event)) != 0:
            if (event.type == SDL_QUIT) or (event.type == SDL_KEYDOWN):
                running = False
                break

        x += 1
        SDL_Delay(30)

    SDL_DestroyWindow(window)
    SDL_Quit()
    return 0

if __name__ == '__main__':
    main()
