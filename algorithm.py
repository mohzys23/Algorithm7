import math
def sum_off(x, y):
    if x == y:
        return 0
    if x < y:
        return -1
    elif x > y:
        return 1

#incremental development
def length(a, b):
    da = a**2
    print(da)
    db = b**2
    print(db)
    print(da + db)
    hypotenuse =math.sqrt(da+db)
    return hypotenuse


def almightFml(a,b,c):
     bsquare = b**2
     print('b square =', bsquare)
     subAC = 4*a*c
     print('4 multiply by a and c =', subAC)
     divA = 2*a
     print('2 multiply by a =', divA)
     subtract=bsquare - subAC
     print('bsquare minus subAC =', subtract)
     subDiv = subtract/divA
     print('ddivA divided by subtract =', subDiv)
     solution = math.sqrt(subDiv)
     return solution
     
     










