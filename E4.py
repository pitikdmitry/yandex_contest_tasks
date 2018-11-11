def primfacs(n):
   i = 2
   primfac = []
   while i * i <= n:
       while n % i == 0:
           primfac.append(i)
           n = n / i
       i = i + 1
   if n > 1:
       primfac.append(int(n))
   return primfac


def checkDigits(arr):
    if len(arr) == 0:
        return False

    indexes = []

    new_counter = {}
    for val in arr:
        if val in counter:
            new_counter[val] = counter[val]
        else:
            return False

    for val in arr:
        amount = new_counter[val][0]
        if amount > 0:
            new_counter[val][0] -= 1
            indexes.append(new_counter[val][1].pop(0))
        else:
            return False

    for val in indexes:
        print(val + 1, end=" ")

    return True


def checkCombinations(arr, k):
    global found

    if found:
        return

    if len(arr) == k:
        # print(arr)
        res = checkDigits(arr)
        if res:
            found = True
            return
        else:
            return

    for i in range(0, len(arr)):
        for j in range(i + 1, len(arr)):
            new_val = arr[i] * arr[j]
            new_arr = []
            new_arr.extend(arr[:i])
            if i + 1 < len(arr):
                new_arr.extend(arr[i + 1:j])
            if j + 1 < len(arr):
                new_arr.extend(arr[j + 1:])

            new_arr.append(new_val)

            checkCombinations(new_arr, k)


m_n_k = input()
m_n_k = m_n_k.split()
n = int(m_n_k[0])
m = int(m_n_k[1]) # multi
k = int(m_n_k[2]) # k elements
arr = input()
arr = arr.split()


counter = {}
ones = 0
new_arr = []
for idx, el in enumerate(arr):
    element = int(el)
    new_arr.append(element)
    if element == 1:
        ones += 1
    if element not in counter:
        counter[element] = [1, [idx]]
    else:
        counter[element][1].append(idx)
        counter[element][0] += 1

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
    primaries = primfacs(m)
    primaries.extend([1 for _ in range(ones)])
    checkCombinations(primaries, k)
