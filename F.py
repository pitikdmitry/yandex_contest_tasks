from math import pi, sqrt, asin, sin


def checkDot(x_c, y_c, R):
    s = pi * R ** 2
    a_x = x_c
    a_y = y_c + R
    A_y = 1
    A_x_l = 0
    A_x_r = 1

    if a_y < A_y:
        #   OK
        pass
    elif a_y == A_y:
        #   OK
        pass
    else:

        x_r_cross = x + sqrt(R ** 2 - (1 - y) ** 2)
        x_l_cross = x - sqrt(R ** 2 - (1 - y) ** 2)

        if x_l_cross >= A_x_l and x_r_cross <= A_x_r:
            hord = x_r_cross - x_l_cross
            height = R - (a_y - 1)
            alpha = 2 * asin(hord / (2 * R))
            s_piece = R ** 2 * (alpha - sin(alpha)) / 2
            s -= s_piece
        elif x_l_cross < A_x_l and x_r_cross <= A_x_r and x_r_cross > A_x_l:

        elif x_l_cross >= A_x_l and x_l_cross < A_x_r and x_l_cross > A_x_r:

        elif x_l_cross < A_x_l and x_r_cross > A_x_r:

        else:
            print("smth wrong")



N, R = map(int, input().split())
chips = []
S = 0
for _ in range(N):
    x, y = map(int, input().split())
    chips.append((x, y))
    s = checkDot(x, y, R)
    S += s
