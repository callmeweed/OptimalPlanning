import numpy as np
import random

#Read data from path
def read_data(path):
    f = open(path)
    fa = f.readlines()
    tmp = fa[0].split()
    N = int(tmp[0])
    D = int(tmp[1])
    a = int(tmp[2])
    b = int(tmp[3])
    day_off = np.zeros([N,D], dtype = int)
    for i in range(1,len(fa)) :
        tmp = fa[i].split()
        for j in range(len(tmp) - 1) :
            m = int(tmp[j])
            day_off[i-1,m-1] = 1
    return N, D, a, b, day_off

def Fitness (sol, N, D) :
    bug = []
    constraint_day_off = 0
    for i in range(N) :
        for j in range(1, D) :
            if sol[i][j-1] == 4 and sol[i][j] > 0 :
                constraint_day_off += 1
                bug.append([i,j-1])
    num_night = np.zeros(N, dtype=int)
    for i in range(N) :
        for j in range(D) :
            if sol[i][j] == 4 :
                num_night[i] += 1
    max_night = max(num_night)
    return (100*constraint_day_off + max_night) , bug



# N, D, a, b, day_off =read_data("TestCase/8_6_1_3.txt")
# print(N, D, a, b, day_off)

sol = [
    [4, 1, 1, 0, 4, 1],
    [1, 0, 1, 4, 1, 4],
    [0,4,0,1,1,0],
    [1,1,1,1,0,1],
    [1,0,4,1,1,1]
]

e, f = Fitness(sol, 5, 6)
print(e, f)

