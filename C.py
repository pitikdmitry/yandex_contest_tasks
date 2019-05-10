"""
Given string encoded in RLE (run-length) format for ex. abbcaaa -> a2bc3a.
You will have q queries
Every query have digits l and r, which are indices of characters of not coded string.
You need to find length of encoded string t[l, r]
"""


def find_coded_len(s, l, r) -> int:
    i, j, counter = 0, 0, 0

    while i < len(s):
        number = ""
        while i < len(s) and s[i].isdigit():
            number += s[i]
            i += 1

        # letter = s[i]
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
