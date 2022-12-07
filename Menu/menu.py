from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


def blok():
    glColor3ub(60, 60, 60)
    glBegin(GL_POLYGON)
    glVertex2f(-300, 150)
    glVertex2f(-300, 300)
    glVertex2f(300, 300)
    glVertex2f(300, 150)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(-160, 40)
    glVertex2f(160, 40)
    glVertex2f(160, -40)
    glVertex2f(-160, -40)
    glEnd()

    glBegin(GL_POLYGON)
    glVertex2f(-160, -90)
    glVertex2f(160, -90)
    glVertex2f(160, -170)
    glVertex2f(-160, -170)
    glEnd()
    
    glBegin(GL_POLYGON)
    glVertex2f(-160, -220)
    glVertex2f(160, -220)
    glVertex2f(160, -300)
    glVertex2f(-160, -300)
    glEnd()

def txt():
    glColor3ub(255, 255, 255)
    glLineWidth(2)
    glBegin(GL_LINES)
    glVertex(-220, 280)
    glVertex(-180, 280)
    
    glVertex(-200, 280)
    glVertex(-200, 240)

    glVertex(-160, 280)
    glVertex(-160, 240)
    
    glVertex(-160, 260)
    glVertex(-120, 260)

    glVertex(-120, 280)
    glVertex(-120, 240)

    glVertex(-100, 280)
    glVertex(-100, 240)

    glVertex(-100, 280)
    glVertex(-60, 280)

    glVertex(-100, 260)
    glVertex(-80, 260)
    
    glVertex(-100, 240)
    glVertex(-60, 240)

    glVertex(0, 280)
    glVertex(0, 240)
    
    glVertex(0, 280)
    glVertex(20, 260)

    glVertex(20, 260)
    glVertex(40, 280)

    glVertex(40, 280)
    glVertex(40, 240)

    glVertex(60, 240)
    glVertex(80, 280)

    glVertex(80, 280)
    glVertex(100, 240)

    glVertex(70, 260)
    glVertex(90, 260)

    glVertex(120, 280)
    glVertex(160, 280)

    glVertex(160, 280)
    glVertex(120, 240)

    glVertex(120, 240)
    glVertex(160, 240)

    glVertex(180, 280)
    glVertex(180, 240)

    glVertex(180, 280)
    glVertex(220, 280)

    glVertex(180, 260)
    glVertex(200, 260)

    glVertex(180, 240)
    glVertex(220, 240)

    glVertex(-200, 180)
    glVertex(-200, 220)

    glVertex(-200, 220)
    glVertex(-180, 220)

    glVertex(-180, 220)
    glVertex(-160, 200)

    glVertex(-160, 200)
    glVertex(-180, 180)

    glVertex(-180, 180)
    glVertex(-200, 180)

    glVertex(-140, 220)
    glVertex(-140, 180)
    
    glVertex(-140, 180)
    glVertex(-100, 180)

    glVertex(-100, 180)
    glVertex(-100, 220)

    glVertex(-80, 180)
    glVertex(-80, 220)

    glVertex(-80, 220)
    glVertex(-40, 180)

    glVertex(-40, 180)
    glVertex(-40, 220)

    glVertex(20, 220)
    glVertex(-20, 220)

    glVertex(-20, 220)
    glVertex(-20, 180)

    glVertex(-20, 180)
    glVertex(20, 180)

    glVertex(20, 180)
    glVertex(20, 200)
    
    glVertex(20, 200)
    glVertex(0, 200)

    glVertex(40, 220)
    glVertex(40, 180)

    glVertex(40, 220)
    glVertex(80, 220)

    glVertex(40, 200)
    glVertex(60, 200)

    glVertex(40, 180)
    glVertex(80, 180)

    glVertex(100, 220)
    glVertex(140, 220)

    glVertex(140, 220)
    glVertex(140, 180)

    glVertex(140, 180)
    glVertex(100, 180)

    glVertex(100, 180)
    glVertex(100, 220)

    glVertex(160, 180)
    glVertex(160, 220)
    
    glVertex(160, 220)
    glVertex(200, 180)

    glVertex(200, 180)
    glVertex(200, 220)

    glVertex(260, 160)
    glVertex(260, 290)

    glVertex(250, 162)
    glVertex(-250, 162)

    glVertex(-260, 160)
    glVertex(-260, 290)

    glVertex(-280, 270)
    glVertex(-280, 170)

    glVertex(280, 270)
    glVertex(280, 170)

    glEnd()
123
def lvl1():
    glTranslated(0, 0, 0)
    glColor3ub(255, 255, 255)
    glLineWidth(2)
    glBegin(GL_LINES)
    glVertex(-140, 20) #L
    glVertex(-140, -20)

    glVertex(-140, -20)
    glVertex(-120, -20)

    glVertex(-100, 20) #E
    glVertex(-80, 20)
    
    glVertex(-100, 20)
    glVertex(-100, -20)

    glVertex(-100, 0)
    glVertex(-80, 0)
    
    glVertex(-100, -20)
    glVertex(-80, -20)

    glVertex(-60, 20) #V
    glVertex(-40, -20)

    glVertex(-40, -20)
    glVertex(-20, 20)

    glVertex(0, 20) #E
    glVertex(20, 20)

    glVertex(0, 20)
    glVertex(0, -20)
    
    glVertex(0, 0)
    glVertex(20, 0)

    glVertex(0, -20)
    glVertex(20, -20)

    glVertex(40, 20) #L
    glVertex(40, -20)

    glVertex(40, -20)
    glVertex(60, -20)

    glVertex(120, 20) #1
    glVertex(120, -20)
    glEnd()

def lvl2():
    glTranslated(0, -130, 0)
    glColor3ub(255, 255, 255)
    glLineWidth(2)
    glBegin(GL_LINES)
    glVertex(-140, 20) #L
    glVertex(-140, -20)

    glVertex(-140, -20)
    glVertex(-120, -20)

    glVertex(-100, 20) #E
    glVertex(-80, 20)
    
    glVertex(-100, 20)
    glVertex(-100, -20)

    glVertex(-100, 0)
    glVertex(-80, 0)
    
    glVertex(-100, -20)
    glVertex(-80, -20)

    glVertex(-60, 20) #V
    glVertex(-40, -20)

    glVertex(-40, -20)
    glVertex(-20, 20)

    glVertex(0, 20) #E
    glVertex(20, 20)

    glVertex(0, 20)
    glVertex(0, -20)
    
    glVertex(0, 0)
    glVertex(20, 0)

    glVertex(0, -20)
    glVertex(20, -20)

    glVertex(40, 20) #L
    glVertex(40, -20)

    glVertex(40, -20)
    glVertex(60, -20)

    glVertex(110, 20) #2
    glVertex(130, 20)

    glVertex(130, 20)
    glVertex(130, 0)

    glVertex(130, 0)
    glVertex(110, 0)

    glVertex(110, 0)
    glVertex(110, -20)

    glVertex(110, -20)
    glVertex(130, -20)
    glEnd()

def lvl3():
    glTranslated(0, -130, 0)
    glColor3ub(255, 255, 255)
    glLineWidth(2)
    glBegin(GL_LINES)
    glVertex(-140, 20) #L
    glVertex(-140, -20)

    glVertex(-140, -20)
    glVertex(-120, -20)

    glVertex(-100, 20) #E
    glVertex(-80, 20)
    
    glVertex(-100, 20)
    glVertex(-100, -20)

    glVertex(-100, 0)
    glVertex(-80, 0)
    
    glVertex(-100, -20)
    glVertex(-80, -20)

    glVertex(-60, 20) #V
    glVertex(-40, -20)

    glVertex(-40, -20)
    glVertex(-20, 20)

    glVertex(0, 20) #E
    glVertex(20, 20)

    glVertex(0, 20)
    glVertex(0, -20)
    
    glVertex(0, 0)
    glVertex(20, 0)

    glVertex(0, -20)
    glVertex(20, -20)

    glVertex(40, 20) #L
    glVertex(40, -20)

    glVertex(40, -20)
    glVertex(60, -20)

    glVertex(110, 20) #3
    glVertex(130, 20)

    glVertex(130, 20)
    glVertex(130, -20)

    glVertex(130, 0)
    glVertex(110, 0)

    glVertex(130, -20)
    glVertex(110, -20)


    glEnd()



# Cek :
def iterate():
    glViewport(0, 0, 700, 700)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-700, 700, -700, 700, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()
def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    blok()
    txt()
    lvl1()
    lvl2()
    lvl3()
    
    glutSwapBuffers()
    
glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(700, 700)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow("OpenGL Coding Practice : GL_POLYGON")
glutDisplayFunc(showScreen)
glutIdleFunc(showScreen)
glutMainLoop()
