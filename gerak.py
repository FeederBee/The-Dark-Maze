from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from Karakter.Knight import *
from Karakter.Spider import *

#set koordinat Knight
x_k=0
y_k=0

#set koordinat Spider (monster)
#x_s, y_s
x_s=0
y_s=0

#set animasi untuk gerakan karakter
rotate=1

def input_keyboard(key,x,y):
    global x_k,y_k,rotate
    if key == GLUT_KEY_UP:
        rotate=1
        y_k+=1
    elif key == GLUT_KEY_DOWN:
        rotate=2
        y_k -= 1
    elif key == GLUT_KEY_RIGHT:
        rotate=3
        x_k+= 1
    elif key == GLUT_KEY_LEFT:
        rotate=4
        x_k -= 1 

def auto_move():
    global x_s,y_s
    for i in range(10):
        if x_s==0 :
            if x_s>6:
                x_s-=1
            elif x_s>-6:
                x_s+=1
            else:
                x_s+=0
        if y_s==0:
            if y_s>6:
                y_s-=1
            elif y_s>-6:
                y_s+=1
            else:
                y_s+=0
    

def knight_mov():
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
    if x_k > 57:
        x_k = 57
    elif x_k < -57:
        x_k = -57
    elif y_k > 57:
        y_k = 57
    elif y_k < -57:
        y_k = -57

    glPopMatrix()

def spider_mov():
    global x_s, y_s, rotate
    glPushMatrix()
    glScale(1.5, 1.5, 0.0)
    glTranslate(x_s,y_s,0)
    auto_move()
    glPopMatrix()

def collision():
    if (x_s-3.5<=x_k+3.5<=x_s+3.5 or x_s-3.5<=x_k-3.5<=x_s+3.5) and (y_s-3.5<=y_k+3.5<=y_s+3.5 or y_s-3.5<=y_k-3.5<=y_s+3.5):
        print('colli')
    elif (x_s-2<=x_k+3.5<=x_s+3.5 or x_s-3.5<=x_k-3.5<=x_s+3.5):
        print('Overlap sumbu x')
    elif (y_s-2<=y_k+2<=y_s+3.5 or y_s-3.5<=y_k-3.5<=y_s+3.5):
        print('Overlap sumbu y')
    else :
        print('None')
