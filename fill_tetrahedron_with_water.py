import math

def fill_tetrahedron(num):
    if type(num)==int or num%1==0:
        Volume=(num**3)/(6*(math.sqrt(2)))
        liters=Volume/1000
        print (" %.2f" % liters)
        return liters
    else:
        raise ValueError('%s is not integer number' %str(num))

fill_tetrahedron(100)
