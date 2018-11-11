def isSubsetSum(set, n, mul, k):
    for i in range(100):
        subset = ([[None for i in range(mul + 1)]
                   for i in range(n + 2)])

    subset = ([[None for i in range(mul + 1)]
              for i in range(n + 2)])
    # If sum is not 0 and set is empty,
    # then answer is false
    for i in range(mul + 1):
        subset[0][i] = None
        subset[1][i] = None

    # If sum is 0, then answer is true
    for i in range(n + 1):
        subset[i][0] = None
        subset[i][1] = None

    # Fill the subset table in botton up manner
    for i in range(2, n + 2):
        for j in range(2, mul + 1):

            if j < set[i - 2]:
                subset[i][j] = subset[i - 1][j]
            if j == set[i - 2]:
                subset[i][j] = [i - 2]

            if j > set[i - 2]:
                j_index = j / set[i - 2]
                if j_index.is_integer():
                    j_index = int(j_index)

                    if subset[i - 1][j_index] is not None and len(subset[i - 1][j_index]) > 0:
                        new_arr = subset[i - 1][j_index].copy()
                        new_arr.append(i - 2)
                        subset[i][j] = new_arr
                    else:
                        subset[i][j] = subset[i - 1][j]
                else:
                    subset[i][j] = subset[i - 1][j]

            if j == mul:
                result = checkSolution(set, subset[i][j], mul, k)
                if result:
                    return result



    # uncomment this code to print table
    # for i in range(n+1):
    #     for j in range(mul+1):
    #         print(subset[i][j], end=" ")
    #     print()


    # #find_solution
    # for i in range(len(subset)):
    #     last_column_arr = subset[i][len(subset[i]) - 1]
    #     checkSolution(set, last_column_arr, mul, k)


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

all_multiplies = set()
for i in range(len(new_arr)):
    for j in range(i, len(new_arr)):
        all_multiplies.add(new_arr[i] * new_arr[j])

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
    res = isSubsetSum(new_arr, n, m, k)
    for idx in res:
        print(idx + 1, end=" ")

# 4 8 2
# 2 3 4 5
# 7 8 3
# 2 2 3 2 3 4 2
