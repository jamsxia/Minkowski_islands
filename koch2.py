import turtle
def koch2(t,n):
    if n<10:
        t.fd(n)
        return
    m=n/4
    koch2(t,m)
    t.lt(90)
    koch2(t,m)
    t.rt(90)
    koch2(t,m)
    t.rt(90)
    koch2(t,m)
    koch2(t,m)
    t.lt(90)
    koch2(t,m)
    t.lt(90)
    koch2(t,m)
    t.rt(90)
    koch2(t,m)
        
def island(t,n, generator):
    for i in range(4):
        generator(t,n)
        t.rt(90)

    
        
bob=turtle.Turtle()
bob.speed(0)
island(bob,200,koch2)
