#!/usr/bin/python3

sqrs = [(i,j) for i in range(8) for j in range(8)]

brd = {s: str(s[0]*8 + s[1]) for s in sqrs}
brd = {s: '' for s in sqrs}

legals = {}
ot = [-1,1,-2,2]
d = [(x,y) for x in ot for y in ot if (x+y)%2]

for i in range(8):
    for j in range(8):
        h = []
        for x,y in d:
            if 0<=i+x<8 and 0<=j+y<8:
                h.append((i+x,j+y))
        h.sort(key = lambda _: len(_))#####
        legals[(i,j)] = h


def solve(x,y,path=[]):
    if len(path) > 62:
        return path
    #assert not (x,y) in path###########
    new_path = path+[(x,y)]
    legal = [_ for _ in legals[(x,y)]]# if not _ in path]
    #legal = list(set(legal))
    legal.sort(key = lambda _: len(legals[_]))
    #input(legal)
    for i,j in legal:
        #print(legal, i, j)##################
        if (i,j) in path:
            continue
        print(legal,i,j)
        s = solve(i,j,new_path)
        
        if s: 
            print(len(s))
            return s

s = solve(4,5,[])
#print(s, len(s))
dd = {_: '0' for _ in sqrs}
for i,sq in enumerate(s):
    dd[sq] = i
    
def display(brd):
    print(' '+'-'*30)
    for i in range(8):
        l = ['{:2}'.format(brd[(i,j)]) for j in range(8)]
        x = ' |'.join(l)
        x = '|' + x + '|'
        print(x)
        print('-'*31)


display(dd)
