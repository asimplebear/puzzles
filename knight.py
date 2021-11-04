#!/usr/bin/python3


#upshot of this iblock is to get "legals" dictionary
# { .. (x,y) : [ (a,b) ]..}  keys are coordinates
#of square and values are list of squares a
#knight's move away
sqrs = [(i,j) for i in range(8) for j in range(8)]
legals = {}
ot = [-1,1,-2,2]
d = [(x,y) for x in ot for y in ot if (x+y)%2]
for i in range(8):
    for j in range(8):
        h = []
        for x,y in d:
            if 0<=i+x<8 and 0<=j+y<8:
                h.append((i+x,j+y))
        legals[(i,j)] = h


def solve(x,y,path=[]):

    new_path = path+[(x,y)]

    if len(new_path) == 64:
        return new_path

    legal = [_ for _ in legals[(x,y)] if not _ in path]

    legal.sort(key = lambda _: len(legals[_]))

    for i,j in legal:
        if (i,j) in path:
            continue
        s = solve(i,j,new_path)
        if s:
            return s


def display(brd):

    print(' '+'-'*30)
    for i in range(8):
        l = ['{:2}'.format(brd[(i,j)]) for j in range(8)]
        x = ' |'.join(l)
        x = '|' + x + '|'
        print(x)
        print('-'*31)


if __name__ == '__main__':

    import sys
    #optional coordinates of square to start on
    x, y = 0, 0
    if len(sys.argv) == 3:
        [x, y] = sys.argv[1:]

    s = solve(int(x), int(y), [])
    soln = {sqr: ind for ind, sqr in enumerate(s)}
    display(soln)
