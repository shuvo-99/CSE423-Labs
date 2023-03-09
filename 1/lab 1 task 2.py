from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random


def draw_points():
    glPointSize(4)
    glBegin(GL_POINTS)
    glVertex2f(260, 180)
    glEnd()


def draw_lines():
    glPointSize(2)
    glBegin(GL_LINES)

    # triangle
    glVertex2f(200, 250)
    glVertex2f(250, 300)
    glVertex2f(250, 300)
    glVertex2f(300, 250)
    glVertex2f(300, 250)
    glVertex2f(200, 250)

    # square
    # left wall
    glVertex2f(200, 250)
    glVertex2f(200, 150)

    # right wall
    glVertex2f(300, 250)
    glVertex2f(300, 150)

    # down wall
    glVertex2f(200, 150)
    glVertex2f(300, 150)

    # door
    glVertex2f(230, 150)
    glVertex2f(230, 200)
    glVertex2f(230, 200)
    glVertex2f(270, 200)
    glVertex2f(270, 200)
    glVertex2f(270, 150)

    # left window
    glVertex2f(220, 210)
    glVertex2f(220, 240)
    glVertex2f(220, 240)
    glVertex2f(240, 240)
    glVertex2f(240, 240)
    glVertex2f(240, 210)
    glVertex2f(240, 210)
    glVertex2f(220, 210)

    # right window
    glVertex2f(260, 210)
    glVertex2f(260, 240)
    glVertex2f(260, 240)
    glVertex2f(280, 240)
    glVertex2f(280, 240)
    glVertex2f(280, 210)
    glVertex2f(280, 210)
    glVertex2f(260, 210)

    glEnd()


def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(1.0, 1.0, 0.0)  # konokichur color set (RGB)
    # call the draw methods here
    draw_lines()
    draw_points()
    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500)  # window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"OpenGL Coding Practice")  # window name
glutDisplayFunc(showScreen)

glutMainLoop()
