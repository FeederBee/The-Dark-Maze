from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from Karakter import *
from Map.mazemap import *
from Karakter.Knight import *
from Karakter.Spider import *

# Ukuran
canvas=700
#set koordinat Knight
x_k=0
y_k=0

#set koordinat Spider (monster)
#x_s, y_s
x_s,y_s=0,0
x_s2,y_s2=0,0
mx,my=0,0
mx2,my2=0,0
#set animasi untuk gerakan karakter
rotate=1
char_scale=canvas/(800*0.701)

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
    global x_k,y_k,rotate 
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
    if x_k > 520:
        x_k = 520
    elif x_k < 0:
        x_k = 0
    elif y_k > 750:
        y_k = 750
    elif y_k < 0:
        y_k = 0
    #garis
    # 1
    elif (0<=x_k+10<=70 or 0<=x_k-10<=70) and (275-4<=y_k+20<=275 or 275-4<=y_k-15<=275):
        if y_k>275:
            y_k+=5
        elif y_k<275:
            y_k-=5
    #2
    elif (70<=x_k+10<=70 or 70<=x_k-10<=70) and (175<=y_k+20<=275 or 175<=y_k-15<=275):
        if x_k<65: x_k-=5
        elif x_k>65: x_k+=5
    # 3
    elif (70<=x_k+10<=70 or 70<=x_k-10<=70) and (75<=y_k+20<=175 or 75<=y_k-15<=175):
        if x_k<65: x_k-=5
        elif x_k>65: x_k+=5
    # 4
    elif (170<=x_k+10<=170 or 170<=x_k-10<=170) and (0<=y_k+20<=275 or 0<=y_k-15<=275):
        if x_k<165: x_k-=5
        elif x_k>165: x_k+=5
    # 5    
    elif (170<=x_k+10<=270 or 170<=x_k-10<=270) and (175-4<=y_k+20<=175 or 175-4<=y_k-15<=175):
        if y_k>175:
            y_k+=5
        elif y_k<175:
            y_k-=5
    # 6
    elif (270<=x_k+10<=670 or 270<=x_k-10<=670) and (75-4<=y_k+20<=75 or 75-4<=y_k-15<=75):
        if y_k>75:
            y_k+=5
        elif y_k<75:
            y_k-=5
    # 7
    elif (370<=x_k+10<=370 or 370<=x_k-10<=370) and (75<=y_k+20<=375 or 75<=y_k-15<=375):
        if x_k<365: x_k-=5
        elif x_k>365: x_k+=5
    # 8
    elif (270<=x_k+10<=570 or 270<=x_k-10<=570) and (275-4<=y_k+20<=275 or 275-4<=y_k-15<=275):
        if y_k>275:
            y_k+=5
        elif y_k<275:
            y_k-=5
    # 9
    elif (470<=x_k+10<=470 or 470<=x_k-10<=470) and (175<=y_k+20<=275 or 175<=y_k-15<=275):
        if x_k<465: x_k-=5
        elif x_k>465: x_k+=5
    # 10
    elif (470<=x_k+10<=670 or 470<=x_k-10<=670) and (175-4<=y_k+20<=175 or 175-4<=y_k-15<=175):
        if y_k>175:
            y_k+=5
        elif y_k<175:
            y_k-=5
    # 11
    elif (670<=x_k+10<=670 or 670<=x_k-10<=670) and (175<=y_k+20<=275 or 175<=y_k-15<=275):
        if x_k<665: x_k-=5
        elif x_k>665: x_k+=5
    # 12
    elif (370<=x_k+10<=670 or 370<=x_k-10<=670) and (375-4<=y_k+20<=375 or 375-4<=y_k-15<=375):
        if y_k>375:
            y_k+=5
        elif y_k<375:
            y_k-=5
    # 13    
    elif (670<=x_k+10<=670 or 670<=x_k-10<=670) and (375<=y_k+20<=675 or 375<=y_k-15<=675):
        if x_k<665: x_k-=5
        elif x_k>665: x_k+=5
    # 14
    elif (70<=x_k+10<=70 or 70<=x_k-10<=70) and (475<=y_k+20<=675 or 475<=y_k-15<=675):
        if x_k<65: x_k-=5
        elif x_k>65: x_k+=5
    # 15
    elif (70<=x_k+10<=370 or 70<=x_k-10<=370) and (675-4<=y_k+20<=675 or 675-4<=y_k-15<=675):
        if y_k>675:
            y_k+=5
        elif y_k<675:
            y_k-=5
    # 16
    elif (370<=x_k+10<=370 or 370<=x_k-10<=370) and (575<=y_k+20<=675 or 575<=y_k-15<=675):
        if x_k<365: x_k-=5
        elif x_k>365: x_k+=5
    # 17    
    elif (270<=x_k+10<=270 or 270<=x_k-10<=270) and (375<=y_k+20<=575 or 375<=y_k-15<=575):
        if x_k<265: x_k-=5
        elif x_k>265: x_k+=5
    # 18
    elif (270<=x_k+10<=470 or 270<=x_k-10<=470) and (475-4<=y_k+20<=475 or 475-4<=y_k-15<=475):
        if y_k>475:
            y_k+=5
        elif y_k<475:
            y_k-=5
    # 19
    elif (270<=x_k+10<=570 or 270<=x_k-10<=570) and (575-4<=y_k+20<=575 or 575-4<=y_k-15<=575):
        if y_k>575:
            y_k+=5
        elif y_k<575:
            y_k-=5
    # 20
    elif (570<=x_k+10<=570 or 570<=x_k-10<=570) and (475<=y_k+20<=675 or 475<=y_k-15<=675):
        if x_k<565: x_k-=5
        elif x_k>565: x_k+=5
    # 21
    elif (570<=x_k+10<=770 or 570<=x_k-10<=770) and (675-4<=y_k+20<=675 or 675-4<=y_k-15<=675):
        if y_k>675:
            y_k+=5
        elif y_k<675:
            y_k-=5
    # 22
    elif (0<=x_k+10<=170 or 0<=x_k-10<=170) and (375-4<=y_k+20<=375 or 375-4<=y_k-15<=375):
        if y_k>375:
            y_k+=5
        elif y_k<375:
            y_k-=5
    # 23
    elif (170<=x_k+10<=170 or 170<=x_k-10<=170) and (375<=y_k+20<=575 or 375<=y_k-15<=575):
        if x_k<165: x_k-=5
        elif x_k>165: x_k+=5
    # 24
    elif (470<=x_k+10<=470 or 470<=x_k-10<=470) and (675<=y_k+20<=775 or 675<=y_k-15<=775):
        if x_k<465: x_k-=5
        elif x_k>465: x_k+=5

    glPopMatrix()

def spider1():
    global x_s, y_s, mx,my
    arah='x'
    glPushMatrix()
    glTranslate(5,320,0)
    glTranslate(x_s,y_s,0)
    #titik awal (5,320)
    if arah=='x':
    #x=220 -> kebawah
    #x=330 -> kebawah
        if x_s<=0 : mx=0.1
        elif x_s>=200: 
            if x_s>=220 or x_s>=330:
                arah='y'
            mx=-0.1
    elif arah=='y':
    #y=220 -> kekanan
    #y=120 -> kekiri
        if y_s==0 or y_s<=-4.5 : 
            if y_s>=220:
                arah='x'
            my=0.5
        elif y_s>250: 
            if y_s>=120:
                arah='x'
            my=-0.5
    else:
        mx=0
        my=0
    x_s+=mx
    y_s+=my

    glScale(5, 5, 0.0)
    laba()
    glPopMatrix()

def spider2():
    global x_s2, y_s2,mx2,my2
    # arah = 'sumbu x'
    glPushMatrix()
    glTranslate(100,600,0)
    glTranslate(x_s2,y_s2,0)
    if True:
        if x_s2<=0 : mx2=0.1
        elif x_s2>=200: mx2=-0.1
    else:
        mx2=0
        my2=0
    x_s2+=mx2
    y_s2+=my2

    glScale(5, 5, 0.0)
    laba()
    glPopMatrix()

def collision():
    global x_s,y_s,x_k,y_k,x_s2,y_s2
    #Spider1
    if (x_s+5-20<=x_k+10<=x_s+5+20 or x_s+5-20<=x_k-10<=x_s+5+20) and (y_s+320-20<=y_k+15<=y_s+320+20 or y_s+320-20<=y_k-2<=y_s+320+20):
        print('collision 1')
    elif (x_s+5-10<=x_k+10<=x_s+5+10 or x_s+5-10<=x_k-10<=x_s+5+10):
        print('Overlap sumbu x')
    elif (y_s+300-2<=y_k+2<=y_s+300+40 or y_s+300-10<=y_k-2<=y_s+300+40):
        print('Overlap sumbu y')
    #Spider2
    if (x_s2+100-20<=x_k+10<=x_s2+100+20 or x_s2+100-20<=x_k-10<=x_s2+100+20) and (y_s2+600-20<=y_k+15<=y_s2+600+20 or y_s2+600-20<=y_k-2<=y_s2+600+20):
        print('collision 2')
    elif (x_s2+100-10<=x_k+10<=x_s2+100+10 or x_s2+100-10<=x_k-10<=x_s2+100+10):
        print('Overlap sumbu x')
    elif (y_s2+580-2<=y_k+2<=y_s2+580+40 or y_s2+580-10<=y_k-2<=y_s2+580+40):
        print('Overlap sumbu y')
    else :
        print('None')

def update(value):
    glutPostRedisplay()
    glutTimerFunc(10,update,0)

def iterate():
    glViewport(0, 0, canvas, canvas)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glColor3ub(50, 50, 50)
    glOrtho(-0, canvas, -0, canvas, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def level2():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    glScaled(char_scale,char_scale,0)
    bg(800*0.7,800*0.7)
    maze2()
    glTranslate(30,30,0)
    knight_move()
    spider1()
    spider2()
    collision()
    glutSwapBuffers()

def level2_main():
    glutInit()
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(canvas, canvas)
    glutInitWindowPosition(0, 0)
    wind = glutCreateWindow("The Dungeon")
    glutDisplayFunc(level2)
    glutIdleFunc(level2)
    glutSpecialFunc(input_keyboard)
    glutTimerFunc(1,update,0)
    glutMainLoop()

level2_main()