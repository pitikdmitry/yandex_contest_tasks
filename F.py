from math import pi, sqrt, asin, sin, acos


def check_direction_up_down(A_x_l, A_x_r, A_y, R, x_c, y_c):
    x_r_cross = x_c + sqrt(R ** 2 - (A_y - y_c) ** 2)
    x_l_cross = x_c - sqrt(R ** 2 - (A_y - y_c) ** 2)
    h_triangle = abs(A_y - y_c)

    s_piece = 0
    if x_l_cross >= A_x_l and x_r_cross <= A_x_r:  # without pieces
        hord = x_r_cross - x_l_cross
        alpha = 2 * asin(hord / (2 * R))
        s_piece = R ** 2 * (alpha - sin(alpha)) / 2
    elif x_l_cross < A_x_l and x_r_cross <= A_x_r and x_r_cross > A_x_l:  # with left piece, delete small part of piece
        osn_triangle = abs(x_r_cross - A_x_l)
        s_triangle = osn_triangle * h_triangle / 2
        from_c_to_left_corner = sqrt((x_c - A_x_l) ** 2 + (y_c - A_y) ** 2)
        alpha = acos((from_c_to_left_corner ** 2 + R ** 2 - osn_triangle ** 2) / (2 * from_c_to_left_corner * R))
        s_piece = ((R ** 2) * alpha / 2) - s_triangle
    elif x_l_cross >= A_x_l and x_l_cross < A_x_r and x_r_cross > A_x_r:
        osn_triangle = abs(A_x_r - x_l_cross)
        s_triangle = osn_triangle * h_triangle / 2
        from_c_to_right_corner = sqrt((x_c - A_x_r) ** 2 + (y_c - A_y) ** 2)
        alpha = acos((from_c_to_right_corner ** 2 + R ** 2 - osn_triangle ** 2) / (2 * from_c_to_right_corner * R))
        s_piece = (R ** 2 * alpha / 2) - s_triangle
    elif x_l_cross < A_x_l and x_r_cross > A_x_r:
        osn_triangle = A_x_r - A_x_l
        s_triangle = osn_triangle * h_triangle / 2
        from_c_to_left_corner = sqrt((x_c - A_x_l) ** 2 + (y_c - A_y) ** 2)
        from_c_to_right_corner = sqrt((x_c - A_x_r) ** 2 + (y_c - A_y) ** 2)
        alpha = acos((from_c_to_right_corner ** 2 + from_c_to_left_corner ** 2 - osn_triangle ** 2) / (2 * from_c_to_right_corner * from_c_to_left_corner))
        s_piece = (R ** 2 * alpha / 2) - s_triangle
    else:
        print("smth wrong")
    return s_piece


def check_direction_left_right(A_y_d, A_y_u, A_x, R, x_c, y_c):
    y_d_cross = y_c - sqrt(R ** 2 - (A_x - x_c) ** 2)
    y_u_cross = y_c + sqrt(R ** 2 - (A_x - x_c) ** 2)
    h_triangle = abs(A_x - x_c)

    s_piece = 0
    if y_d_cross >= A_y_d and y_u_cross <= A_y_u:  # without pieces
        hord = y_u_cross - y_d_cross
        alpha = 2 * asin(hord / (2 * R))
        s_piece = R ** 2 * (alpha - sin(alpha)) / 2
    elif y_d_cross < A_y_d and y_u_cross <= A_y_u and y_u_cross > A_y_d:  # with left piece, delete small part of piece
        osn_triangle = abs(y_u_cross - A_y_d)
        s_triangle = osn_triangle * h_triangle / 2
        from_c_to_down_corner = sqrt((x_c - A_x) ** 2 + (y_c - A_y_d) ** 2)
        alpha = acos((from_c_to_down_corner ** 2 + R ** 2 - osn_triangle ** 2) / (2 * from_c_to_down_corner * R))
        s_piece = ((R ** 2) * alpha / 2) - s_triangle
    elif y_d_cross >= A_y_d and y_d_cross < A_y_u and y_u_cross > A_y_u:
        osn_triangle = abs(A_y_u - y_d_cross)
        s_triangle = osn_triangle * h_triangle / 2
        from_c_to_up_corner = sqrt((x_c - A_x) ** 2 + (y_c - A_y_u) ** 2)
        alpha = acos((from_c_to_up_corner ** 2 + R ** 2 - osn_triangle ** 2) / (2 * from_c_to_up_corner * R))
        s_piece = (R ** 2 * alpha / 2) - s_triangle
    elif y_d_cross < A_y_d and y_u_cross > A_y_u:
        osn_triangle = A_y_u - A_y_d
        s_triangle = osn_triangle * h_triangle / 2
        from_c_to_down_corner = sqrt((x_c - A_x) ** 2 + (y_c - A_y_d) ** 2)
        from_c_to_up_corner = sqrt((x_c - A_x) ** 2 + (y_c - A_y_u) ** 2)
        alpha = acos((from_c_to_up_corner ** 2 + from_c_to_down_corner ** 2 - osn_triangle ** 2) / (2 * from_c_to_up_corner * from_c_to_down_corner))
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
        s_piece = check_direction_up_down(A_x_l=A_x_l, A_x_r=A_x_r, A_y=A_y, R=R, x_c=x_c, y_c=y_c)
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
        s_piece = check_direction_up_down(A_x_l=B_x_l, A_x_r=B_x_r, A_y=B_y_l, R=R, x_c=x_c, y_c=y_c)
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


