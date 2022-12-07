from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


def knight():
    glColor3f(0.2,0.2,0.2)
    glScaled(5,5,0)
    glBegin(GL_POLYGON)   
    #Kaki Kiri
    glVertex2f(-2.9335231425966, 2.8673369924097)#C
    glVertex2f(-0.6835231425966, 2.8673369924097)#D
    glVertex2f(-0.6835231425966, 1.0673369924097)#E
    glVertex2f(-2.9335231425966, 1.0673369924097)#F
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(-2.4835231425966, 3.3173369924097)#H
    glVertex2f(-1.1565231425966, 3.3173369924097)#I
    glVertex2f(-1.1565231425966, 2.8673369924097)#J
    glVertex2f(-2.4835231425966, 2.8673369924097)#G
    glEnd()
    glBegin(GL_POLYGON)
    #Kaki Kanan
    glVertex2f(2.9335231425966, 2.8673369924097)#N
    glVertex2f(0.6835231425966, 2.8673369924097)#M
    glVertex2f(0.6835231425966, 1.0673369924097)#P
    glVertex2f(2.9335231425966, 1.0673369924097)#O
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(2.4835231425966, 3.3173369924097)#S
    glVertex2f(1.1565231425966, 3.3173369924097)#R
    glVertex2f(1.1565231425966, 2.8673369924097)#Q
    glVertex2f(2.4835231425966, 2.8673369924097)#T
    glEnd()
    #Pundak dan Kepala
    glBegin(GL_POLYGON)
    glVertex2f(-2.9335231425966, -1.6580737266661)#W
    glVertex2f(2.9335231425966, -1.6580737266661)#A1
    glVertex2f(2.9335231425966, 1.955)#B1 
    glVertex2f(-2.9335231425966, 1.955)#Z
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(-3.86, 1.0673369924097)#C1
    glVertex2f(3.86, 1.0673369924097)#D1
    glVertex2f(3.86, -1.22)#E1
    glVertex2f(-3.86, -1.22)#F1
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(-4.32, 0.6)#G1
    glVertex2f(4.32, 0.6)#H1
    glVertex2f(4.32, -0.76)#I1
    glVertex2f(-4.32, -0.76)#J1
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(-1.596, -1.6580737266661)#K1
    glVertex2f(1.6, -1.6580737266661)#L1
    glVertex2f(1.6, -2.15)#M1
    glVertex2f(-1.596, -2.15)#R1
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(-1.1686940008555, -2.15)#Q1
    glVertex2f(1.1565231425966, -2.15)#N1
    glVertex2f(1.1565231425966, -2.5789599504434)#O1
    glVertex2f(-1.1686940008555, -2.5789599504434)#P1
    glEnd()

    glColor3f(0.73,0.75,0.8)
    #Kaki Kiri
    glBegin(GL_POLYGON)
    glVertex2f(-1.1565231425966, 2.8673369924097)#J
    glVertex2f(-2.4835231425966, 2.8673369924097)#G
    glVertex2f(-2.4835231425966, 1.5331766904738)#L
    glVertex2f(-1.1565231425966, 1.5331766904738)#K
    glEnd()

    #Kaki Kanan
    glBegin(GL_POLYGON)
    glVertex2f(1.1565231425966, 2.8673369924097)#Q
    glVertex2f(2.4835231425966, 2.8673369924097)#T
    glVertex2f(2.4835231425966, 1.5331766904738)#U
    glVertex2f(1.1565231425966, 1.5331766904738)#V
    glEnd()

    #Kepala
    glBegin(GL_POLYGON)
    glVertex2f(-1.1686940008555, -1.6580737266661)#S1
    glVertex2f(1.1565231425966, -1.6580737266661)#T1
    glVertex2f(1.1565231425966, 1.0673369924097)#U1
    glVertex2f(-1.1686940008555, 1.0673369924097)#V1
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(-1.596, 0.15)#W1
    glVertex2f(1.6, 0.15)#Z1
    glVertex2f(1.6, -1.22)#A2
    glVertex2f(-1.596, -1.22)#B2
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(-0.6835231425966, -2.1018861089941)#C2
    glVertex2f(0.687, -2.1018861089941)#D2
    glVertex2f(0.687, 1.5)#E2
    glVertex2f(-0.6835231425966, 1.5)#F2
    glEnd()
    # Pundak Kiri
    glBegin(GL_POLYGON)
    glVertex2f(-2.4835231425966, 0.6)#J2
    glVertex2f(-2.4835231425966, 1.0673369924097)#G2
    glVertex2f(-1.58, 1.0673369924097)#H2
    glVertex2f(-1.58, 0.6)#I2
    glVertex2f(-2.06, 0.6)#n2
    glVertex2f(-2.06, -0.76)#M2
    glVertex2f(-2.964, -0.76)#L2
    glVertex2f(-2.964, 0.6)#K2
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(-2.4835231425966, -0.76)#O2
    glVertex2f(-2.06, -0.76)#M2
    glVertex2f(-2.06, -1.22)#Q2
    glVertex2f(-2.4835231425966, -1.22)#P2
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(-3.86, 0.6)#R2
    glVertex2f(-3.437, 0.6)#S2
    glVertex2f(-3.437, -0.76)#T2
    glVertex2f(-3.86, -0.76)#U2
    glEnd()
    #Pundak Kanan
    glBegin(GL_POLYGON)
    glVertex2f(2.4835231425966, 0.6)#J2
    glVertex2f(2.4835231425966, 1.0673369924097)#G2
    glVertex2f(1.58, 1.0673369924097)#H2
    glVertex2f(1.58, 0.6)#I2
    glVertex2f(2.06, 0.6)#n2
    glVertex2f(2.06, -0.76)#M2
    glVertex2f(2.964, -0.76)#L2
    glVertex2f(2.964, 0.6)#K2
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(2.4835231425966, -0.76)#O2
    glVertex2f(2.06, -0.76)#M2
    glVertex2f(2.06, -1.22)#Q2
    glVertex2f(2.4835231425966, -1.22)#P2
    glEnd()
    glBegin(GL_POLYGON)
    glVertex2f(3.86, 0.6)#R2
    glVertex2f(3.437, 0.6)#S2
    glVertex2f(3.437, -0.76)#T2
    glVertex2f(3.86, -0.76)#U2
    glEnd()


def hadap_atas():
    knight()

def hadap_bawah():
    glRotatef(180,0.0,0.0,1.0)
    knight()

def hadap_kiri():
    glRotatef(90,0.0,0.0,1.0)
    knight()

def hadap_kanan():
    glRotatef(-90,0.0,0.0,1.0)
    knight()



# # Cek :
# def iterate():
#     glViewport(0, 0, 500, 500)
#     glMatrixMode(GL_PROJECTION)
#     glLoadIdentity()
#     glOrtho(-5, 5, -3, 4, 0.0, 1.0)
#     glMatrixMode (GL_MODELVIEW)
#     glLoadIdentity()
# def showScreen():
#     glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
#     glLoadIdentity()
#     iterate()
#     hadap_bawah()
#     glutSwapBuffers()
    
# glutInit()
# glutInitDisplayMode(GLUT_RGBA)
# glutInitWindowSize(500, 500)
# glutInitWindowPosition(0, 0)
# wind = glutCreateWindow("OpenGL Coding Practice : GL_POLYGON")
# glutDisplayFunc(showScreen)
# glutIdleFunc(showScreen)
# glutMainLoop()
