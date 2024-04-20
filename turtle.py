from turtle import *

def trojkat(bok, x):
    if x == 0:
        for i in range(3):
            fd(bok)
            left(120)
    else:
        trojkat(bok/2, x-1)
        fd(bok/2)
        trojkat(bok/2, x-1)
        bk(bok/2)
        left(60)
        fd(bok/2)
        right(60)
        trojkat(bok/2, x-1)
        left(60)
        bk(bok/2)
        right(60)
        
pu(); bk(400); left(90); bk(300); right(90); pd(); speed(0)

trojkat(700,5)
done()
