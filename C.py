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

        if j <= l <= j + number:
            if j + number <= r:
                if j + number - l == 0:
                    counter += 1
                elif j + number - l > 0:
                    counter += 1 + len(str(j + number - l))
            else:
                if l - r == 0:
                    counter += 1
                elif l - r > 0:
                    counter += 1 + len(str(l - r))
        else:
            if j + number <= r:
                if number == 1:
                    counter += 1
                elif number > 1:
                    counter += 1 + len(str(number))
            elif j + number > r and j > r:
                if r - j == 1:
                    counter += 1
                elif r - j > 1:
                    counter += 1 + len(str(r - j))
            else:
                break

        j += number

    return counter


s = input()
q = int(input())
for i in range(q):
    l, r = map(int, input().split())
    print(find_coded_len(s, l - 1, r - 1))
