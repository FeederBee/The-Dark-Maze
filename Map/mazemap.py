from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

# state = int(input())
state=3
def bg(x,y):
    glBegin(GL_POLYGON)
    glVertex(0, 0)
    glVertex(0, y)

    glVertex(0, y)
    glVertex(x, y)

    glVertex(x, y)
    glVertex(x, 0)

    glVertex(x, 0)
    glVertex(0, 0)

    glEnd()

#Level1, Ukuran asli : 500*500
def maze1():
    glColor3f(0.0, 0.0, 0.0)
    glLineWidth(3)
    glScaled(0.7,0.7,0.0)
    glBegin(GL_LINES)
    glVertex(0, 100)
    glVertex(0, 500)

    glVertex(0, 500)
    glVertex(500, 500)

    glVertex(500, 500)
    glVertex(500, 300)

    glVertex(500, 200)
    glVertex(500, 0)
    
    glVertex(500, 0)
    glVertex(0, 0)

    # Krus
    #1
    glVertex(0, 100)
    glVertex(300, 100)
    #2
    glVertex(400, 0)
    glVertex(400, 100)
    #3
    glVertex(100, 200)
    glVertex(100, 400)
    #4
    glVertex(100, 400)
    glVertex(200, 400)
    #5
    glVertex(200, 400)
    glVertex(200, 200)
    #6
    glVertex(200, 200)
    glVertex(500, 200)
    #7
    glVertex(400, 500)
    glVertex(400, 400)
    #8
    glVertex(300, 400)
    glVertex(300, 300)
    #9
    glVertex(300, 300)
    glVertex(500, 300)

    glEnd()

#Level2, Ukuran asli : 800*800
def maze2():
    glColor3ub(0, 0, 0)
    glLineWidth(3)
    glScaled(1.0,0.7,0.0)
    glBegin(GL_LINES)
    glVertex(0, 0)
    glVertex(0, 300)

    glVertex(0, 400)
    glVertex(0, 800)

    glVertex(0, 800)
    glVertex(800, 800)

    glVertex(800, 700)
    glVertex(800, 0)
    
    glVertex(800, 0)
    glVertex(0, 0)

    #krus
    #1
    glVertex(0, 300)
    glVertex(100, 300)
    # 2
    glVertex(100, 300)
    glVertex(100, 200)
# 3
    glVertex(100, 100)
    glVertex(100, 200)
# 4
    glVertex(200, 0)
    glVertex(200, 300)
# 5    
    glVertex(200, 200)
    glVertex(300, 200)
# 6
    glVertex(300, 100)
    glVertex(700, 100)
# 7
    glVertex(400, 100)
    glVertex(400, 400)
# 8
    glVertex(300, 300)
    glVertex(600, 300)
# 9
    glVertex(500, 300)
    glVertex(500, 200)
# 10
    glVertex(500, 200)
    glVertex(700, 200)
# 11
    glVertex(700, 200)
    glVertex(700, 300)
# 12
    glVertex(400, 400)
    glVertex(700, 400)
# 13    
    glVertex(700, 400)
    glVertex(700, 700)
# 14
    glVertex(100, 500)
    glVertex(100, 700)
# 15
    glVertex(100, 700)
    glVertex(400, 700)
# 16
    glVertex(400, 700)
    glVertex(400, 600)
# 17    
    glVertex(300, 400)
    glVertex(300, 600)
# 18
    glVertex(300, 500)
    glVertex(500, 500)
# 19
    glVertex(300, 600)
    glVertex(600, 600)
# 20
    glVertex(600, 500)
    glVertex(600, 700)
# 21
    glVertex(600, 700)
    glVertex(800, 700)
# 22
    glVertex(0, 400)
    glVertex(200, 400)
# 23
    glVertex(200, 400)
    glVertex(200, 600)
# 24
    glVertex(500, 800)
    glVertex(500, 700)

    glEnd()

#Level 3, Ukuran asli: 1000*1000
def maze3():
    glColor3ub(0, 0, 0)
    glScaled(0.7, 0.7, 0)
    glLineWidth(3)
    glBegin(GL_LINES)
    glVertex(0, 0)
    glVertex(0, 900)

    glVertex(0, 1000)
    glVertex(1000, 1000)

    glVertex(1000, 1000)
    glVertex(1000, 600)

    glVertex(1000, 500)
    glVertex(1000, 0)

    glVertex(1000, 0)
    glVertex(0, 0)

    glVertex(0, 900)
    glVertex(300 , 900)

    glVertex(0, 600)
    glVertex(100, 600)

    glVertex(100, 600)
    glVertex(100, 700)

    glVertex(400, 1000)
    glVertex(400, 700)

    glVertex(400, 800)
    glVertex(100, 800)
    
    glVertex(200, 800)
    glVertex(200, 400)

    glVertex(200, 600)
    glVertex(300, 600)
    
    glVertex(300, 600)
    glVertex(300, 700)

    glVertex(200, 500)
    glVertex(100, 500)

    glVertex(100, 500)
    glVertex(100, 300)

    glVertex(100, 300)
    glVertex(400, 300)

    glVertex(200, 300)
    glVertex(200, 200)

    glVertex(300, 300)
    glVertex(300, 200)
    
    glVertex(300, 200)
    glVertex(500, 200)

    glVertex(100, 200)
    glVertex(100, 100)

    glVertex(100, 100)
    glVertex(600, 100)
    
    glVertex(600, 100)
    glVertex(600, 400)

    glVertex(300, 500)
    glVertex(300, 400)
    
    glVertex(300, 400)
    glVertex(500, 400)

    glVertex(400, 400)
    glVertex(400, 600)

    glVertex(500, 300)
    glVertex(500, 500)
    
    glVertex(500, 500)
    glVertex(600, 500)

    glVertex(700, 0)
    glVertex(700, 200)

    glVertex(700, 100)
    glVertex(900, 100)

    glVertex(800, 100)
    glVertex(800, 300)

    glVertex(900, 200)
    glVertex(900, 300)
    
    glVertex(900, 300)
    glVertex(1000, 300)

    glVertex(500, 1000)
    glVertex(500, 600)

    glVertex(500, 800)
    glVertex(600, 800)

    glVertex(500, 600)
    glVertex(700, 600)

    glVertex(700, 600)
    glVertex(700, 300)
    
    glVertex(700, 400)
    glVertex(900, 400)

    glVertex(1000, 500)
    glVertex(800, 500)

    glVertex(800, 500)
    glVertex(800, 800)

    glVertex(800, 700)
    glVertex(600, 700)

    glVertex(700, 700)
    glVertex(700, 900)

    glVertex(600, 900)
    glVertex(900, 900)

    glVertex(900, 800)
    glVertex(900, 600)

    glVertex(900, 600)
    glVertex(1000, 600)

    glVertex(600, 400)
    glVertex(600, 500)    

    glEnd()


# def iterate():
#     glViewport(0, 0, 700, 700)
#     glMatrixMode(GL_PROJECTION)
#     glLoadIdentity()
#     glColor3ub(50, 50, 50)
#     glOrtho(-0, 700, -0, 700, 0.0, 1.0)
#     glMatrixMode (GL_MODELVIEW)
#     glLoadIdentity()

# def showScreen():
#     glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
#     glLoadIdentity()
#     iterate()
#     if state==1:
#         x = 500*0.7
#         y =500*0.7
#         bg(x,y)
#         maze1()
#     elif state==2:
#         x = 800*0.7
#         y = 800*0.7
#         bg(x,y)
#         maze2()
#     elif state==3:
#         x = 1000*0.7
#         y = 1000*0.7
#         bg(x,y)
#         maze3()
#     glutSwapBuffers()

# glutInit()
# glutInitDisplayMode(GLUT_RGBA)
# glutInitWindowSize(700, 700)
# glutInitWindowPosition(0, 0)
# wind = glutCreateWindow("The Dungeon")
# glutDisplayFunc(showScreen)
# glutIdleFunc(showScreen)
# glutMainLoop()