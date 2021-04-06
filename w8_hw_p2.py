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

permutations = get_permutation_cycles(2,3)
sgn = [get_signature(p) for p in permutations]


## Format results
eq_pair = [2,4]

data = []
for x in range(0, len(permutations)):
    updated_permutation = list(permutations[x])
    id = updated_permutation.index(eq_pair[0])
    updated_permutation[id] = eq_pair[1]
    
    row = [x+1, permutations[x], updated_permutation, sgn[x]]
    prod = ""
    current_sign = sgn[x]
    phi_vectors = updated_permutation[0:2]
    psi_vectors = updated_permutation[2:]

    if len(phi_vectors) != len(set(phi_vectors)):
        row.append(0)
        prod = "0"
    else:
        row.append(f"phi{phi_vectors}")
        prod += f"{row[-1]}"
    
    if len(psi_vectors) != len(set(psi_vectors)):
        row.append(0)
        prod = "0"
    else:
        row.append(f"psi{psi_vectors}")
        if prod != "0":
            prod += "*"+row[-1]

    if current_sign < 0 and prod != "0":
        row.append(f"-{prod}")
    else:
        row.append(f"{prod}")

    if prod != "0":
        current_sign *= get_signature(phi_vectors)*get_signature(psi_vectors)
        if current_sign < 0:
            prod = f"-psi{sorted(phi_vectors)}*psi{sorted(psi_vectors)}"
        else:
            prod = f"psi{sorted(phi_vectors)}*psi{sorted(psi_vectors)}"
        
    row.append(prod)
    data.append(row)

x = PrettyTable()
x.field_names = ["#", "Sigma", "v2 = v4", "sgn(s)", "phi(va,vb)", "psi(vc,vd,ve)", "sgn*phi*psi","sorted sgn*phi*psi"]
x.add_rows(data)
print(x)
