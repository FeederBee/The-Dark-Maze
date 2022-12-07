from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

w, h = 1000, 1000
state = int(input())
def bg(x,y):
    glBegin(GL_POLYGON)
    glVertex(0, 0)
    glVertex(0, y)

    glVertex(0, y)
    glVertex(x, y)

    glVertex(x, y)
    glVertex(x, 0)

    glVertex(x, 0)
    glVertex(0, 0)

    glEnd()

def maze1():
    glColor3f(0.0, 0.0, 0.0)
    glLineWidth(3)
    glBegin(GL_LINES)
    glVertex(0, 100)
    glVertex(0, 500)

    glVertex(0, 500)
    glVertex(500, 500)

    glVertex(500, 500)
    glVertex(500, 300)

    glVertex(500, 200)
    glVertex(500, 0)
    
    glVertex(500, 0)
    glVertex(0, 0)

    glVertex(0, 100)
    glVertex(300, 100)

    glVertex(400, 0)
    glVertex(400, 100)

    glVertex(100, 200)
    glVertex(100, 400)

    glVertex(100, 400)
    glVertex(200, 400)

    glVertex(200, 400)
    glVertex(200, 200)

    glVertex(200, 200)
    glVertex(500, 200)

    glVertex(400, 500)
    glVertex(400, 400)

    glVertex(300, 400)
    glVertex(300, 300)

    glVertex(300, 300)
    glVertex(500, 300)

    glEnd()

def maze2():
    glColor3ub(0, 0, 0)
    glLineWidth(3)
    glBegin(GL_LINES)
    glVertex(0, 0)
    glVertex(0, 300)

    glVertex(0, 400)
    glVertex(0, 800)

    glVertex(0, 800)
    glVertex(800, 800)

    glVertex(800, 700)
    glVertex(800, 0)
    
    glVertex(800, 0)
    glVertex(0, 0)

    glVertex(0, 300)
    glVertex(100, 300)

    glVertex(100, 300)
    glVertex(100, 200)

    glVertex(100, 100)
    glVertex(100, 200)

    glVertex(200, 0)
    glVertex(200, 300)
    
    glVertex(200, 200)
    glVertex(300, 200)

    glVertex(300, 100)
    glVertex(700, 100)

    glVertex(400, 100)
    glVertex(400, 400)

    glVertex(300, 300)
    glVertex(600, 300)

    glVertex(500, 300)
    glVertex(500, 200)

    glVertex(500, 200)
    glVertex(700, 200)

    glVertex(700, 200)
    glVertex(700, 300)

    glVertex(400, 400)
    glVertex(700, 400)
    
    glVertex(700, 400)
    glVertex(700, 700)

    glVertex(100, 500)
    glVertex(100, 700)

    glVertex(100, 700)
    glVertex(400, 700)

    glVertex(400, 700)
    glVertex(400, 600)
    
    glVertex(300, 400)
    glVertex(300, 600)

    glVertex(300, 500)
    glVertex(500, 500)

    glVertex(300, 600)
    glVertex(600, 600)

    glVertex(600, 500)
    glVertex(600, 700)

    glVertex(600, 700)
    glVertex(800, 700)

    glVertex(0, 400)
    glVertex(200, 400)

    glVertex(200, 400)
    glVertex(200, 600)

    glVertex(500, 800)
    glVertex(500, 700)

    glEnd()

def maze3():
    glColor3ub(0, 0, 0)
    glScaled(1, 0.84, 0)
    glLineWidth(3)
    glBegin(GL_LINES)
    glVertex(0, 0)
    glVertex(0, 900)

    glVertex(0, 1000)
    glVertex(1000, 1000)

    glVertex(1000, 1000)
    glVertex(1000, 600)

    glVertex(1000, 500)
    glVertex(1000, 0)

    glVertex(1000, 0)
    glVertex(0, 0)

    glVertex(0, 900)
    glVertex(300 , 900)

    glVertex(0, 600)
    glVertex(100, 600)

    glVertex(100, 600)
    glVertex(100, 700)

    glVertex(400, 1000)
    glVertex(400, 700)

    glVertex(400, 800)
    glVertex(100, 800)
    
    glVertex(200, 800)
    glVertex(200, 400)

    glVertex(200, 600)
    glVertex(300, 600)
    
    glVertex(300, 600)
    glVertex(300, 700)

    glVertex(200, 500)
    glVertex(100, 500)

    glVertex(100, 500)
    glVertex(100, 300)

    glVertex(100, 300)
    glVertex(400, 300)

    glVertex(200, 300)
    glVertex(200, 200)

    glVertex(300, 300)
    glVertex(300, 200)
    
    glVertex(300, 200)
    glVertex(500, 200)

    glVertex(100, 200)
    glVertex(100, 100)

    glVertex(100, 100)
    glVertex(600, 100)
    
    glVertex(600, 100)
    glVertex(600, 400)

    glVertex(300, 500)
    glVertex(300, 400)
    
    glVertex(300, 400)
    glVertex(500, 400)

    glVertex(400, 400)
    glVertex(400, 600)

    glVertex(500, 300)
    glVertex(500, 500)
    
    glVertex(500, 500)
    glVertex(600, 500)

    glVertex(700, 0)
    glVertex(700, 200)

    glVertex(700, 100)
    glVertex(900, 100)

    glVertex(800, 100)
    glVertex(800, 300)

    glVertex(900, 200)
    glVertex(900, 300)
    
    glVertex(900, 300)
    glVertex(1000, 300)

    glVertex(500, 1000)
    glVertex(500, 600)

    glVertex(500, 800)
    glVertex(600, 800)

    glVertex(500, 600)
    glVertex(700, 600)

    glVertex(700, 600)
    glVertex(700, 300)
    
    glVertex(700, 400)
    glVertex(900, 400)

    glVertex(1000, 500)
    glVertex(800, 500)

    glVertex(800, 500)
    glVertex(800, 800)

    glVertex(800, 700)
    glVertex(600, 700)

    glVertex(700, 700)
    glVertex(700, 900)

    glVertex(600, 900)
    glVertex(900, 900)

    glVertex(900, 800)
    glVertex(900, 600)

    glVertex(900, 600)
    glVertex(1000, 600)

    glEnd()


def iterate():
    glViewport(0, 0, 1000, 1000)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glColor3ub(50, 50, 50)
    glOrtho(-0, 1000, -0, 1000, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    # glColor3f(1.0, 0.0, 3.0)
    # glClearColor(80, 80, 80, 1)
    if state==1:
        x = 500
        y =500
        bg(x,y)
        maze1()
    elif state==2:
        x = 800
        y =800
        bg(x,y)
        maze2()
    elif state==3:
        x = 1000
        y = 1000
        bg(x,y)
        maze3()
    glutSwapBuffers()

glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(1000, 1000)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow("The Maze Dungeon")
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutMainLoop()