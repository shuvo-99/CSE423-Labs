from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random

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
   glColor3f(1.0, 1.0, 0.0)
   # call the draw methods here
   glPointSize(5)
   glBegin(GL_POINTS)
   for i in range(0, 50):
       glVertex2f(random.randint(0,500), random.randint(0,500))
   glEnd()

   glutSwapBuffers()


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500)  # window size
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"OpenGL Coding Practice")  # window name
glutDisplayFunc(showScreen)

glutMainLoop()
