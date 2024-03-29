"""
You have an array A length N of non-negative integers,
you also have number M. You need to choose K elements from array A,
that their production was equal to M
"""


from itertools import permutations
from functools import reduce


m_n_k = input()
m_n_k =  m_n_k.split()

n = int(m_n_k[0])
m = int(m_n_k[1])

k = int(m_n_k[2])
arr = input()
arr = arr.split()

new_arr = []
indexes = {}

for idx, el in enumerate(arr):
    el = int(el)
    new_arr.append(el)
    if el not in indexes:
        indexes[el] = [idx]
    else:
        indexes[el].append(idx)


perm = permutations(new_arr, k)

stop = False
for arr in list(perm):
    mul = reduce(lambda x, y: x * y, arr)
    if mul == m:
        for value in arr:
            print(indexes[value][0] + 1)
            indexes[value].pop(0)
        break
