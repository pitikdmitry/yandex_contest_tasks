def printCombination():
    five = 0
    not_five = 0
    values = ["4235221"]
    K = 4

    for k in range(K):
        l = 0
        new_values = []
        while l < len(values):
            arr = values[l]
            for i in range(len(arr)):
                for j in range(i + 1, len(arr)):
                    new_arr = arr[:i] + arr[j] + arr[i + 1:j] + arr[i] + arr[j + 1:]
                    if k == K - 1:
                        if new_arr[len(new_arr) - 1] == '5':
                            five += 1
                        else:
                            not_five += 1
                    new_values.append(new_arr)
            l += 1
        values = new_values

    print(five, end=" ")
    print(not_five)



printCombination()
