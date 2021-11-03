#!/usr/bin/python3



def good(l):
    for i in range(len(l)):
        for j in range(i):
            if l[i]==l[j]: return False
            if l[i]+i == l[j]+j: return False
            if l[i]-i == l[j]-j: return False
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


print(solve([]))


