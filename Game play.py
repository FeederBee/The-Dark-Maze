from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from gerak import *
from Karakter import *
# from Karakter.Love import love

#Ukuran canvas
lebar = 60
panjang = 60

def init():
    glClearColor(0.0, 0.0, 0.0, 1.0)
    gluOrtho2D(-panjang, lebar, -lebar, panjang)

def display():
    glClear(GL_COLOR_BUFFER_BIT)
    knight_mov()
    spider_mov()
    # love()
    collision()
    glFlush()

def update(value):
    glutPostRedisplay()
    glutTimerFunc(10,update,0)

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_SINGLE|GLUT_RGB)
    glutInitWindowSize(500,500)
    glutInitWindowPosition(100,100)
    glutCreateWindow("knight")
    glutDisplayFunc(display)
    glutSpecialFunc(input_keyboard)
    glutTimerFunc(1,update,0)
    init()
    glutMainLoop()

main()