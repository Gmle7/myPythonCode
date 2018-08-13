from functools import reduce

def f(x,y):
    return x*y
list(map(f,[2,4,6,8,10],[1,3,5,7,9]))
list(map(str,[2,4,6,8,10]))

reduce(f,[1,2,3,4,5])

def str2int(s):
    def fn(x,y):
        return x*10+y
    def char2num(s):
        digits={'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9}
        return digits[s]
    return reduce(fn,map(char2num,s))
str2int('54')

def normalize(name):
    return name[0].upper()+name[1:].lower()
list(map(normalize,['adam', 'LISA', 'barT']))

def prod(L):
    def f(x,y):
        return x*y
    return reduce(f,L)
prod([8,5,7])

def str2float(s):
    indexDot = s.index(".")
    l = list(s)
    l.remove(".")
    return reduce(lambda x,y:x*10+y,list(map(int,l)))/10**(len(l)-indexDot)

str2float('123.789')