from math import pi, sqrt, asin, sin
import scipy.integrate as integrate


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

        if x_l_cross >= A_x_l and x_r_cross <= A_x_r:# without pieces
            hord = x_r_cross - x_l_cross
            # height = R - (a_y - 1)
            alpha = 2 * asin(hord / (2 * R))
            s_piece = R ** 2 * (alpha - sin(alpha)) / 2
            s -= s_piece
        elif x_l_cross < A_x_l and x_r_cross <= A_x_r and x_r_cross > A_x_l:# with left piece, delete small part of piece
            h_triangle = 1 - y_c
            osn_triangle = x_r_cross
            s_triangle = osn_triangle * h_triangle / 2
            from_c_to_corner = sqrt((x_c - 0) ** 2 + (y_c - 1) ** 2)
            alpha = asin(2 * s_triangle / (from_c_to_corner * R))
            s_piece = R ** 2 * alpha / 2
            s -= s_piece
            # next need to go to left pair
        elif x_l_cross >= A_x_l and x_l_cross < A_x_r and x_l_cross > A_x_r:
            h_triangle = 1 - y_c
            osn_triangle = 1 - x_r_cross
            s_triangle = osn_triangle * h_triangle / 2
            from_c_to_corner = sqrt((x_c - 1) ** 2 + (y_c - 1) ** 2)
            alpha = asin(2 * s_triangle / (from_c_to_corner * R))
            s_piece = R ** 2 * alpha / 2
            s -= s_piece
            # next need to go to right pair
        elif x_l_cross < A_x_l and x_r_cross > A_x_r:
            h_triangle = 1 - y_c
            osn_triangle = 1
            s_triangle = osn_triangle * h_triangle / 2
            from_c_to_left_corner = sqrt((x_c - 0) ** 2 + (y_c - 1) ** 2)
            from_c_to_right_corner = sqrt((x_c - 1) ** 2 + (y_c - 1) ** 2)
            alpha = asin(2 * s_triangle / (from_c_to_left_corner * from_c_to_right_corner))
            s_piece = R ** 2 * alpha / 2
            s -= s_piece
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
