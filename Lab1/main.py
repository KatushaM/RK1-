import sys
import math
import random
def Discriminate(a:int, b:int, c:int)->float:
    return b**2 - 4*a*c

def Calc_solutions(discr:float,a:int,b:int) -> tuple:
    roots=[]
    if discr==0.0:
        roots.append(-b/(2.0*a))
    if discr>0.0:
        roots.append((-b+(discr)**(0.5))/(2*a))
        roots.append((-b-(discr)**(0.5))/(2*a))
    else:
        roots=[]
    return roots
'''
def Calc_solutions_be(solut:tuple)->tuple:
    return (solut[0]**(0.5), -(solut[0]**(0.5)), solut[1]**(0.5), -(solut[1]**(0.5)))
'''
print("Do you want to set the coefficients yourself?")
print("1-yes, 2-no")
koef=int(input())
if koef==1:
    print("Input coef")
    print("A: ")
    a = float(input())
    while a==0:
        print("A is incorrect, it should be >0, pleas enter a new one")
        print("A: ")
        a=float(input())
    print("B: ")
    b = float(input())
    print("C: ")
    c = float(input())

if koef==2:
    a=a.randint(1,100)
    a=float(a)
    b=b.randint(1,100)
    b=float(b)
    c=c.randint(1,100)
    c=float(c)

if len(Calc_solutions(Discriminate(a,b,c),a,b))==0:
    print("No roots. Discriminate < 0")
elif len(Calc_solutions(Discriminate(a,b,c),a,b))==1:
    print("1 Solutions:")
    print(Calc_solutions(Discriminate(a, b, c), a, b))
else:
    print("2 Solutions:")
    print(Calc_solutions(Discriminate(a, b, c), a, b))
'''
print("Solutions:")
print(Calc_solutions(Discriminate(a,b,c),a,b))
print("Solutions_be")
print(Calc_solutions_be(Calc_solutions(Discriminate(a,b,c),a,b)))
'''




