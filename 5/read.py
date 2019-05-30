def read ():
    f = open ("plecak.txt","r")
    if f.mode == "r":
        tmp= f.read().split()
        C = int(tmp[0])
        n = int(tmp[1])
        for i in range(2,len(tmp)):
            tmp[i] = eval(tmp[i])
        f.close()
        return tmp[2:]
    return False