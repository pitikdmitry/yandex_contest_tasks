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

    #up
    a_x = x_c
    a_y = y_c + R
    A_y = 1000
    A_x_l = 0
    A_x_r = 1000

    if a_y > A_y:
        s_piece = check_direction_up_down(A_x_l=A_x_l, A_x_r=A_x_r, A_y=A_y, R=R, x_c=x_c, y_c=y_c)
        s -= s_piece

    #down
    a_x = x_c
    a_y = y_c - R
    A_y = 0
    A_x_l = 0
    A_x_r = 1000

    if a_y < A_y:
        s_piece = check_direction_up_down(A_x_l=A_x_l, A_x_r=A_x_r, A_y=A_y, R=R, x_c=x_c, y_c=y_c)
        s -= s_piece

    #left
    a_x = x_c - R
    a_y = y_c
    A_y_d = 0
    A_y_u = 1000
    A_x = 0

    if a_x < A_x:
        s_piece = check_direction_left_right(A_y_d=A_y_d, A_y_u=A_y_u, A_x=A_x, R=R, x_c=x_c, y_c=y_c)
        s-= s_piece

    #right
    a_x = x_c + R
    a_y = y_c
    A_y_d = 0
    A_y_u = 1000
    A_x = 1000

    if a_x > A_x:
        s_piece = check_direction_left_right(A_y_d=A_y_d, A_y_u=A_y_u, A_x=A_x, R=R, x_c=x_c, y_c=y_c)
        s -= s_piece

    return s


N, R = map(float, input().split())
N = int(N)
R *= 1000
S_cube = 1000 * 1000
S_summ = 0
for _ in range(N):
    x, y = map(lambda x: float(x) * 1000, input().split())
    s = checkDot(x, y, R)
    S_summ += s

print(S_summ / S_cube)
