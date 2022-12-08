from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

def victory():
    glColor3ub(0, 0, 0)
    glBegin(GL_POLYGON)
    glVertex(0, 0)
    glVertex(0, 2000)
    glVertex(2000, 2000)
    glVertex(2000, 0)
    glEnd()
    
    glColor3ub(120, 0, 0)
    glBegin(GL_POLYGON)
    glVertex(80, 280)
    glVertex(80, 480)
    glVertex(620, 480)
    glVertex(620, 280)
    glEnd()

    glColor3ub(150, 75, 0)
    glBegin(GL_POLYGON)
    glVertex(100, 300)
    glVertex(100, 460)
    glVertex(600, 460)
    glVertex(600, 300)
    glEnd()


    glColor3ub(150, 0, 0)
    glBegin(GL_POLYGON)
    glVertex(120, 320)
    glVertex(120, 440)
    glVertex(580, 440)
    glVertex(580, 320)
    glEnd()

    glColor3ub(255, 160, 160)
    glLineWidth(3)
    glBegin(GL_LINES)
    glVertex(160, 400)
    glVertex(180, 360)

    glVertex(180, 360)
    glVertex(200, 400)

    glVertex(220, 400)
    glVertex(220, 360)

    glVertex(280, 400)
    glVertex(240, 400)

    glVertex(240, 400)
    glVertex(240, 360)

    glVertex(240, 360)
    glVertex(280, 360)

    glVertex(300, 400)
    glVertex(340, 400)
    
    glVertex(320, 400)
    glVertex(320, 360)

    glVertex(360, 400)
    glVertex(400, 400)

    glVertex(400, 400)
    glVertex(400, 360)
    
    glVertex(400, 360)
    glVertex(360, 360)

    glVertex(360, 360)
    glVertex(360, 400)

    glVertex(420, 360)
    glVertex(420, 400)

    glVertex(420, 400)
    glVertex(460, 400)

    glVertex(460, 400)
    glVertex(460, 380)

    glVertex(460, 380)
    glVertex(420, 380)

    glVertex(420, 380)
    glVertex(460, 360)

    glVertex(480, 400)
    glVertex(500, 380)

    glVertex(500, 380)
    glVertex(500, 360)

    glVertex(500, 380)
    glVertex(520, 400)

    glVertex(540, 400)
    glVertex(540, 370)

    glVertex(540, 365)
    glVertex(540, 360)
    glEnd()

    glColor3ub(255, 160, 160)
    glLineWidth(3)
    glBegin(GL_LINES)
    glVertex(320, 200)
    glVertex(350, 220)
    
    glVertex(350, 220)
    glVertex(380, 200)

    glVertex(330, 200)
    glVertex(330, 180)

    glVertex(330, 180)
    glVertex(370, 180)

    glVertex(370, 180)
    glVertex(370, 200)

    glVertex(190, 150)
    glVertex(190, 130)

    glVertex(190, 150)
    glVertex(210, 150)

    glVertex(210, 150)
    glVertex(210, 140)

    glVertex(210, 140)
    glVertex(190, 140)

    glVertex(220, 130)
    glVertex(220, 150)

    glVertex(220, 150)
    glVertex(240, 150)

    glVertex(240, 150)
    glVertex(240, 140)

    glVertex(240, 140)
    glVertex(220, 140)

    glVertex(220, 140)
    glVertex(240, 130)

    glVertex(250, 150)
    glVertex(250, 130)

    glVertex(250, 150)
    glVertex(270, 150)

    glVertex(250, 140)
    glVertex(270, 140)

    glVertex(250, 130)
    glVertex(270, 130)

    glVertex(300, 150)
    glVertex(280, 150)

    glVertex(280, 150)
    glVertex(280, 140)

    glVertex(280, 140)
    glVertex(300, 140)

    glVertex(300, 140)
    glVertex(300, 130)

    glVertex(300, 130)
    glVertex(280, 130)

    glVertex(330, 150)
    glVertex(310, 150)

    glVertex(310, 150)
    glVertex(310, 140)

    glVertex(310, 140)
    glVertex(330, 140)

    glVertex(330, 140)
    glVertex(330, 130)
    
    glVertex(330, 130)
    glVertex(310, 130)

    glVertex(390, 150)
    glVertex(370, 150)
    
    glVertex(370, 150)
    glVertex(370, 140)

    glVertex(370, 140)
    glVertex(390, 140)

    glVertex(390, 140)
    glVertex(390, 130)

    glVertex(390, 130)
    glVertex(370, 130)

    glVertex(400, 130)
    glVertex(400, 150)

    glVertex(400, 150)
    glVertex(420, 150)

    glVertex(420, 150)
    glVertex(420, 140)

    glVertex(420, 140)
    glVertex(400, 140)

    glVertex(430, 130)
    glVertex(430, 150)

    glVertex(430, 150)
    glVertex(450, 150)

    glVertex(450, 150)
    glVertex(450, 130)

    glVertex(430, 140)
    glVertex(450, 140)

    glVertex(480, 150)
    glVertex(460, 150)

    glVertex(460, 150)
    glVertex(460, 130)

    glVertex(460, 130)
    glVertex(480, 130)

    glVertex(490, 150)
    glVertex(490, 130)

    glVertex(490, 150)
    glVertex(510, 150)

    glVertex(490, 140)
    glVertex(510, 140)

    glVertex(490, 130)
    glVertex(510, 130)

    glEnd()


def gameend():
    glColor3ub(0, 0, 0)
    glBegin(GL_POLYGON)
    glVertex(0, 0)
    glVertex(0, 2000)
    glVertex(2000, 2000)
    glVertex(2000, 0)
    glEnd()
    
    glColor3ub(120, 0, 0)
    glBegin(GL_POLYGON)
    glVertex(80, 280)
    glVertex(80, 480)
    glVertex(620, 480)
    glVertex(620, 280)
    glEnd()

    glColor3ub(150, 75, 0)
    glBegin(GL_POLYGON)
    glVertex(100, 300)
    glVertex(100, 460)
    glVertex(600, 460)
    glVertex(600, 300)
    glEnd()


    glColor3ub(150, 0, 0)
    glBegin(GL_POLYGON)
    glVertex(120, 320)
    glVertex(120, 440)
    glVertex(580, 440)
    glVertex(580, 320)
    glEnd()

    glColor3ub(255, 160, 160)
    glLineWidth(3)
    glBegin(GL_LINES)
    glVertex(180, 400)
    glVertex(140, 400)

    glVertex(140, 400)
    glVertex(140, 360)

    glVertex(140, 360)
    glVertex(180, 360)

    glVertex(180, 360)
    glVertex(180, 380)

    glVertex(180, 380)
    glVertex(160, 380)

    glVertex(200, 360)
    glVertex(220, 400)
    
    glVertex(220, 400)
    glVertex(240, 360)

    glVertex(210, 380)
    glVertex(230, 380)

    glVertex(260, 360)
    glVertex(260, 400)

    glVertex(260, 400)
    glVertex(280, 380)

    glVertex(280, 380)
    glVertex(300, 400)

    glVertex(300, 400)
    glVertex(300, 360)

    glVertex(320, 400)
    glVertex(320, 360)

    glVertex(320, 400)
    glVertex(360, 400)

    glVertex(320, 380)
    glVertex(340, 380)

    glVertex(320, 360)
    glVertex(360, 360)

    glVertex(400, 400)
    glVertex(400, 360)

    glVertex(400, 400)
    glVertex(440, 400)

    glVertex(400, 380)
    glVertex(420, 380)

    glVertex(400, 360)
    glVertex(440, 360)

    glVertex(460, 360)
    glVertex(460, 400)

    glVertex(460, 400)
    glVertex(500, 360)

    glVertex(500, 360)
    glVertex(500, 400)

    glVertex(520, 360)
    glVertex(520, 400)
    
    glVertex(520, 400)
    glVertex(540, 400)

    glVertex(540, 400)
    glVertex(560, 380)

    glVertex(560, 380)
    glVertex(540, 360)

    glVertex(540, 360)
    glVertex(520, 360)

    glEnd()

    glColor3ub(255, 160, 160)
    glLineWidth(3)
    glBegin(GL_LINES)
    glVertex(320, 200)
    glVertex(350, 220)
    
    glVertex(350, 220)
    glVertex(380, 200)

    glVertex(330, 200)
    glVertex(330, 180)

    glVertex(330, 180)
    glVertex(370, 180)

    glVertex(370, 180)
    glVertex(370, 200)

    glVertex(190, 150)
    glVertex(190, 130)

    glVertex(190, 150)
    glVertex(210, 150)

    glVertex(210, 150)
    glVertex(210, 140)

    glVertex(210, 140)
    glVertex(190, 140)

    glVertex(220, 130)
    glVertex(220, 150)

    glVertex(220, 150)
    glVertex(240, 150)

    glVertex(240, 150)
    glVertex(240, 140)

    glVertex(240, 140)
    glVertex(220, 140)

    glVertex(220, 140)
    glVertex(240, 130)

    glVertex(250, 150)
    glVertex(250, 130)

    glVertex(250, 150)
    glVertex(270, 150)

    glVertex(250, 140)
    glVertex(270, 140)

    glVertex(250, 130)
    glVertex(270, 130)

    glVertex(300, 150)
    glVertex(280, 150)

    glVertex(280, 150)
    glVertex(280, 140)

    glVertex(280, 140)
    glVertex(300, 140)

    glVertex(300, 140)
    glVertex(300, 130)

    glVertex(300, 130)
    glVertex(280, 130)

    glVertex(330, 150)
    glVertex(310, 150)

    glVertex(310, 150)
    glVertex(310, 140)

    glVertex(310, 140)
    glVertex(330, 140)

    glVertex(330, 140)
    glVertex(330, 130)
    
    glVertex(330, 130)
    glVertex(310, 130)

    glVertex(390, 150)
    glVertex(370, 150)
    
    glVertex(370, 150)
    glVertex(370, 140)

    glVertex(370, 140)
    glVertex(390, 140)

    glVertex(390, 140)
    glVertex(390, 130)

    glVertex(390, 130)
    glVertex(370, 130)

    glVertex(400, 130)
    glVertex(400, 150)

    glVertex(400, 150)
    glVertex(420, 150)

    glVertex(420, 150)
    glVertex(420, 140)

    glVertex(420, 140)
    glVertex(400, 140)

    glVertex(430, 130)
    glVertex(430, 150)

    glVertex(430, 150)
    glVertex(450, 150)

    glVertex(450, 150)
    glVertex(450, 130)

    glVertex(430, 140)
    glVertex(450, 140)

    glVertex(480, 150)
    glVertex(460, 150)

    glVertex(460, 150)
    glVertex(460, 130)

    glVertex(460, 130)
    glVertex(480, 130)

    glVertex(490, 150)
    glVertex(490, 130)

    glVertex(490, 150)
    glVertex(510, 150)

    glVertex(490, 140)
    glVertex(510, 140)

    glVertex(490, 130)
    glVertex(510, 130)

    glEnd()


# def iterate():
#     glViewport(0, 0, 1000, 1000)
#     glMatrixMode(GL_PROJECTION)
#     glLoadIdentity()
#     glOrtho(0, 1000, 0, 1000, 0.0, 1.0)
#     glMatrixMode (GL_MODELVIEW)
#     glLoadIdentity()
# def showScreen():
#     glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
#     glLoadIdentity()
#     iterate()
#     # victory()
#     gameend()
#     glutSwapBuffers()
    
# glutInit()
# glutInitDisplayMode(GLUT_RGBA)
# glutInitWindowSize(1000, 1000)
# glutInitWindowPosition(0, 0)
# wind = glutCreateWindow("OpenGL Coding Practice : GL_POLYGON")
# glutDisplayFunc(showScreen)
# glutIdleFunc(showScreen)
# glutMainLoop()
