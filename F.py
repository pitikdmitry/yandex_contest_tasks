from math import pi, sqrt, asin, sin
import scipy.integrate as integrate
def check_direction(x_l_cross, x_r_cross, A_x_l, A_x_r, A_y, h_triangle, R, x_c, y_c):
    s_piece = 0
    if x_l_cross >= A_x_l and x_r_cross <= A_x_r:  # without pieces
        hord = x_r_cross - x_l_cross
        # height = R - (a_y - 1)
        alpha = 2 * asin(hord / (2 * R))
        s_piece = R ** 2 * (alpha - sin(alpha)) / 2
    elif x_l_cross < A_x_l and x_r_cross <= A_x_r and x_r_cross > A_x_l:  # with left piece, delete small part of piece
        osn_triangle = x_r_cross
        s_triangle = osn_triangle * h_triangle / 2
        from_c_to_left_corner = sqrt((x_c - A_x_l) ** 2 + (y_c - A_y) ** 2)
        alpha = asin(2 * s_triangle / (from_c_to_left_corner * R))
        s_piece = R ** 2 * alpha / 2
        # next need to go to left pair
    elif x_l_cross >= A_x_l and x_l_cross < A_x_r and x_l_cross > A_x_r:
        osn_triangle = 1 - x_l_cross
        s_triangle = osn_triangle * h_triangle / 2
        from_c_to_right_corner = sqrt((x_c - A_x_r) ** 2 + (y_c - A_y) ** 2)
        alpha = asin(2 * s_triangle / (from_c_to_right_corner * R))
        s_piece = R ** 2 * alpha / 2
        # next need to go to right pair
    elif x_l_cross < A_x_l and x_r_cross > A_x_r:
        osn_triangle = 1
        s_triangle = osn_triangle * h_triangle / 2
        from_c_to_left_corner = sqrt((x_c - A_x_l) ** 2 + (y_c - A_y) ** 2)
        from_c_to_right_corner = sqrt((x_c - A_x_r) ** 2 + (y_c - A_y) ** 2)
        alpha = asin(2 * s_triangle / (from_c_to_left_corner * from_c_to_right_corner))
        s_piece = R ** 2 * alpha / 2
    else:
        print("smth wrong")
    return s_piece


def checkDot(x_c, y_c, R):
    s = pi * R ** 2

    #high
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

        x_r_cross = x_c + sqrt(R ** 2 - (1 - y_c) ** 2)
        x_l_cross = x_c - sqrt(R ** 2 - (1 - y_c) ** 2)
        h_triangle = 1 - y_c
        s_piece = 0

        if x_l_cross >= A_x_l and x_r_cross <= A_x_r:# without pieces
            hord = x_r_cross - x_l_cross
            # height = R - (a_y - 1)
            alpha = 2 * asin(hord / (2 * R))
            s_piece = R ** 2 * (alpha - sin(alpha)) / 2
        elif x_l_cross < A_x_l and x_r_cross <= A_x_r and x_r_cross > A_x_l:# with left piece, delete small part of piece
            osn_triangle = x_r_cross
            s_triangle = osn_triangle * h_triangle / 2
            from_c_to_left_corner = sqrt((x_c - A_x_l) ** 2 + (y_c - A_y) ** 2)
            alpha = asin(2 * s_triangle / (from_c_to_left_corner * R))
            s_piece = R ** 2 * alpha / 2
            # next need to go to left pair
        elif x_l_cross >= A_x_l and x_l_cross < A_x_r and x_l_cross > A_x_r:
            osn_triangle = 1 - x_l_cross
            s_triangle = osn_triangle * h_triangle / 2
            from_c_to_right_corner = sqrt((x_c - A_x_r) ** 2 + (y_c - A_y) ** 2)
            alpha = asin(2 * s_triangle / (from_c_to_right_corner * R))
            s_piece = R ** 2 * alpha / 2
            # next need to go to right pair
        elif x_l_cross < A_x_l and x_r_cross > A_x_r:
            osn_triangle = 1
            s_triangle = osn_triangle * h_triangle / 2
            from_c_to_left_corner = sqrt((x_c - A_x_l) ** 2 + (y_c - A_y) ** 2)
            from_c_to_right_corner = sqrt((x_c - A_x_r) ** 2 + (y_c - A_y) ** 2)
            alpha = asin(2 * s_triangle / (from_c_to_left_corner * from_c_to_right_corner))
            s_piece = R ** 2 * alpha / 2
        else:
            print("smth wrong")
        s -= s_piece

    #down
    b_x = x_c
    b_y = y_c - R
    B_y = 0
    B_x_l = 0
    B_x_r = 1
    if b_y > B_y:
        #OK
        pass
    elif b_y == B_y:
        #OK
        pass
    else:
        x_r_cross = x_c + sqrt(R ** 2 - y_c ** 2)
        x_l_cross = x_c - sqrt(R ** 2 - y_c ** 2)
        h_triangle = y_c
        s_piece = 0

        if x_l_cross >= B_x_l and x_r_cross <= B_x_l:   # without pieces
            hord = x_r_cross - x_l_cross
            # height = R - (a_y - 1)
            alpha = 2 * asin(hord / (2 * R))
            s_piece = R ** 2 * (alpha - sin(alpha)) / 2
        elif x_l_cross < B_x_l and x_r_cross <= A_x_r and x_r_cross > A_x_l:# with left piece, delete small part of piece
            osn_triangle = x_r_cross
            s_triangle = osn_triangle * h_triangle / 2
            from_c_to_left_corner = sqrt((x_c - B_x_l) ** 2 + (y_c - B_y) ** 2)
            alpha = asin(2 * s_triangle / (from_c_to_left_corner * R))
            s_piece = R ** 2 * alpha / 2
            # next need to go to left pair
        elif x_l_cross >= A_x_l and x_l_cross < A_x_r and x_l_cross > A_x_r:
            osn_triangle = 1 - x_l_cross
            s_triangle = osn_triangle * h_triangle / 2
            from_c_to_right_corner = sqrt((x_c - B_x_r) ** 2 + (y_c - B_y) ** 2)
            alpha = asin(2 * s_triangle / (from_c_to_right_corner * R))
            s_piece = R ** 2 * alpha / 2
            # next need to go to right pair
        elif x_l_cross < A_x_l and x_r_cross > A_x_r:
            osn_triangle = 1
            s_triangle = osn_triangle * h_triangle / 2
            from_c_to_left_corner = sqrt((x_c - B_x_l) ** 2 + (y_c - B_y) ** 2)
            from_c_to_right_corner = sqrt((x_c - B_x_r) ** 2 + (y_c - B_y) ** 2)
            alpha = asin(2 * s_triangle / (from_c_to_left_corner * from_c_to_right_corner))
            s_piece = R ** 2 * alpha / 2
        else:
            print("smth wrong")
        s -= s_piece


N, R = map(int, input().split())
chips = []
S = 0
for _ in range(N):
    x, y = map(int, input().split())
    chips.append((x, y))
    s = checkDot(x, y, R)
    S += s
