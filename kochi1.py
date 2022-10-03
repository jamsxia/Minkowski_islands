import turtle
def koch1(t,n):
    if n<10:
        t.fd(n)
        return
    m=n/3
    koch1(t,m)
    t.lt(90)
    koch1(t,m)
    t.rt(90)
    koch1(t,m)
    t.rt(90)
    koch1(t,m)
    t.lt(90)
    koch1(t,m)
        
def island(t,n, generator):
    for i in range(4):
        generator(t,n)
        t.rt(90)

    
        
bob=turtle.Turtle()
bob.speed(0)
island(bob,200,koch1)
