from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from Menu.menu import *
from Level1 import *
from Level2 import *
from Level3 import *

# import Level1
# import Level2
# import Level3

# BUTTON_STATE= menu.BUTTONCLICK
# Key=menu.Keyb
#set koordinat Knight
x_k=0
y_k=0

#set koordinat Spider (monster)
#x_s, y_s
x_s=0
y_s=0

Key=Key

def input_keyboard(key,x,y):
    global x_k,y_k,rotate
    if key == GLUT_KEY_UP:
        rotate=1
        y_k+=5
    elif key == GLUT_KEY_DOWN:
        rotate=2
        y_k -= 5
    elif key == GLUT_KEY_RIGHT:
        rotate=3
        x_k+= 5
    elif key == GLUT_KEY_LEFT:
        rotate=4
        x_k -= 5


def colliMouse(x,y):
    global Key
    x=-350+x
    y=350-y
    if -80<= x<=80 and -20<= y <=20 :
        Key=1
    elif -80<= x<=80 and -85<= y <=-45 :
        Key=2
    elif -80<= x<=80 and -150<= y <=-110 :
        Key=3
    print(Key)

def input_mouse(button, state, x, y):
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        colliMouse(x,y)

def update(value):
    glutPostRedisplay()
    glutTimerFunc(10,update,0)

def scane():
    global Key, p
    glutInit()
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(700, 700)
    glutInitWindowPosition(0, 0)
    wind = glutCreateWindow("OpenGL Coding Practice : GL_POLYGON")
    if Key==0:
        # menu()
        main_menu()
        # glutDestroyWindow(menu)
    if Key==1:
        #Menjalanakn level1
        # level1()
        level1_main()
    if Key==2:
        #RUN LEVEL2
        # level2()
        level2_main()
        # knight_move()
    if Key==3:
        # level3()
        level3_main()
    print(Key)

    glutTimerFunc(1,update,0)
    glutMainLoop()

# def main_menu():
#     glutInit()
#     glutInitDisplayMode(GLUT_RGBA)
#     glutInitWindowSize(700, 700)
#     glutInitWindowPosition(0, 0)
#     wind = glutCreateWindow("OpenGL Coding Practice : GL_POLYGON")
#     glutDisplayFunc(scane)
#     glutIdleFunc(scane)
#     glutSpecialFunc(input_keyboard)
#     glutMouseFunc(input_mouse)
#     glutTimerFunc(1,update,0)
#     glutMainLoop()

scane()