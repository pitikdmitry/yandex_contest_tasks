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


def isSubsetSum(set, n, mul, k, prim_arr):

    subset = ([[None for _ in range(len(prim_arr) + 2)]
              for _ in range(n + 2)])

    f = 0
    indexes = {}
    for g in range(2, len(prim_arr) + 2):
        indexes[prim_arr[f]] = g
        subset[0][g] = prim_arr[f]
        f += 1

    for i in range(2, n + 2):
        for j in range(2, len(prim_arr) + 2):
            new_j = subset[0][j]
            if new_j < set[i - 2]:
                subset[i][j] = subset[i - 1][j]
            elif new_j == set[i - 2]:
                value = i - 2
                array = [value]
                subset[i][j] = array
            elif new_j > set[i - 2]:
                if set[i - 2] == 0:
                    subset[i][j] = subset[i - 1][j] # or None
                else:
                    j_index = new_j / set[i - 2]
                    if j_index.is_integer():
                        j_index = int(j_index)

                        j_index = indexes.get(j_index)
                        # j_index = indexes[j_index]
                        #
                        if j_index is None:
                            subset[i][j] = subset[i - 1][j]
                        elif subset[i - 1][j_index] is not None:
                            temp_arr = subset[i - 1][j_index].copy()
                            temp_arr.append(i - 2)
                            subset[i][j] = temp_arr
                        else:
                            subset[i][j] = subset[i - 1][j]
                    else:
                        subset[i][j] = subset[i - 1][j]

            if j == len(prim_arr) + 1:
                result = checkSolution(set, subset[i][j], mul, k)
                if result:
                    return result

    for i in range(2, n + 2):
        last = subset[i][len(subset[i]) - 1]
        result = checkSolution2(set, last, mul, k)
        if result:
            return result


def checkSolution(set, arr, mul, k):
    if arr is None:
        return None

    new_arr = []
    for val in arr:
        if set[val] != 1:
            new_arr.append(val)

    if k < len(new_arr):
        return None
    if k == len(new_arr):
        return new_arr
    elif k > len(new_arr) and k <= len(new_arr) + amount_of_ones:
        for i in range(0, k - len(new_arr)):
            new_arr.append(ones[i])
        return new_arr
    else:
        return None


def checkSolution2(set, arr, mul, k):
    if arr is None:
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
    elif k < len(new_arr):
        return new_arr.extend([ones[i] for i in range(k - len(new_arr))])


m_n_k = input()
m_n_k = m_n_k.split()
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
    indexes = []
    for i in range(len(new_arr)):
        if new_arr[i] == 1:
            indexes.append(i)
            if len(indexes) == k:
                break

    for val in indexes:
        print(val + 1, end=" ")
elif k == 1:
    for i in range(len(new_arr)):
        if new_arr[i] == m:
            print(i + 1, end=" ")
            break
elif n == k:
    for i in range(len(new_arr)):
        print(i + 1, end=" ")
elif n == 1:
    print(1, end=" ")
else:
    prim_arr = [m]
    prim_arr.extend(new_arr)
    prim_arr = sorted(prim_arr)
    prim_arr = delete_dubl(prim_arr)
    res = isSubsetSum(new_arr, n, m, k, prim_arr)
    for idx in res:
        print(idx + 1, end=" ")
