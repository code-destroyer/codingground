import math

def fill_tetrahedron(num):
    if type(num)==int or num%1==0:
        volume=((num)**3)/(6*(math.sqrt(2)))
        liters=volume/1000
        return liters
    else: 
        raise ValueError('%s is not integer number' %str(num)) 
    
def tetrahedron_filled(tetrahedrons, water):
    counter = 0
    tetrahedrons.sort()
    for tetrahedron in tetrahedrons:
        liters = fill_tetrahedron(tetrahedron)
        if liters<water:
            counter = counter+1
            water = water - liters
        else:
            break

    return counter

print (tetrahedron_filled([100, 20, 30], 10))
