from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from Karakter import *
from Map.mazemap import *
from Karakter.Knight import *
from Karakter.Spider import *
from Karakter.princess import *
from label import *


# Ukuran
canvas=700
gameover = False
tamat = False

#set koordinat princess
x_p = 960
y_p = -430

# x_p = 100 #lebih dekat jaraknya
# y_p = -30

#set koordinat Knight
x_k=0
y_k=0

#set koordinat Spider (monster)
#x_s, y_s
#mx,my adalah step untuk gerakan
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

speed=0.5

def input_keyboard(key,x,y):
    global x_k,y_k,rotate
    step=5
    if key == GLUT_KEY_UP:
        rotate=1
        y_k+=step
    elif key == GLUT_KEY_DOWN:
        rotate=2
        y_k -= step
    elif key == GLUT_KEY_RIGHT:
        rotate=3
        x_k+= step
    elif key == GLUT_KEY_LEFT:
        rotate=4
        x_k -= step


def knight_move():
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

def spider1():
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

def spider2(): #done
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

def spider3():
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

    # if stat3==0:
    #     if 0<=y_s3<=0 : #bawah
    #         my3=-0.3
    #         stat3=0
    #     elif 99<=y_s3 :#kanan
    #         my2=0
    #         mx2=0.3
    #         stat2=0
    #     if x_s2>=-100 : #bawah
    #         mx2=0
    #         my2=-0.3
    #         stat2=0
    #     elif -280>=y_s3 :#kiri
    #         my2=0
    #         mx2=-0.3
    #         stat2=0
    #     if y_s3<=-189:
    #         mx2=0
    #         my2=0.3
    #         stat2=1
    # elif stat2==1:
    #     if -200<=y_s2<=-199:
    #         mx2=0
    #         my2=0.3
    #     elif -180<=y_s2:
    #         my2=0
    #         mx2=-0.3
    #     if x_s2<=0 : 
    #         mx2=0
    #         my2=-0.3
    #     if -1<=y_s2<=1 and x_s2<=0:
    #         mx2=0
    #         my2=0.3
    #         stat2=0

    x_s3+=mx3
    y_s3+=my3

    glScale(6, 6, 0.0)
    laba()
    glPopMatrix()

def princes():
    global x_p, y_p
    # glTranslated(960, -430, 0)
    glTranslate(x_p, y_p, 0)
    glScaled(0.1,0.1,0)
    glRotated(-180,0,1,0)
    princess()

def labelend():
    glTranslatef(-130, -950, 0)
    glScaled(1.7, 1.7,0)
    gameend()

def labelvictory():
    glTranslatef(-130, -950, 0)
    glScaled(1.7, 1.7,0)
    victory()

def collision():
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

def gamestateover():
    global gameover
    if gameover == True:
        labelend()
    else:
        princes()

def gamestatefinish():
    global tamat
    if tamat == True:
        labelvictory()
    else:
        princes()


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

def level3():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    bg(1000*0.7,1000*0.7)
    maze3()
    spider1()
    spider2()
    spider3()
    glTranslate(30,950,0)
    knight_move()
    collision()
    gamestateover()
    gamestatefinish()
    print(x_p, y_p)
    print(x_k, y_k)
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

level3_main()