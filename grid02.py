def two(f,x):
    f(x)
    f(x)
def four(f,x):
    two(f,x)
    two(f,x)
    
def put(x):
    print(x,end=' ')
    
def putln(x):     # this can be abstracted
    print(x)

def half_beam(x):
    put('+')
    four(put,'-')

def beam(x):
    four(half_beam,x)#changed
    putln('+')

def half_strut(x):
    put('/')
    four(put,' ')

def strut(x):
    four(half_strut,x)#changed
    putln('/')

def half_box(x):
    beam(x)
    four(strut,x)

def box(x):
    four(half_box,x)#changed
    beam(x)
    
box('dummy')
