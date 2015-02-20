import math

def fill_tetrahedron(num):
    if type(num)==int or num%1==0:
        Volume_cm=(num**3)/(6*(math.sqrt(2)))
        Volume_L=Volume_cm/1000
        print (" %.2f" % Volume_L)
        return
    else: print("Ne e cqlo chislo")

fill_tetrahedron(100)
