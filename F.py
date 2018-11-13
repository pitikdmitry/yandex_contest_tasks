from math import pi, sqrt, asin, sin


def check_direction(A_x_l, A_x_r, A_y, R, x_c, y_c):
    x_r_cross = x_c + sqrt(R ** 2 - (A_y - y_c) ** 2)
    x_l_cross = x_c - sqrt(R ** 2 - (A_y - y_c) ** 2)
    h_triangle = abs(A_y - y_c)

    # if change_direction:
    #     y_r_cross = x_c + sqrt(R ** 2 - (A_y - y_c) ** 2)
    #     y_l_cross = x_c - sqrt(R ** 2 - (A_y - y_c) ** 2)
    #     h_triangle = abs(A_y - x_c)

    s_piece = 0
    if x_l_cross >= A_x_l and x_r_cross <= A_x_r:  # without pieces
        hord = x_r_cross - x_l_cross
        alpha = 2 * asin(hord / (2 * R))
        s_piece = R ** 2 * (alpha - sin(alpha)) / 2
    elif x_l_cross < A_x_l and x_r_cross <= A_x_r and x_r_cross > A_x_l:  # with left piece, delete small part of piece
        osn_triangle = x_r_cross
        s_triangle = osn_triangle * h_triangle / 2
        from_c_to_left_corner = sqrt((x_c - A_x_l) ** 2 + (y_c - A_y) ** 2)
        alpha = asin(2 * s_triangle / (from_c_to_left_corner * R))
        s_piece = (R ** 2 * alpha / 2) - s_triangle
    elif x_l_cross >= A_x_l and x_l_cross < A_x_r and x_l_cross > A_x_r:
        osn_triangle = 1 - x_l_cross
        s_triangle = osn_triangle * h_triangle / 2
        from_c_to_right_corner = sqrt((x_c - A_x_r) ** 2 + (y_c - A_y) ** 2)
        alpha = asin(2 * s_triangle / (from_c_to_right_corner * R))
        s_piece = (R ** 2 * alpha / 2) - s_triangle
    elif x_l_cross < A_x_l and x_r_cross > A_x_r:
        osn_triangle = 1
        s_triangle = osn_triangle * h_triangle / 2
        from_c_to_left_corner = sqrt((x_c - A_x_l) ** 2 + (y_c - A_y) ** 2)
        from_c_to_right_corner = sqrt((x_c - A_x_r) ** 2 + (y_c - A_y) ** 2)
        alpha = asin(2 * s_triangle / (from_c_to_left_corner * from_c_to_right_corner))
        s_piece = (R ** 2 * alpha / 2) - s_triangle
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

    if a_y > A_y:
        s_piece = check_direction(A_x_l=A_x_l, A_x_r=A_x_r, A_y=A_y, R=R, x_c=x_c, y_c=y_c)
        s -= s_piece

    # left
    b_x = abs(R - x_c)
    b_y = y_c

    B_x_l = 0
    B_x_r = 0
    B_x = B_x_l

    B_y_l = 0
    B_y_r = 1

    if b_x < B_x:
        x_c, y_c = y_c, x_c
        B_x_l, B_y_l = B_y_l, B_x_l
        B_x_r, B_y_r = B_y_r, B_x_r
        s_piece = check_direction(A_x_l=B_x_l, A_x_r=B_x_r, A_y=B_y_l, R=R, x_c=x_c, y_c=y_c)
        s -= s_piece

    # #down
    # b_x = x_c
    # b_y = abs(R - y_c)
    # B_y = 0
    # B_x_l = 0
    # B_x_r = 1
    # if b_y < B_y:
    #     s_piece = check_direction(B_x_l, B_x_r, B_y, R, x_c, y_c)
    #     s -= s_piece
    #
    #
    #
    # # right
    # b_x = x_c + R
    # b_y = y_c
    # B_y = 1
    # B_x_l = 0
    # B_x_r = 1
    # if b_y < B_y:
    #     s_piece = check_direction(B_x_l, B_x_r, B_y, R, x_c, y_c)
    #     s -= s_piece


# N, R = map(int, input().split())
# chips = []
# S = 0
# for _ in range(N):
#     x, y = map(int, input().split())
#     chips.append((x, y))
#     s = checkDot(x, y, R)
#     S += s


