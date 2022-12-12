from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from Karakter import *
from Map.mazemap import *
from Karakter.Knight import *
from Karakter.Spider import *
from Karakter.princess import *
from label import *


canvas=700

gameover = False
tamat = False

x_p,x_p2,x_p3 = 455,520,960
y_p,y_p2,y_p3 = 200,680,-430

#set koordinat Knight
x_k=0
y_k=0

char_scale=2
char_scale2=canvas/(800*0.701)


#set koordinat Spider (monster)
#x_s, y_s
x_s,y_s,x_s2,y_s2,x_s3,y_s3 =0,0,0,0,0,0
mx,my,mx2,my2,mx3,my3 =0,0,0,0,0,0

tran_xs = [35,250,850] 
tran_ys = [550,650,330]

tran_xk=30-60
tran_yk=950

#set pergantian sisi untuk gerakan karakter 
rotate=1 #knight
stat,stat2,stat3=0,0,0 #spider
scl=0.7
arah = 'sumbu y'

speed=0.5
game=None


#Menu
Key = 0


def blok():
    glColor3ub(60, 60, 60)
    glBegin(GL_POLYGON)
    glVertex2f(-300, 150)
    glVertex2f(-300, 300)
    glVertex2f(300, 300)
    glVertex2f(300, 150)
    glEnd()
    #LEVEL1
    glBegin(GL_POLYGON)
    glVertex2f(-160, 40)
    glVertex2f(160, 40)
    glVertex2f(160, -40)
    glVertex2f(-160, -40)
    glEnd()
    # LEVEL2
    glBegin(GL_POLYGON)
    glVertex2f(-160, -90)
    glVertex2f(160, -90)
    glVertex2f(160, -170)
    glVertex2f(-160, -170)
    glEnd()
    #LEVEL3
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


#Level1
def knight_move1():
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

def spider1_():
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

def collision1():
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


def level1():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate1()
    glScaled(char_scale,char_scale,0)
    bg(500*0.7,500*0.7)
    maze1()
    glTranslate(30,30,0)
    knight_move1()
    spider1_()
    collision1()
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


#Level 2
def princes2():
    global x_p2, y_p2
    # glTranslated(520, 700, 0)
    glTranslate(x_p2, y_p2, 0)
    glScaled(0.08,0.1,0)
    glRotated(-180,0,1,0)
    princess()

def knight_move2():
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

def spider1_2():
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

def spider2_2():
    global x_s2, y_s2,mx2,my2
    # arah = 'sumbu x'
    glPushMatrix()
    glTranslate(100,600,0)
    glTranslate(x_s2,y_s2,0)
    if True:
        if x_s2<=0 : mx2=0.05
        elif x_s2>=200: mx2=-0.05
    else:
        mx2=0
        my2=0
    x_s2+=mx2
    y_s2+=my2

    glScale(5, 5, 0.0)
    laba()
    glPopMatrix()

def collision2():
    global x_s,y_s,x_k,y_k,x_s2,y_s2, gameover, tamat
    #Spider1
    if (x_s+5-20<=x_k+10<=x_s+5+20 or x_s+5-20<=x_k-10<=x_s+5+20) and (y_s+320-20<=y_k+15<=y_s+320+20 or y_s+320-20<=y_k-2<=y_s+320+20):
        gameover = True
    # elif (x_s+5-10<=x_k+10<=x_s+5+10 or x_s+5-10<=x_k-10<=x_s+5+10):
    #     print('Overlap sumbu x')
    # elif (y_s+300-2<=y_k+2<=y_s+300+40 or y_s+300-10<=y_k-2<=y_s+300+40):
    #     print('Overlap sumbu y')
    #Spider2
    if (x_s2+100-20<=x_k+10<=x_s2+100+20 or x_s2+100-20<=x_k-10<=x_s2+100+20) and (y_s2+600-20<=y_k+15<=y_s2+600+20 or y_s2+600-20<=y_k-2<=y_s2+600+20):
        gameover = True
    # elif (x_s2+100-10<=x_k+10<=x_s2+100+10 or x_s2+100-10<=x_k-10<=x_s2+100+10):
    #     print('Overlap sumbu x')
    # elif (y_s2+580-2<=y_k+2<=y_s2+580+40 or y_s2+580-10<=y_k-2<=y_s2+580+40):
    #     print('Overlap sumbu y')

    if (x_p-35<=x_k<=x_p) and (y_p-10<=y_k<=y_p+50):
        tamat = True

def labelend2():
    glTranslated(-60, -27, 0)
    glScaled(0.9, 0.9,0)
    gameend()

def labelvictory2():
    glTranslated(-60, -27, 0)
    glScaled(0.9, 0.9, 0)
    victory()

def gamestateover2():
    global gameover
    if gameover == True and tamat==False:
        labelend2()

def gamestatefinish2():
    global tamat
    if tamat == True and gameover==False:
        labelvictory2()
    elif tamat==False and gameover==False:
        princes2()

def level2():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate1()
    glScaled(char_scale2,char_scale2,0)
    bg(800*0.7,800*0.7)
    maze2()
    glTranslate(30,30,0)
    knight_move2()
    spider1_2()
    spider2_2()
    collision2()
    gamestateover2()
    gamestatefinish2()
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



#Level 3
def knight_move3():
    global x_k,y_k,rotate, scl
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
    if x_k > 950:
        x_k = 950
    elif x_k < -5:
        x_k = -5
    elif y_k > 25:
        y_k = 25
    elif y_k <= -930:
        y_k = -930
    #garis
    # glVertex(0, 900)
    # glVertex(300 , 900)
    #Done
    elif -70<=y_k<=-35 and -5<=x_k<=290:
        if y_k>=-35: y_k+=5
        elif y_k<=-70: y_k-=5

    #vertikal
    elif -255<=y_k+10<=25 and 360<=x_k+10<=395:
        if 360<x_k<=395: x_k+=5
        elif x_k<=360: x_k-=5
    #horizontal
    elif -170<=y_k<=-130 and 65<=x_k+10<=395:
        if y_k>=-130: y_k+=5
        elif y_k<=-170: y_k-=5

    elif -170<=y_k<=-130 and 140<=x_k+10<=165:
        if 140<x_k<=165: x_k+=5
        elif x_k<=140: x_k-=5

    elif -370<=y_k<=-330 and -5<=x_k<=80:
        if y_k>=-330: y_k+=5
        elif y_k<=-370: y_k-=5

    elif -370<=y_k<=-330 and 70-20<=x_k<=90:
        if x_k>=90: x_k+=5
        elif x_k<=70-20: x_k-=5

    elif -545<=y_k<=-170 and 160<=x_k+10<=175:
        if 160<x_k<=175: x_k+=5
        elif x_k<=160: x_k-=5

    elif -470<=y_k<=-430 and 70<=x_k<=175:
        if y_k>=-430: y_k+=5
        elif y_k<=-470: y_k-=5

    elif -450<=y_k<=-650 and 50<=x_k+10<=90:
        if 50<x_k<=90: x_k+=5
        elif x_k<=50: x_k-=5

    # 70,-255
    # 70,-350
    elif -350<=y_k+10<=-250 and 60<=x_k+10<=95:
        if 60<x_k<=95: x_k+=5
        elif x_k<=60: x_k-=5

    # 70,-450
    # 70,-650
    elif -650<=y_k+10<=-450 and 60<=x_k+10<=95:
        if 60<x_k<=95: x_k+=5
        elif x_k<=60: x_k-=5

    # (70,-650)
    # (370,-650)
    elif -670<=y_k<=-635 and 75<=x_k<=390:
        if y_k>=-635: y_k+=5
        elif y_k<=-670: y_k-=5

    # (270,-650)
    # (270,-750)
    elif -755<=y_k+10<=-655 and 270-10<=x_k+10<=270+15:
        if 270-10<x_k<=270+15: x_k+=5
        elif x_k<=270+10: x_k-=5

    # (170,-650)
    # (170,-750)
    elif -750<=y_k+10<=-650 and 160<=x_k+10<=195:
        if 160<x_k<=195: x_k+=5
        elif x_k<=160: x_k-=5

    # (275,-750)
    # (475,-750)
    elif -770<=y_k<=-735 and 275<=x_k<=490:
        if y_k>=-735: y_k+=5
        elif y_k<=-770: y_k-=5

    # (70,-750)
    # (70,-850)
    elif -855<=y_k+10<=-775 and 70-10<=x_k+10<=70+15:
        if 60<x_k<=85: x_k+=5
        elif x_k<=60: x_k-=5

    # (570,-850)
    # (570,-550)
    elif -855<=y_k+10<=-555 and 560<=x_k+10<=585:
        if 560<x_k<=585: x_k+=5
        elif x_k<=560: x_k-=5

    # (270,-255)
    # (270,-350)
    elif -255<=y_k+10<=-350 and 260<=x_k+10<=285:
        if 260<x_k<=295: x_k+=5
        elif x_k<=260: x_k-=5

    # (270,-350)
    # (170,-350)
    elif -370<=y_k<=-335 and 175<=x_k<=290:
        if y_k>=-335: y_k+=5
        elif y_k<=-370: y_k-=5

    # (370,-350)
    # (370,-550)
    elif -550<=y_k+10<=-350 and 360<=x_k+10<=395:
        if 360<x_k<=395: x_k+=5
        elif x_k<=360: x_k-=5

    # (270,-550)
    # (470,-550)
    elif -570<=y_k<=-535 and 275<=x_k<=490:
        if y_k>=-535: y_k+=5
        elif y_k<=-570: y_k-=5

    # (270,-550)
    # (270,-450)
    elif -550<=y_k+10<=-450 and 260<=x_k+10<=295:
        if 260<x_k<=295: x_k+=5
        elif x_k<=260: x_k-=5

    # (470,-450)
    # (470,-650)
    elif -650<=y_k+10<=-450 and 460<=x_k+10<=495:
        if 460<x_k<=495: x_k+=5
        elif x_k<=460: x_k-=5

    # (670,-750)
    # 670,-930
    elif -930<=y_k+10<=-750 and 660<=x_k+10<=695:
        if 660<x_k<=695: x_k+=5
        elif x_k<=660: x_k-=5

    # 670,-850
    # 870,-850
    elif -870<=y_k<=-835 and 675<=x_k<=890:
        if y_k>=-835: y_k+=5
        elif y_k<=-870: y_k-=5


    # 770,-850
    # 770,-650
    elif -850<=y_k+10<=-650 and 760<=x_k+10<=795:
        if 760<x_k<=795: x_k+=5
        elif x_k<=760: x_k-=5

    # 870,-650
    # 870,-750
    elif -750<=y_k+10<=-650 and 860<=x_k+10<=895:
        if 860<x_k<=895: x_k+=5
        elif x_k<=860: x_k-=5

    # 870,-650
    # 950,-650
    elif -670<=y_k<=-635 and 875<=x_k<=970:
        if y_k>=-635: y_k+=5
        elif y_k<=-670: y_k-=5

    # 870,-550
    # 670,-550
    elif -570<=y_k<=-535 and 675<=x_k<=890:
        if y_k>=-535: y_k+=5
        elif y_k<=-570: y_k-=5   

    # 670,-350
    # 670,-650
    elif -650<=y_k+10<=-350 and 660<=x_k+10<=695:
        if 660<x_k<=695: x_k+=5
        elif x_k<=660: x_k-=5

    # 670,-350
    # 470,-350
    elif -370<=y_k<=-335 and 475<=x_k<=690:
        if y_k>=-335: y_k+=5
        elif y_k<=-370: y_k-=5

    # 470,-350
    # 470,50
    elif -350<=y_k+10<=50 and 460<=x_k+10<=495:
        if 460<x_k<=495: x_k+=5
        elif x_k<=460: x_k-=5

    # 470,-150
    # 570,-150
    elif -170<=y_k<=-135 and 475<=x_k<=590:
        if y_k>=-135: y_k+=5
        elif y_k<=-170: y_k-=5

    # 570,-250
    # 770,-250
    elif -270<=y_k<=-235 and 575<=x_k<=790:
        if y_k>=-235: y_k+=5
        elif y_k<=-270: y_k-=5

    # 670,-250
    # 670,-50
    elif -250<=y_k+10<=-50 and 660<=x_k+10<=695:
        if 660<x_k<=695: x_k+=5
        elif x_k<=660: x_k-=5

    # 570,-50
    # 870,-50
    elif -70<=y_k<=-35 and 575<=x_k<=890:
        if y_k>=-35: y_k+=5
        elif y_k<=-70: y_k-=5

    # 770,-150
    # 770,-450
    elif -450<=y_k+10<=-150 and 760<=x_k+10<=795:
        if 760<x_k<=795: x_k+=5
        elif x_k<=760: x_k-=5

    # 770,-450
    # 970,-450
    elif -470<=y_k<=-435 and 775<=x_k<=990:
        if y_k>=-435: y_k+=5
        elif y_k<=-470: y_k-=5

    # 870,-350
    # 870,-150
    elif -350<=y_k+10<=-150 and 860<=x_k+10<=895:
        if 860<x_k<=895: x_k+=5
        elif x_k<=860: x_k-=5

    # 870,-350
    # 950,-350
    elif -370<=y_k<=-335 and 860<=x_k<=970:
        if y_k>=-335: y_k+=5
        elif y_k<=-370: y_k-=5

    # 570,-850
    # 70,-850
    elif -870<=y_k<=-835 and 60<=x_k<=590:
        if y_k>=-835: y_k+=5
        elif y_k<=-870: y_k-=5

    # 570,-450
    # 470,-450
    elif -470<=y_k<=-435 and 460<=x_k<=590:
        if y_k>=-435: y_k+=5
        elif y_k<=-470: y_k-=5

    # 270,-250
    # 270,-350
    elif -350<=y_k+10<=-250 and 260<=x_k+10<=295:
        if 260<x_k<=295: x_k+=5
        elif x_k<=260: x_k-=5

    #570, -450
    #570, -550
    elif -550<=y_k+10<=-450 and 560<=x_k+10<=575:
        if 560<x_k<=575: x_k+=5
        elif x_k<=560: x_k-= 5
    
        
    # print('X = ',x_k)
    # print('Y = ',y_k)
    glPopMatrix()

def spider1_3():
    global x_s, y_s, mx,my,stat,speed
    glPushMatrix()
    glTranslate(35,550,0)
    glTranslate(x_s,y_s,0)
    if stat==0:
        if y_s==0 and x_s<=0: 
            my=-speed
            stat=0
        if y_s<=-500: #kanan
            my=0
            mx=speed
            stat=0
        if x_s==625:#atas
            mx=0
            my=speed
            stat=0
        if y_s==-20 and x_s==625:
            mx=0
            my=0
            stat=1
    elif stat==1:
        if y_s==-20 and x_s==625: #Bawah
            mx=0
            my=-speed
            stat=1
        if y_s<=-500: #kekiri
            my=0
            mx=-speed
            stat=1
        if y_s==-500 and x_s==0: #keatas
            mx=0
            my=+speed
            stat=1
        if y_s==0 and x_s<=0:
            mx=0
            my=0
            stat=0

    x_s+=mx
    y_s+=my
    # print(x_s,y_s)

    glScale(6, 6, 0.0)
    laba()
    glPopMatrix()

def spider2_3(): #done
    global x_s2, y_s2,mx2,my2, stat2
    # arah = 'sumbu x'
    p=0
    glPushMatrix()
    glTranslate(250,650,0)
    glTranslate(x_s2,y_s2,0)
    if stat2==0:
        if 0<=y_s2<=0 : 
            my2=0.3
            stat2=0
        elif 99<=y_s2 :
            my2=0
            mx2=0.3
            stat2=0
        if x_s2>=100 :
            mx2=0
            my2=-0.3
            stat2=0
        if y_s2<=-199:
            mx2=0
            my2=0.3
            stat2=1
    elif stat2==1:
        if -200<=y_s2<=-199:
            mx2=0
            my2=0.3
        elif 99<=y_s2:
            my2=0
            mx2=-0.3
        if x_s2<=0 : 
            mx2=0
            my2=-0.3
        if -1<=y_s2<=1 and x_s2<=0:
            mx2=0
            my2=0.3
            stat2=0

    x_s2+=mx2
    y_s2+=my2

    glScale(5, 5, 0.0)
    laba()
    glPopMatrix()

def spider3_3():
    global x_s3, y_s3,mx3,my3, stat3, speed
    glPushMatrix()
    glTranslate(850,330,0)
    glTranslate(x_s3,y_s3,0)
    if stat3==0:
        if (0<=y_s3<=0) :#kebawah 
            my3=-speed
            stat3=0
        if (y_s3<=-180 ): #kanan
            my3=0
            mx3=speed
            stat3=0
        if (x_s3>=120):#bawah
            mx3=0
            my3=-speed
            stat3=0
        if y_s3 <=-280:#kiri
            my3=0
            mx3=-speed
            stat3=0
        if x_s3<=-100: #titik balik
            mx3=0
            my3=0
            stat3=1
    elif stat3==1:
        if x_s3<=0  :#kanan
            mx3=speed
            stat3=1
        if x_s3>=120  : #keatas 
            mx3=0
            my3=speed
            stat3=1
        if y_s3==-180 and x_s3>=120: #kiri
            my3=0
            mx3=-speed
            stat3=1
        if x_s3==0 and y_s3==-180 :
            mx3=0
            my3=speed
            stat3=0
    x_s3+=mx3
    y_s3+=my3

    glScale(6, 6, 0.0)
    laba()
    glPopMatrix()

def princes3():
    global x_p3, y_p3
    # glTranslated(960, -430, 0)
    glTranslate(x_p3, y_p3, 0)
    glScaled(0.1,0.1,0)
    glRotated(-180,0,1,0)
    princess()

def labelend3():
    glTranslatef(-130, -950, 0)
    glScaled(1.7, 1.7,0)
    gameend()

def labelvictory3():
    glTranslatef(-130, -950, 0)
    glScaled(1.7, 1.7,0)
    victory()


def gamestateover3():
    global gameover, tamat
    if gameover == True and tamat==False:
        labelend3()

def gamestatefinish3():
    global tamat, gameover
    if tamat == True:
        labelvictory3()
    else: 
        princes3()

def collision3():
    global x_s,y_s,x_k,y_k,x_s2,y_s2,tran_xs,tran_ys,tran_yk,tran_xk, gameover, tamat
    #Spider1
    if (x_s+tran_xs[0]-50<=x_k<=x_s+tran_xs[0] or x_s+tran_xs[0]-50<=x_k<=x_s+tran_xs[0]) and (y_s+tran_ys[0]-25<=y_k+tran_yk<=y_s+tran_ys[0]+20 or y_s+tran_ys[0]-25<=y_k-tran_yk<=y_s+tran_ys[0]+20):
        gameover = True

    #Spider2
    if (x_s2+tran_xs[1]-50<=x_k+10<=x_s2+tran_xs[1] or x_s2+tran_xs[1]-50<=x_k-10<=x_s2+tran_xs[1]) and (y_s2+tran_ys[1]-25<=y_k+tran_yk<=y_s2+tran_ys[1]+20 or y_s2+tran_ys[1]-25<=y_k-tran_yk<=y_s2+tran_ys[1]+20):
        gameover = True

    if (x_s3+tran_xs[2]-55<=x_k<=x_s3+tran_xs[2]+5 or x_s3+tran_xs[2]-55<=x_k<=x_s3+tran_xs[2]+5) and (y_s3+tran_ys[2]-25<=y_k+tran_yk<=y_s3+tran_ys[2]+25 or y_s3+tran_ys[2]-25<=y_k-tran_yk<=y_s3+tran_ys[2]+25):
        gameover = True

    if (x_p-30<=x_k<=x_p) and (y_p<=y_k<=y_p+55):
        tamat = True
        print("tamat")

def level3():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate1()
    bg(1000*0.7,1000*0.7)
    maze3()
    spider1_3()
    spider2_3()
    spider3_3()
    glTranslate(30,950,0)
    knight_move3()
    collision3()
    gamestateover3()
    gamestatefinish3()
    glutSwapBuffers()

def level3_main():
    glutInit()
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(canvas, canvas)
    glutInitWindowPosition(0, 0)
    wind = glutCreateWindow("The Dungeon")
    glutDisplayFunc(level3)
    glutIdleFunc(level3)
    glutSpecialFunc(input_keyboard)
    glutTimerFunc(1,update,0)
    glutMainLoop()



#Menu

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
    # print(Key)

def input_mouse(button, state, x, y):
    if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
        colliMouse(x,y)

def update(value):
    glutPostRedisplay()
    glutTimerFunc(10,update,0)

def iterate1():
    glViewport(0, 0, 700, 700)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glColor3ub(50, 50, 50)
    glOrtho(-0, 700, -0, 700, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def iterate():
    glViewport(0, 0, 700, 700)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(-700, 700, -700, 700, 0.0, 1.0)
    glMatrixMode (GL_MODELVIEW)
    glLoadIdentity()

def menu():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    blok()
    txt()
    lvl1()
    lvl2()
    lvl3()
    glutSwapBuffers()
    
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

def restart(key,x,y):
    global Key,x_s,y_s,x_s2,y_s2,x_s3,y_s3,x_k,y_k
    if key == b' ':
        Key = 0
        # x_k=0
        # y_k=0
        # x_s,y_s,x_s2,y_s2,x_s3,y_s3=0,0,0,0,0,0
        # print("TES")

def scane():
    global Key, p
    if Key==0:
        menu()
    if Key==1:
        #Menjalanakn level1
        level1()
    if Key==2:
        #RUN LEVEL2
        level2()
        # knight_move()
    if Key==3:
        level3()

def main():
    glutInit()
    glutInitDisplayMode(GLUT_RGBA)
    glutInitWindowSize(700, 700)
    glutInitWindowPosition(0, 0)
    wind = glutCreateWindow("OpenGL Coding Practice : GL_POLYGON")
    glutDisplayFunc(scane)
    glutIdleFunc(scane)
    glutSpecialFunc(input_keyboard)
    glutKeyboardFunc(restart)
    if Key==0 : glutMouseFunc(input_mouse)
    glutTimerFunc(1,update,0)
    glutMainLoop()

# main_menu()
# level1_main()
# level2_main()
# level3_main()
main()


