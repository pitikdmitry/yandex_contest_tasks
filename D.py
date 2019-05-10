"""
Alex has three lucky numbers: 5, 6, 10.
Also Alex has number N which hasn't got zeros.
He wants his favourite number to be divided at least on one of his favourite numbers.
For that he K times swaps any two numbers of N
"""


from collections import Counter
from math import factorial


def c_n_k_func(N: int, K: int = 2) -> int:
    return int(factorial(N) / (factorial(N - K) * factorial(K)))


def check_division_3(N: str) -> bool:
    summ = 0
    for c in N:
        summ += int(c)

    if summ % 3 == 0:
        return True
    return False


def check_division_2(N: str, K: int, counter: {}, c_n_k: int, c_n_k_len_minus_one: int) -> float:
    good_numbers = 0
    good_numbers += counter[2]
    good_numbers += counter[4]
    good_numbers += counter[6]
    good_numbers += counter[8]
    if good_numbers == 0:
        return float(0)

    if K == 0:
        if int(N[len(N) - 1]) % 2 == 0:
            return float(1)
        else:
            return float(0)

    on_end = 0
    elements = c_n_k ** K

    if int(N[len(N) - 1]) % 2 == 0:
        on_end = 1
    not_on_end = 1 - on_end

    if len(N) == 2:
        for k in range(0, K):
            on_end = not on_end
        if on_end:
            on_end = 1
        else:
            on_end = 0
    else:
        for k in range(1, K + 1):
            new_on_end = not_on_end * good_numbers

            new_on_end += on_end * ( c_n_k_len_minus_one + good_numbers - 1 )
            new_not_on_end = c_n_k ** k - new_on_end

            on_end = new_on_end
            not_on_end = new_not_on_end

    return on_end / elements


def check_division_6(N: str, K: int, counter: {}, c_n_k: int, c_n_k_len_minus_one: int) -> float:
    if not check_division_3(N):
        return float(0)

    return check_division_2(N, K, counter, c_n_k, c_n_k_len_minus_one)


def check_division_5(N: str, K: int, counter: {}, c_n_k: int, c_n_k_len_minus_one: int) -> float:
    good_numbers = counter[5]
    if good_numbers == 0:
        return float(0)

    if K == 0:
        if N[len(N) - 1] == str(5):
            return float(1)
        else:
            return float(0)

    on_end = 0
    elements = c_n_k ** K

    if N[len(N) - 1] == str(5):
        on_end = 1
    not_on_end = 1 - on_end

    if len(N) == 2:
        for k in range(0, K):
            on_end = not on_end
        if on_end:
            on_end = 1
        else:
            on_end = 0
    else:
        for k in range(1, K + 1):
            new_on_end = not_on_end * good_numbers

            new_on_end += on_end * ( c_n_k_len_minus_one + good_numbers - 1 )
            new_not_on_end = c_n_k ** k - new_on_end

            on_end = new_on_end
            not_on_end = new_not_on_end

    return on_end / elements


N = input()
K = int(input())
counter = Counter()

c_n_k = c_n_k_func(len(N), 2)
if len(N) <= 2:
    c_n_k_len_minus_one = -1
else:
    c_n_k_len_minus_one = c_n_k_func(len(N) - 1, 2)

for c in N:
    num = int(c)
    counter[num] += 1

div_5_probability = check_division_5(N, K, counter, c_n_k, c_n_k_len_minus_one)
div_6_probability = check_division_6(N, K, counter, c_n_k, c_n_k_len_minus_one)
if div_5_probability == 0 and div_6_probability != 0:
    print(div_6_probability)
elif div_5_probability != 0 and div_6_probability == 0:
    print(div_5_probability)
elif div_5_probability == 0 and div_6_probability == 0:
    print(0)
else:
    res = div_5_probability + div_6_probability
    if res > 1:
        res = 1
    print(res)
