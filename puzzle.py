#!/usr/bin/python3



def good(l):
    for i in range(len(l)):
        for j in range(i):
            if l[i]==l[j] or\
               l[i]+i == l[j]+j or\
               l[i]-i == l[j]-j:
                   return False
    return True


def solve(rows):

    if len(rows) == 8 and good(rows):
        return rows
    for i in range(8):
        inc_rows = rows + [i]
        if not good(inc_rows):
            continue
        soln = solve(inc_rows)
        if soln:
            return soln

def solve_all(rows, solns = []):

    if len(rows) == 8 and good(rows):
        #return rows
        solns.append(rows)
        return None, solns
    for i in range(8):
        inc_rows = rows + [i]
        if not good(inc_rows):
            continue
        soln, solns = solve_all(inc_rows, solns)
        if soln and soln[0]:
            solns.append(soln)
            return inc_rows, solns
    return None, solns


def display(rows):
    st = ' '
    print('   '+'-'*31)
    for row in rows:
        x='  | '*row+'  | Q'+' |  '*(8-row)
        print(x)
        print('   '+'-'*31)


#s = solve([])
#print(s)
#display(s)

_, solns = solve_all([])
print(len(solns))
for soln in solns:
    display(soln)
    input('..')




