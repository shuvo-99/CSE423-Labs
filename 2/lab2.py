from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import math


def findZone(dx, dy):
    if abs(dx) >= abs(dy) and (dx >= 0 and dy >= 0):
        Zone = 0
        return Zone

    elif abs(dy) >= abs(dx) and (dx >= 0 and dy >= 0):
        Zone = 1
        return Zone

    elif abs(dy) >= abs(dx) and (dx <= 0 and dy >= 0):
        Zone = 2
        return Zone

    elif abs(dx) >= abs(dy) and (dx <= 0 and dy >= 0):
        Zone = 3
        return Zone
    elif abs(dx) >= abs(dy) and (dx <= 0 and dy <= 0):
        Zone = 4
        return Zone
    elif abs(dy) >= abs(dx) and (dx <= 0 and dy <= 0):
        Zone = 5
        return Zone
    elif abs(dy) >= abs(dx) and (dx >= 0 and dy <= 0):
        Zone = 6
        return Zone
    elif abs(dx) >= abs(dy) and (dx >= 0 and dy <= 0):
        Zone = 7
        return Zone


def convertToZone0_X(x, y, zone):
    if zone == 1:
        return y
    elif zone == 2:
        return y
    elif zone == 3:
        return -x
    elif zone == 4:
        return -x
    elif zone == 5:
        return -y
    elif zone == 6:
        return -y
    else:
        return x


def convertToZone0_Y(x, y, zone):
    if zone == 1:
        return x
    elif zone == 2:
        return -x
    elif zone == 4:
        return -y
    elif zone == 5:
        return -x
    elif zone == 6:
        return x
    elif zone == 7:
        return -y
    else:
        return y


# Converting the zones from 0 before drawing
def draw(x, y, zone):
    if zone == 1:
        glVertex2d(y, x)
    elif zone == 2:
        glVertex2d(-y, x)
    elif zone == 3:
        glVertex2d(-x, y)
    elif zone == 4:
        glVertex2d(-x, -y)
    elif zone == 5:
        glVertex2d(-y, -x)
    elif zone == 6:
        glVertex2d(y, -x)
    elif zone == 7:
        glVertex2d(x, -y)
    else:
        glVertex2d(x, y)


def midpoint(x1, y1, x2, y2):
    glBegin(GL_POINTS)
    dx = x2 - x1
    dy = y2 - y1
    zone = findZone(dx, dy)
    new_x1 = convertToZone0_X(x1, y1, zone)
    new_y1 = convertToZone0_Y(x1, y1, zone)
    new_x2 = convertToZone0_X(x2, y2, zone)
    new_y2 = convertToZone0_Y(x2, y2, zone)
    dx = (new_x2 - new_x1)
    dy = (new_y2 - new_y1)
    d_init = (2 * dy) - dx
    NE = 2 * (dy - dx)
    E = 2 * dy
    x = new_x1
    y = new_y1

    while x <= new_x2:
        draw(x, y, zone)
        x += 1
        if d_init > 0:
            y += 1
            d_init = d_init + NE
        else:
            d_init = d_init + E
    glEnd()


def drawID():
    # print 0
    midpoint(60, 400, 120, 400)
    midpoint(60, 200, 120, 200)
    midpoint(60, 400, 60, 200)
    midpoint(120, 400, 120, 200)
    # print 1
    midpoint(200, 200, 200, 400)
    midpoint(150, 200, 250, 200)
    midpoint(150, 350, 200, 400)


def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def showscreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glColor3f(1.0, 1.0, 1.0)
    # call the draw methods here
    glPointSize(1)
    drawID()
    glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"ID- 20301301 - Last Two Digit - 01")
glutDisplayFunc(showscreen)
glutIdleFunc(showscreen)
glutMainLoop()
