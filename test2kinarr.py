def printCombination(arr, n, r):
    data = [0 for x in range(r)]

    combinationUtil(arr, data, 0, n - 1, 0, 3)


def combinationUtil(arr, data, start, end, index, r):
    # print(data)
    if index == r:

        print(data)
        return

    stop = min(len(arr), start + 3)
    for i in range(start, stop):#maybe + 1
        data[index] = arr[i]
        combinationUtil(arr, data, i + 1, end, index + 1, r)


m_n_k = input()
m_n_k =  m_n_k.split()
n = int(m_n_k[0])
m = int(m_n_k[1]) # multi
k = int(m_n_k[2]) # k elements
arr = input()
arr = arr.split()
new_arr = []
for el in arr:
    new_arr.append(int(el))


n = len(new_arr)
printCombination(arr, n, k)