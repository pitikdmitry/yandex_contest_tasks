def func(arr, m, start, k, cur_elements):
    print(arr[start])
    cur_elements += str(arr[start])

    for i in range(start, k):
        func(arr, m, i, k, cur_elements)



m_n_k = input()
m_n_k =  m_n_k.split()
n = int(m_n_k[0])
m = int(m_n_k[1])
k = int(m_n_k[2])
arr = input()
arr = arr.split()
new_arr = []
for el in arr:
    new_arr.append(int(el))

func(new_arr, m, 0, k, "")
