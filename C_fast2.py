def create_cash(s, cash):
    i, j = 0, 1

    while i < len(s):
        number = ""
        while i < len(s) and s[i].isdigit():
            number += s[i]
            i += 1

        letter = s[i]
        i += 1
        j += 1

        if number == "":
            number = 1
        else:
            number = int(number)

        previous = cash[len(cash) - 1]
        if number == "":
            number = 1
            new_val_1 = previous[1] + 1
            cash.append((j, new_val_1))
        else:
            number = int(number)
            new_val_1 = previous[1] + 1
            cash.append((j, new_val_1))

            j += 1
            new_val_2 = previous[1] + 2
            # for k in range(number - 1):
            cash.append((j, new_val_2))

        j += number + 1


    print()


def find_coded_len(l, r, cash):
    res = cash[r] - cash[l - 1]
    return res


s = input()
q = int(input())
cash = [(0, 0)]
create_cash(s, cash)

for i in range(q):
    l, r = map(int, input().split())
    print(find_coded_len(l, r, cash))

