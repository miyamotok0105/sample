#!/usr/bin/python

from OpenGL.GL import *
from OpenGL.GLUT import *


def draw():
    glClearColor(1.0, 0.0, 0.0, 0.0)
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glFlush()
    glutSwapBuffers()


glutInit(sys.argv)
glutInitDisplayMode(GLUT_RGBA | GLUT_DOUBLE | GLUT_DEPTH)
glutInitWindowSize(320, 240)
glutCreateWindow("PyOpenGL 1")
glutDisplayFunc(draw)

glutMainLoop()



