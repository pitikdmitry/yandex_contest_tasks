def delete_dubl(arr):

    new_arr = []
    new_arr.append(arr[0])
    previous = arr[0]

    for i in range(1, len(arr)):
        if arr[i] == previous:
            continue
        else:
            new_arr.append(arr[i])
            previous = arr[i]
    return new_arr


def primfacs(n):
    i = 2
    primfac = []

    while i * i <= n:
        while n % i == 0:
            primfac.append(i)
            primfac.append(int(n))
            n = n / i
        i = i + 1
    if n > 1:
        primfac.append(int(n))

    return primfac


def isSubsetSum(set, n, mul, k, prim_arr):

    subset = ([[None for i in range(len(prim_arr) + 2)]
              for i in range(n + 2)])
    # If sum is not 0 and set is empty,
    # then answer is false
    subset[0][0] = None
    subset[0][1] = None
    j = 0
    indexes = {}
    for i in range(2, len(prim_arr) + 2):
        indexes[prim_arr[j]] = i
        subset[0][i] = prim_arr[j]
        subset[1][i] = None
        j += 1

    # If sum is 0, then answer is true
    for i in range(n + 1):
        subset[i][0] = None
        subset[i][1] = None

    # Fill the subset table in botton up manner
    for i in range(2, n + 2):
        for j in range(2, len(prim_arr) + 2):
            new_j = subset[0][j]
            if new_j < set[i - 2]:
                subset[i][j] = subset[i - 1][j]
            elif new_j == set[i - 2]:
                subset[i][j] = [i - 2]
            elif new_j > set[i - 2]:
                j_index = new_j / set[i - 2]
                if j_index.is_integer():
                    j_index = int(j_index)

                    j_index = indexes.get(j_index)
                    # j_index = indexes[j_index]
                    #
                    if j_index is None:
                        subset[i][j] = subset[i - 1][j]
                    elif subset[i - 1][j_index] is not None and len(subset[i - 1][j_index]) > 0:
                        new_arr = subset[i - 1][j_index].copy()
                        new_arr.append(i - 2)
                        subset[i][j] = new_arr
                    else:
                        subset[i][j] = subset[i - 1][j]
                else:
                    subset[i][j] = subset[i - 1][j]

            if j == len(prim_arr) + 1:
                result = checkSolution(set, subset[i][j], mul, k)
                if result:
                    return result

    print()


def checkSolution(set, arr, mul, k):
    if arr is None:
        return None

    if k < len(arr):
        return None

    new_arr = []
    for val in arr:
        if set[val] != 1:
            new_arr.append(val)

    if k == len(new_arr):
        return new_arr
    elif k > len(new_arr) and k <= len(new_arr) + amount_of_ones:
        for i in range(0, k - len(new_arr)):
            new_arr.append(ones[i])
        return new_arr
    else:
        return None
    # print(last_column_arr)


m_n_k = input()
m_n_k =  m_n_k.split()
n = int(m_n_k[0])
m = int(m_n_k[1])
k = int(m_n_k[2])
arr = input()
arr = arr.split()
new_arr = []
amount_of_ones = 0
ones = []
for idx, el in enumerate(arr):
    element = int(el)
    if element == 1:
        amount_of_ones += element
        ones.append(idx)
        new_arr.append(element)
    else:
        new_arr.append(element)

n = len(new_arr)

if m == 0:
    counter = 0
    res = []
    has_zero = False
    for i in range(k):
        if new_arr[i] == 0:
            has_zero = True
        res.append(i)
        counter += 1

    if not has_zero:
        for i in range(len(new_arr)):
            if new_arr[i] == 0:
                res[0] = i
                break

    for val in res:
        print(val + 1, end=" ")
elif m == 1:
    for _ in range(k):
        print(1, end=" ")
elif k == 1:
    for i in range(len(new_arr)):
        if new_arr[i] == m:
            print(i + 1)
            break
else:
    prim_arr = primfacs(m)
    prim_arr.extend(new_arr)
    prim_arr = sorted(prim_arr)
    prim_arr = delete_dubl(prim_arr)
    res = isSubsetSum(new_arr, n, m, k, prim_arr)
    for idx in res:
        print(idx + 1, end=" ")

# 4 8 2
# 2 3 4 5
# 7 8 3
# 2 2 3 2 3 4 2
