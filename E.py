# def get_digits(arr, result, delte):
#     #needed sorted array
#     #set
#     new_delte = []
#     for de in delte:
#         for val in arr:
#             new_val = de / val
#             if new_val.is_integer():
#                 if new_val not in new_delte:
#                     new_delte.append(new_val)
#     if len(new_delte) == 0:
#         return result
#     else:
#         return get_digits(arr, result, new_delte)
def get_array(s):
    arr= []
    for val in s:
        arr.append(val)
    return arr


def get_digits(arr, result, m):
    new_s = []
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            new_val = arr[i] * arr[j]
            if new_val < m:
                new_s.append(new_val)

    # if len(new_s) > 0:
    #     result.extend(new_s)
    #     return get_digits(new_s, result, m)
    # else:
        return result


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

    indexes = {}
    for g in range(2, len(prim_arr) + 2):
        element = prim_arr[g - 2]
        subset[0][g] = element
        indexes[element] = g

    for i in range(2, n + 2):
        for j in range(2, len(prim_arr) + 2):
            new_mul = subset[0][j] # то произведение которые мы хотим высчимтать
            if new_mul < set[i - 2]:
                subset[i][j] = subset[i - 1][j]
            elif new_mul == set[i - 2]: # можем ли получить new_mul текущим эелементом из set
                value = i - 2
                array = [value]
                subset[i][j] = array
            elif new_mul > set[i - 2]:
                if set[i - 2] == 0:
                    subset[i][j] = subset[i - 1][j] # or None
                else:
                    needed_element = new_mul / set[i - 2] # нам нужен этот элемент он результат от деления
                    if needed_element.is_integer():
                        needed_element = int(needed_element)

                        index = indexes.get(needed_element)

                        if index is None:
                            subset[i][j] = subset[i - 1][j]
                        elif subset[i - 1][index] is not None:
                            temp_arr = subset[i - 1][index].copy()
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

    # for i in range(2, n + 2):
    #     last = subset[i][len(subset[i]) - 1]
    #     result = checkSolution2(set, last, mul, k)
    #     if result:
    #         return result
    return [0, 0, 0, 0]


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
    # prim_arr = [m]
    # new_arr = delete_dubl(new_arr)
    # new_arr = sorted(new_arr)
    result = []
    res_prim = get_digits(new_arr, result, m)
    res_prim.append(m)
    res_prim = new_arr + res_prim
    res_prim = sorted(res_prim)
    res_prim = delete_dubl(res_prim)

    res = isSubsetSum(new_arr, n, m, k, res_prim)
    for idx in res:
        print(idx + 1, end=" ")
# Print()