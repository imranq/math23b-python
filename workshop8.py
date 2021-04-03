import itertools 
import math
from prettytable import PrettyTable
import numpy as np
from pandas import *

def get_form(form, vectors):
    # form should be an array with k elements, with no element less than 1 and greater than k
    # vectors should be an n x k numpy matrix
    
    # need to subtract one since forms are written with a start of 1
    m = np.array(vectors)[[f-1 for f in form],:]
    
    # print(DataFrame(vectors, columns = [""]*vectors.shape[1]).to_string(index=False))
    return np.linalg.det(m)

def phi(va):
    vectors = np.array([va]).T
    return get_form([1], vectors) + get_form([2], vectors)

def psi(vb,vc):
    m1 = get_form([1,3], np.array([vb,vc]).T)
    m2 = get_form([2,4], np.array([vb,vc]).T)
    
    return m1+m2

positive_signature = ["123", "231", "312"]

v1 = [2,0,1,2]
v2 = [3,2,0,1]
v3 = [0,1,2,0]

result = 0
vectors = [v1,v2,v3]
permutations = list(itertools.permutations([1,2,3]))

data = []
for x in range(0,len(permutations)):
    p = permutations[x]
    row = [p, 1, phi(vectors[p[0]-1]), psi(vectors[p[1]-1],vectors[p[2]-1])]
    
    if not "".join([str(i) for i in p]) in positive_signature:
        row[1] = -1
    
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
    [2,2,4]
]

for p in differential_forms:
    m = get_form(p,np.array([v1,v2,v3]).T)
    print(m)
    



