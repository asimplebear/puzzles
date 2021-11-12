#!/usr/bin/python3

'''
rows is list of ints.  each int is the column that
the queen on that row is on
'''

def good(l):
    '''
    at least as long as l is there's no attacks
    '''
    for i in range(len(l)):
        for j in range(i):
              #two in same column or
              #two on same upright-downleft diagonal or
              #two on same downright-upleft diagonal
              if l[i]==l[j] or\
                 l[i]+i == l[j]+j or\
                 l[i]-i == l[j]-j:
                   return False
    return True


def solve_all(rows, solns = []):
    '''
    get all solutions
    '''
    if len(rows) == 8 and good(rows):
        #append this soln and tell the loop
        #there are no more ways to go
        solns.append(rows)
        return None, solns
    for i in range(8):
        #try to extend this partial soln
        inc_rows = rows + [i]
        #nope
        if not good(inc_rows):
            continue
        #append all the solns that extend by 'i'
        soln, solns = solve_all(inc_rows, solns)
        if soln and soln[0]:
            solns.append(soln)
            #send back to get extended again
            return inc_rows, solns
    #no more solutions extending this partial soln
    return None, solns


def display(rows):

    print('   '+'-'*31)
    for row in rows:
        x='  | '*row+'  | Q'+' |  '*(8-row)
        print(x)
        print('   '+'-'*31)


def symmetries(rows):
    '''
    dihedral group on chess board
    to eliminate symmetric solutions
    '''
    def rot(rows):
        ret = ['@']*8
        for i in range(8):
            ret[rows[i]]=7-i
        return ret


    def flip(rows):
        ret=['@']*8
        for i in range(8):
            ret[rows[i]]=i
        return ret

    y = [_ for _ in rows]
    for n in range(1,4):
        y = rot(y)
        yield y
    y = [_ for _ in rows]
    y = flip(y)
    yield y
    for n in range(1,4):
        y = rot(y)
        yield(y)




if __name__ == '__main__':

    _, solns = solve_all([])

    uniques = []
    for soln in solns:
        there = False
        for sol in symmetries(soln):
            if sol in uniques:
                there = True
        if not there:
            uniques.append(soln)

    print(len(uniques), 'solutions')
    for soln in uniques:
        display(soln)
        if input('..') != '': break


def solve(rows):
    '''
    just get SOME solution
    included for clarity
    '''
    if len(rows) == 8 and good(rows):
        return rows
    for i in range(8):
        inc_rows = rows + [i]
        if not good(inc_rows):
            continue
        soln = solve(inc_rows)
        if soln:
            return soln


