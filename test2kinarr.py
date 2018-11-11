def check_multiplication(data, arr, m):
    multi = None
    for index in data:
        if multi == None:
            multi = arr[index]
        else:
            multi *= arr[index]
    if multi == m:
        return True
    else:
        return False


def printCombination(arr, n, r, m):
    data = [0 for x in range(r)]

    combinationUtil(arr, data, 0, n - 1, 0, r, m)


def combinationUtil(arr, data, start, end, index, r, m):
    # print(data)
    global found
    if found:
        return

    if index == r:
        # if check_multiplication(data, arr, m):
        if check_multiplication(data, arr, m) and not found:
            found = True
            for index in data:
                index = index + 1
                print(str(index), end=" ")

            print("")
        return

    i = start
    while (i <= end and end - i + 1 >= r - index) and not found:
        data[index] = i

        combinationUtil(arr, data, i + 1, end, index + 1, r, m)

        i += 1


m_n_k = input()
m_n_k = m_n_k.split()
n = int(m_n_k[0])
m = int(m_n_k[1]) # multi
r = int(m_n_k[2]) # k elements
arr = input()
arr = arr.split()
new_arr = []
for el in arr:
    el = int(el)
    if el > m:
        continue

    new_arr.append(el)


n = len(new_arr)
found = False

if m == 0:
    counter = 0
    res = []
    has_zero = False
    for i in range(r):
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
        print(val, end=" ")
elif m == 1:
    for _ in range(r):
        print(1, end=" ")
else:
    printCombination(new_arr, len(new_arr), r, m)