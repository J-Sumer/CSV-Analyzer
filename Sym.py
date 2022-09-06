import math

class Sym:
    def __init__(self, c=0, s=""):
        self.n = 0
        self.at = c
        self.name = s
        self._has = {}


    def add(self, v):
        if v != '?':
            self.n += 1
            self_has[v] = 1 + (self._has[v] or 0)

    def mid(self, col, most, mode):
        most = -1
        for k,v in enumerate(self._has):
            if v > most:
                most = k, v
        return most

    def fun(self, p):
        return p*math.log(p,2)

    def div(self, e, fun):
        e = 0
        for _,n in enumerate(self._has):
            if n>0:
                e = e - seelf.fun(n/self.n)
        return e


