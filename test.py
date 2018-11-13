from itertools import permutations
from functools import reduce

arr = "12535"
counter = 0
all = 0
for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        a = arr[:i]
        b= arr[i + 1:j]
        c =arr[j + 1:]
        new_arr = arr[:i] + arr[j] + arr[i + 1:j] + arr[i] + arr[j + 1:]
        if new_arr[len(new_arr) - 1] == '5':
            counter += 1
        all += 1
        print(new_arr, end="   ")


print("")
print(counter)
print(all)
