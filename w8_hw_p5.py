## Written by Imran Qureshi for Math23b - Homework 8

import itertools 
import math
from prettytable import PrettyTable
import numpy as np
from pandas import *

def get_permutation_cycles(a,b):
    n = a+b
    s = list(range(1,n+1))
    result = list(itertools.combinations(s, a))
    for x in range(0, len(result)):
        ts = []
        for y in s:
            if y not in result[x]:
                ts.append(y)
        result[x] += tuple(sorted(ts))
    return result

def get_signature(p):
    n = 0
    for x in range(0,len(p)):
        for y in range(0, len(p)):
            if y > x and p[x] > p[y]:
                n += 1
    
    return (-1)**n
        
    pass

permutations = get_permutation_cycles(1,3)
sgn = [get_signature(p) for p in permutations]


## Format results

data = []
summands = []

for x in range(0, len(permutations)):
    row = [x+1, permutations[x], sgn[x]]
    current_sign = sgn[x]
    phi_vectors = list(permutations[x][0:1])
    psi_vectors = list(permutations[x][1:])
    prod = f"psi{phi_vectors}*phi{psi_vectors}"

    if current_sign < 0:
        prod = "-"+prod

    row.append(prod)
    summands.append(prod)
    data.append(row)

x = PrettyTable()
x.field_names = ["#", "Sigma", "sgn(s)", "sgn*phi*psi"]
x.add_rows(data)
print(x)

print(f"phi^psi = {' + '.join(summands)}")
