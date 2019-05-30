from random import randint

def create (C,n,pmax,wmax):
    f = open("plecak.txt", "w+")
    f.write("{}\n".format(C))
    f.write("{}\n".format(n))
    for i in range(n):
       f.write( "({},{})\n".format(randint(1,pmax),randint(1,wmax)) )
    f.close()