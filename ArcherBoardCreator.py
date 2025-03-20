#archer map buildtester
import random
import turtle
import math

'''
spawn = 1 (4 total)
good: * 18 (6 each)
 - treasure = 2.1
 - heal = 2.2
 - reload = 2.3
bad = 3 (8 total)
chance = 4 (6 total)
tunnels (4 total) 2 each
 - tunnel 1 = 5.1
 - tunnel 2 = 5.2
random = 6 (6 total)
shop = 7 (4 total)
empty = 8 (10 total)
wall = 0 (21 total)
'''
def getMax(l):
    m = -1
    for i in l:
        if i > m:
            m = i
    return m
def findSpawns(l):
    if len(l) == 9:
        s1,s2,s3,s4=[0,0],[0,0],[0,0],[0,0]
        half = math.ceil((len(l)-1)/2)
        s1[0] = random.randint(0,half)
        s2[0] = random.randint(0,half)
        s3[0] = random.randint(half,len(l)-1)
        s4[0] = random.randint(half,len(l)-1)
        s = [s1,s2,s3,s4]
        for i in range(4):
            if i%2==0:
                s[i][1] = random.randint(0,math.floor(l[s[i][0]]/2))
            else:
                s[i][1] = random.randint(math.ceil(l[s[i][0]]/2),l[s[i][0]]-1)

    return s1,s2,s3,s4
def grayBoard(l3,l4):
    s = turtle.Screen()
    t = turtle.Turtle()
    t.penup()
    t.speed(0)
    a = -300
    b = -100
    t.goto(a,b)
    count = 0
    up = False
    #print(spawns)
    counts=0
    for k in range(len(l3)):
        for j0 in range(len(l3[k])):
            #print(k, j0)
            j = l3[k][j0]
            t.pendown()
            '''
            if j == 1:
                t.fillcolor("cyan")
            if j == 2.1:
                t.fillcolor("gold")
            if j == 2.2:
                t.fillcolor("sienna")
            if j == 2.3:
                t.fillcolor("lime")
            if j == 3:
                t.fillcolor("red")
            if j == 4:
                t.fillcolor("purple")
            if j == 5.1:
                t.fillcolor("maroon")
            if j == 5.2:
                t.fillcolor("dark red")
            if j == 5.3:
                t.fillcolor("peru")
            if j == 5.4:
                t.fillcolor("firebrick")
            if j == 6:
                t.fillcolor("orange")
            if j == 7:
                t.fillcolor("yellow")
            if j == 8:
                t.fillcolor("gray")
            #'''
            if j == 0:
                t.fillcolor("white")
            else:
                t.fillcolor('gray')
            t.begin_fill()
            for l in range(6):
                t.forward(25)
                t.right(60)
            t.end_fill()
            if j != 0:
                t.right(75)
                t.up()
                t.forward(30)
                t.write(counts,font=("Verdana",15, "normal"))
                t.backward(30)
                t.left(75)
                counts+=1
                t.down()
            '''
            if [k,j0] in spawns:
                t.right(150)
                t.color("cyan")
                t.width(10)
                t.circle(25)
                t.left(150)
                t.color("black")
                t.width(1)
            #'''
            t.penup()
            t.left(90)
            t.forward(40)
            t.right(90)
            count+=1
            if l4[k] == getMax(l4):
                up = True
            if count == l4[k]:
                count = 0
                if up:
                    b+= 20
                else:
                    b-= 20
                a+=40
                t.goto(a,b)
def masterBoard(l3,l4):
    s = turtle.Screen()
    t = turtle.Turtle()
    t.penup()
    t.speed(0)
    a = 100
    b = -100
    t.goto(a,b)
    count = 0
    up = False
    #print(spawns)
    counts=0
    for k in range(len(l3)):
        for j0 in range(len(l3[k])):
            #print(k, j0)
            j = l3[k][j0]
            t.pendown()
            if j == 1:
                t.fillcolor("cyan")
            if j == 2.1:
                t.fillcolor("gold")
            if j == 2.2:
                t.fillcolor("sienna")
            if j == 2.3:
                t.fillcolor("lime")
            if j == 3:
                t.fillcolor("red")
            if j == 4:
                t.fillcolor("purple")
            if j == 5.1:
                t.fillcolor("maroon")
            if j == 5.2:
                t.fillcolor("dark red")
            if j == 5.3:
                t.fillcolor("peru")
            if j == 5.4:
                t.fillcolor("firebrick")
            if j == 6:
                t.fillcolor("orange")
            if j == 7:
                t.fillcolor("yellow")
            if j == 8:
                t.fillcolor("gray")
            if j == 0:
                t.fillcolor("white")
            t.begin_fill()
            for l in range(6):
                t.forward(25)
                t.right(60)
            t.end_fill()
            if j != 0:
                t.right(75)
                t.up()
                t.forward(30)
                t.write(counts,font=("Verdana",15, "normal"))
                t.backward(30)
                t.left(75)
                counts+=1
                t.down()
            if [k,j0] in spawns:
                t.right(150)
                t.color("cyan")
                t.width(10)
                t.circle(25)
                t.left(150)
                t.color("black")
                t.width(1)
            t.penup()
            t.left(90)
            t.forward(40)
            t.right(90)
            count+=1
            if l4[k] == getMax(l4):
                up = True
            if count == l4[k]:
                count = 0
                if up:
                    b+= 20
                else:
                    b-= 20
                a+=40
                t.goto(a,b)
#l0 = [16,4,8,8,8,6,6,2,2,2,2,8,12,15]
l0=[12,0,4,4,4,3,3,2,2,8,9,10]
#l01 = [0,1,2.1,2.2,2.3,3,4,5.1,5.2,5.3,5.4,6,7,8]
l01 = [0,1,2.1,2.2,2.3,3,4,5.1,5.2,6,7,8]
l = []
for h in range(len(l0)):
    for h1 in range(l0[h]):
        l.append(l01[h])
#print(l)
#'''
#print(len(l))
l21 = [l.count(0),l.count(1),l.count(2.1),l.count(2.2),l.count(2.3),l.count(3),
      l.count(4),l.count(5.1),l.count(5.2),l.count(6),l.count(7),l.count(8)]
#print(l21)
for i0 in range(len(l)):
    y0 = random.randint(0,len(l)-1)
    temp = l[i0]
    l[i0] = l[y0]
    l[y0] = temp
for i in range(1000):
    x = random.randint(0,len(l)-1)
    y = random.randint (0,len(l)-1)
    temp = l[x]
    l[x] = l[y]
    l[y] = temp
#print(len(l))
#print(l)
l22 = [l.count(0),l.count(1),l.count(2.1),l.count(2.2),l.count(2.3),l.count(3),
      l.count(4),l.count(5.1),l.count(5.2),l.count(6),l.count(7),l.count(8)]
#print(l22)
l3 = []
l4 = [5,6,7,8,9,8,7,6,5]
#l4=[6,7,8,9,10,11,10,9,8,7,6]
spawns=findSpawns(l4)
counter=0
for z in l4:
    x = []
    for y in range(z):
        x.append(l[counter])
        counter+=1
    l3.append(x)
#print(l3)
#print(len(l))
#print(l2)
d = {}
d[0] = 0
d[1] = 0
d[2.1] = 0
d[2.2] = 0
d[2.3] = 0
d[3] = 0
d[4] = 0
d[5.1] = 0
d[5.2] = 0
d[5.3] = 0
d[5.4] = 0
d[6] = 0
d[7] = 0
d[8] = 0
for w in range(len(l3)):
    d[0] += l3[w].count(0)
    d[1] += l3[w].count(1)
    d[2.1] += l3[w].count(2.1)
    d[2.2] += l3[w].count(2.2)
    d[2.3] += l3[w].count(2.3)
    d[3] += l3[w].count(3)
    d[4] += l3[w].count(4)
    d[5.1] += l3[w].count(5.1)
    d[5.2] += l3[w].count(5.2)
    d[6] += l3[w].count(6)
    d[7] += l3[w].count(7)
    d[8] += l3[w].count(8)
grayBoard(l3,l4)
masterBoard(l3,l4)
#'''

