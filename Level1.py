from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from Karakter import *
from Map.mazemap import *
from Karakter.Knight import *
from Karakter.Spider import *
from Karakter.princess import*
from label import *

from Main import *
# from Main import *

gameover = False
tamat = False

# #set koordinat Knight
# x_k=0
# y_k=0

# #set koordinat Spider (monster)
# #x_s, y_s
# x_s=0
# y_s=0
mx,my=0,0

#set koordinat princess
x_p = 455
y_p = 200

#set animasi untuk gerakan karakter
rotate=1
arah = 'sumbu y'

char_scale=2

game=None

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

def knight_move():
    global x_k,y_k,rotate, game
    glPushMatrix()
    glTranslate(x_k,y_k,0)
    if rotate==1:
        hadap_atas()
    elif rotate==2:
        hadap_bawah()
    elif rotate==3:
        hadap_kanan()
    elif rotate==4:
        hadap_kiri()
    else:
        hadap_atas()
    if x_k > 455:
        x_k = 455
    elif x_k < 0:
        x_k = 0
    elif y_k > 455:
        y_k = 455
    elif y_k < 0:
        y_k = 0
    #1
    elif (0<=x_k+10<=270 or 0<=x_k-10<=270) and (75-4<=y_k+20<=75 or 75-4<=y_k-15<=75):
        if y_k>75:
            y_k+=5
        elif y_k<75:
            y_k-=5
        if 250>x_k>270:
            x_k=275
    #2
    elif (370<=x_k+10<=370 or 370<=x_k-10<=370) and (0<=y_k+20<=75 or 0<=y_k-15<=75):
        if x_k<365: x_k-=5
        elif x_k>365: x_k+=5
    #3
    elif (70<=x_k+10<=70 or 70<=x_k-10<=70) and (175-4<=y_k+20<=375 or 175-4<=y_k-15<=375):
        if x_k<65: x_k-=5
        elif x_k>75: x_k+=5
    #4
    elif (70<=x_k+10<=170 or 70<=x_k-10<=170) and (375-4<=y_k+20<=375 or 375-4<=y_k-15<=375):
        if y_k>375:
            y_k+=5
        elif y_k<375:
            y_k-=5
    #5
    elif (170<=x_k+10<=170 or 170<=x_k-10<=170) and (175-4<=y_k+20<=375 or 175-4<=y_k-15<=375):
        if x_k<165: x_k-=5
        elif x_k>175: x_k+=5
    #6
    elif (170<=x_k+10<=470 or 170<=x_k-10<=470) and (175-4<=y_k+20<=175 or 175-4<=y_k-15<=175):
        if y_k>175:
            y_k+=5
        elif y_k<175:
            y_k-=5
    #7
    elif (370<=x_k+10<=370 or 370<=x_k-10<=370) and (370-4<=y_k+20<=475 or 370-4<=y_k-15<=475):
        if x_k<365: x_k-=5
        elif x_k>375: x_k+=5
    #8
    elif (270<=x_k+10<=270 or 270<=x_k-10<=270) and (270-4<=y_k+20<=375 or 270-4<=y_k-15<=375):
        if x_k<275: x_k-=5
        elif x_k>275: x_k+=5
    #9
    elif (270<=x_k+10<=470 or 270<=x_k-10<=470) and (275-4<=y_k+20<=275 or 275-4<=y_k-15<=275):
        if y_k>275:
            y_k+=5
        elif y_k<275:
            y_k-=5
    #10
    elif 460<x_k+10<490 and 490<y_k<490:
        game = 'victory'

    glPopMatrix()



def spider():
    global x_s, y_s, state, mx,my, arah
    glPushMatrix()
    glTranslate(200,200,0)
    glTranslate(x_s,y_s,0)
    if arah=='sumbu x':
        if x_s<=0: mx=1
        elif x_s>40 or x_s>=0: mx=-1
    if arah=='sumbu y':
        if y_s==0 or y_s<=-4.5: my=0.1
        elif y_s>250: my=-0.1
    else:
        mx=0
        my=0
    x_s+=mx
    y_s+=my

    glScale(5, 5, 0.0)
    laba()
    glPopMatrix()

def princes():
    global x_p, y_p
    # glTranslated(465, 185, 0)i
    glPushMatrix()
    glTranslated(x_p,y_p,0)
    glScaled(0.1,0.1,0)
    glRotated(-180,0,1,0)
    princess()
    glPopMatrix()

def labelend():
    glTranslatef(-60, -50, 0)
    glScaled(0.8, 0.8,0)
    gameend()

def labelvictory():
    glTranslatef(-60, -50, 0)
    glScaled(0.8, 0.8,0)
    victory()


def collision():
    global x_s,y_s,x_k,y_k, gameover, tamat
    if (x_s+200-20<=x_k+10<=x_s+200+20 or x_s+200-20<=x_k-10<=x_s+200+20) and (y_s+200-20<=y_k+15<=y_s+200+20 or y_s+200-20<=y_k-2<=y_s+200+20):
        gameover = True
    # elif (x_s+200-10<=x_k+10<=x_s+200+10 or x_s+200-10<=x_k-10<=x_s+200+10):
    #     print('Overlap sumbu x')
    # elif (y_s+180-2<=y_k+2<=y_s+180+40 or y_s+180-10<=y_k-2<=y_s+180+40):
    #     print('Overlap sumbu y')
    if (x_p-40<=x_k<=x_p+20) and (y_p-20<=y_k<=y_p+40):
        tamat = True
    else :
        None

def gamestateover():
    global gameover
    if gameover == True and tamat==False:
        labelend()
    else:
        princes()

def gamestatefinish():
    global tamat
    if tamat == True:
        labelvictory()


def update(value):
    glutPostRedisplay()
    glutTimerFunc(10,update,0)

def iterate():
    glViewport(0, 0, 700, 700)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glColor3ub(50, 50, 50)
    glOrtho(-0, 700, -0, 700, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def level1():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glScaled(char_scale,char_scale,0)
    bg(500*0.7,500*0.7)
    maze1()
    glTranslate(30,30,0)
    knight_move()
    spider()
    collision()
    gamestateover()
    gamestatefinish()
    # print(x_p, y_p)
    # print(x_k, y_k)
    glutSwapBuffers()

def level1_main():
    glutInit()
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(700, 700)
    glutInitWindowPosition(400, 60)
    wind = glutCreateWindow("The Dungeon")
    glutDisplayFunc(level1)
    glutIdleFunc(level1)
    glutSpecialFunc(input_keyboard)
    glutTimerFunc(1,update,0)
    glutMainLoop()

# level1_main()