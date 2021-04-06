import itertools 
import math
from prettytable import PrettyTable
import numpy as np
from pandas import *

def get_form(form, vectors):
    # form should be an array with k elements, with no element less than 1 and greater than k
    # vectors should be an k x n numpy matrix
    
    # need to subtract one since forms are written with a start of 1
    m = np.array(vectors)[:, [f-1 for f in form]]
    
    # print(DataFrame(vectors, columns = [""]*vectors.shape[1]).to_string(index=False))
    return np.linalg.det(m)

def phi(va):
    vectors = np.array([va])
    return get_form([1], vectors) + get_form([2], vectors)

def psi(vb,vc):
    m1 = get_form([1,3], np.array([vb,vc]))
    m2 = get_form([2,4], np.array([vb,vc]))
    
    return m1+m2

def get_signature(p):
    n = 0
    for x in range(0,len(p)):
        for y in range(0, len(p)):
            if y > x and p[x] > p[y]:
                # print(f"{p}: {x} < {y} => {p[x]} > {p[y]}")
                n += 1
    
    return (-1)**n
        
    pass

def get_permutation_cycles(a,b):
    n = a+b
    s = list(range(1,n+1))
    result = itertools.combinations(s, a)
    for x in range(0, len(result)):
        ts = []
        for y in s:
            if y not in result[x]:
                ts.append(y)
        result[x] += sorted(ts)


positive_signature = ["123", "231", "312"]

v1 = [2,0,1,2]
v2 = [3,2,0,1]
v3 = [0,1,2,0]
v4 = [0,1,2,0]
v5 = [0,1,2,0]

result = 0
vectors = [v1,v2,v3]
permutations = list(itertools.permutations(list(range(1,len(vectors)+1))))

data = []
for x in range(0,len(permutations)):
    p = permutations[x]
    row = [p, get_signature(p), phi(vectors[p[0]-1]), psi(vectors[p[1]-1],vectors[p[2]-1])]
    row.append(math.prod(row[1:]))
    data.append(row)
    result += row[-1]

x = PrettyTable()
x.field_names = ["Sigma", "sgn(s)", "phi(va)", "psi(vb,vc)", "sgn(s)*phi(va)*psi(vb,vc)"]
x.add_rows(data)
print(x)
print(f"Total: {result}")


## Method 2

differential_forms = [
    [1,1,3],
    [1,2,4],
    [2,1,3],
    [2,4,2]
]

for p in differential_forms:
    m = get_form(p,np.array([v1,v2,v3]))
    print(m)
    



