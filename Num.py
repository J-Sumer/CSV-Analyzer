import math
import cfunctions

class Num:
    def __init__(self, c=0, s=""):
        self.n = 0
        self.at = c
        self.name = s
        self._has = {}
        self.lo = math.huge
        self.hi = -math.huge
        self.isSorted = True
        self.w = (s.find("-$") and -1 or 1)


    def nums(self):
        if not self.isSorted:
            table.sort(self._has)
            self.isSorted = True
        return self._has

    def add(self, v, pos):
        if v != "?":
            self.n += 1
            self.lo = math.min(v, self.lo)
            self.hi = math.max(v, self.hi)
            if self._has < the.nums:
                pos = 1 + (#self._has) 
            elif math.random() < the.nums/self.n:
                pos=math.random(#self._has)
            if pos:
                self.isSorted = false
                self._has[pos] = tonumber(v)

    def div(self, a):
        a = self:nums(); 
        return per(a,.9)-per(a,.1))/2.58 


    def mid(self):
        return per((self))

