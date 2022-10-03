def two(f):
    f()
    f()
def four(f):
    two(f)
    two(f)
    
def plus():
    print('+',end=' ')

def dash():
    print('-',end=' ')

def bar():
    print('/',end=' ') # this is easier to change to |

def space():
    print(' ',end=' ')

def half_beam():
    plus()
    four(dash)

def beam():
    four(half_beam)#changed
    plus()
    print()

def half_strut():
    bar()
    four(space)

def strut():
    four(half_strut)
    bar()
    print()

def half_box():
    beam()
    four(strut)

def box():
    four(half_box)#changed
    beam()

box()
