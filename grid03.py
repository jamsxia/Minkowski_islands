
def two(f):
    f()
    f()
def four(f):
    two(f)
    two(f)
    
def makeline(a,b):
    print(2*((((a + b*4) * 2) ) )+a) # uses a powerful feature of python  changed
    
def beam():
    makeline('+ ','- ')
    
def strut():
    makeline('/ ','  ')

def half_box():
    beam()
    four(strut)

def box():
    four(half_box)#changed
    beam()

box()
