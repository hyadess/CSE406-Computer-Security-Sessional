import hashlib
import math
from random import randint
from sympy import prevprime


inf = (None, None)



def pointAddition(p1,p2,a,p):
    if p1==inf:
        return p2
    if p2==inf:
        return p1

    x1,y1=p1
    x2,y2=p2

    if p1!=p2:
        s=((y2-y1)*pow(x2-x1,-1,p))%p
    else:
        s=((3*x1**2+a)*pow(2*y1,-1,p))%p

    x3=(s**2-x1-x2)%p
    y3=(s*(x1-x3)-y1)%p

    return (x3,y3)


def pointDoubling(p1,a,p):
    if p1==inf:
        return inf

    x, y = p1
    #print(x,y)
    s=((3*x**2+a)*pow(2*y,-1,p))%p
    x3=(s**2-2*x)%p
    y3=(s*(x-x3)-y)%p

    return (x3,y3)


def scalarMultiplication(kk, point,a,p):
    result = point
    k=kk
    while k > 0:
        if k % 2 == 1:
            result = pointAddition(result, point,a,p)
        result = pointDoubling(result,a,p)
        k //= 2
    return result

def calculateE(p):
    offset=randint(1,2**20)
    E=prevprime(p + 1 - int(math.sqrt(p))-offset)
    return E


def generatePublicPrivatePair(gx,gy,a,p):
    private_key = randint(1, calculateE(p) - 1)
    #print(gx,gy,a,p)
    public_key = scalarMultiplication(private_key, (gx, gy),a,p)
    return private_key, public_key


def generateSharedKey(privateKey, peerKey,a,p):
    keyPoint = scalarMultiplication(privateKey, peerKey,a,p)
    sharedKey = keyPoint[0]
    return sharedKey


