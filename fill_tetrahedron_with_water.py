import math

def fill_tetrahedron(num):
    if type(num)==int or num%1==0:
        V=(num**3)/(6*(math.sqrt(2)))
        L=V/1000
        print (" %.2f" % L)
        return
    else: print("Ne e cqlo chislo")

fill_tetrahedron(100)
