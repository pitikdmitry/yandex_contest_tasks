def find_coded_len(s, l, r):
    i, j, counter = 0, 0, 0

    while i < len(s):
        letter = s[i]
        i += 1

        number = ""
        if i < len(s):
            while s[i].isdigit():
                if i == len(s):
                    break
                number += s[i]
                i += 1

        if number == "":
            number = 1
        else:
            number = int(number)

        value = 0
        if l <= j <= r and j + number - 1 <= r:
            value = number
        elif l <= j <= r and j + number - 1 > r:
            value = r - j + 1
        elif j < l and l <= j + number - 1 <= r:
            value = j + number - 1 - l + 1
        elif j < l and j + number - 1 > r:
            value = r - l + 1
        elif j < l and j + number - 1 < l:
            j += number
            continue
        elif j > l and j + number - 1 > l:
            return counter
        else:
            print("wrong diapason")

        if value == 1:
            counter += 1
        elif value > 1:
            counter += 1 + len(str(value))

        j += number

    return counter


s = input()
q = int(input())
for i in range(q):
    l, r = map(int, input().split())
    print(find_coded_len(s, l - 1, r - 1))
