from math import sqrt

 

def quad(a,b,c):

    x1 = (-b + sqrt(b**2 -4*a*c))/(2*a)

    x2 = (-b - sqrt(b**2 -4*a*c))/(2*a)

    return x1, x2

 

def myEquation(a,b,c,d):

    '''solve equations of the form

        ax + b = cx + d '''

    return (d-b)/(a-c)


def g(x):
    return 6*x**3 + 31*x**2 + 3*x - 10

def plug():
    x = -100
    while x < 100:
        if g(x) == 0:
            print("x = " , x)
        x += 1
    print("dond")        

x = myEquation(2,5,0,13)

print("answer is ", x)

   

x = myEquation(12,18,-34,67)

print("answer is ", x)

   

x = quad(2,7,-15)

print ("quad answer is ", x[0], ", ", x[1])

plug();
