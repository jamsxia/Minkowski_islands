


def two(f):
    f()
    f()
def four(f):
    two(f)
    two(f)
    
def beam():
    print('+ - - - - + - - - - + - - - - + - - - - +')#changed

def strut():
    print('/         /         /         /         /')#changed

def half_box():
    beam()
    four(strut)

def box():
    four(half_box)#changed
    beam()

box()
