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

        return

    i = start
    while (i <= end and end - i + 1 >= r - index):
        data[index] = arr[i] # tuple(value, [indexes])
        combinationUtil(arr, data, i + 1, end, index + 1, r, m)
        i += 1


m_n_k = input()
m_n_k = m_n_k.split()
n = int(m_n_k[0])
m = int(m_n_k[1]) # multi
k = int(m_n_k[2]) # k elements
arr = input()
arr = arr.split()

counter = {}
new_arr = []
for idx, el in enumerate(arr):
    element = int(el)
    if element not in counter:
        counter[element] = [idx]
    else:
        counter[element].append(idx)

for key, value in counter.items():
    new_arr.append((key, value))


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
    found = False
    printCombination(new_arr, len(new_arr), k, m)
