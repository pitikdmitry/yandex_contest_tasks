"""
Bob has square (0,0), (0,1), (1,0), (1,1).
There are N small chips in this square with random coordinates.
Bob chooses one random point and counts amount of chips,
 distance to which is smaller than R
"""


from math import pi, sqrt, asin, sin, acos


def check_dir_up_down(left_line, right_line, y_line, r, c_x, c_y):
    x_r_cross = c_x + sqrt(r ** 2 - (y_line - c_y) ** 2)
    x_l_cross = c_x - sqrt(r ** 2 - (y_line - c_y) ** 2)
    h_triangle = abs(y_line - c_y)

    s_sector = 0
    if x_l_cross >= left_line and x_r_cross <= right_line:  # without pieces
        hord = x_r_cross - x_l_cross
        alpha = 2 * asin(hord / (2 * r))
        s_sector = r ** 2 * (alpha - sin(alpha)) / 2
    elif x_l_cross < left_line < x_r_cross <= right_line:  # with left piece, delete small part of piece
        osn_triangle = abs(x_r_cross - left_line)
        s_triangle = osn_triangle * h_triangle / 2
        from_c_to_left_corner = sqrt((c_x - left_line) ** 2 + (c_y - y_line) ** 2)
        alpha = acos((from_c_to_left_corner ** 2 + r ** 2 - osn_triangle ** 2) / (2 * from_c_to_left_corner * r))
        s_sector = ((r ** 2) * alpha / 2) - s_triangle
    elif left_line <= x_l_cross < right_line < x_r_cross:
        osn_triangle = abs(right_line - x_l_cross)
        s_triangle = osn_triangle * h_triangle / 2
        from_c_to_right_corner = sqrt((c_x - right_line) ** 2 + (c_y - y_line) ** 2)
        alpha = acos((from_c_to_right_corner ** 2 + r ** 2 - osn_triangle ** 2) / (2 * from_c_to_right_corner * r))
        s_sector = (r ** 2 * alpha / 2) - s_triangle
    elif x_l_cross < left_line and x_r_cross > right_line:
        osn_triangle = right_line - left_line
        s_triangle = osn_triangle * h_triangle / 2
        from_c_to_left_corner = sqrt((c_x - left_line) ** 2 + (c_y - y_line) ** 2)
        from_c_to_right_corner = sqrt((c_x - right_line) ** 2 + (c_y - y_line) ** 2)
        alpha = acos((from_c_to_right_corner ** 2 + from_c_to_left_corner ** 2 - osn_triangle ** 2)
                     / (2 * from_c_to_right_corner * from_c_to_left_corner))
        s_sector = (r ** 2 * alpha / 2) - s_triangle

    return s_sector


def check_dir_left_right(down_line, up_line, x_line, r, c_x, c_y):
    y_d_cross = c_y - sqrt(r ** 2 - (x_line - c_x) ** 2)
    y_u_cross = c_y + sqrt(r ** 2 - (x_line - c_x) ** 2)
    h_triangle = abs(x_line - c_x)

    s_sector = 0
    if y_d_cross >= down_line and y_u_cross <= up_line:  # without pieces
        hord = y_u_cross - y_d_cross
        alpha = 2 * asin(hord / (2 * r))
        s_sector = r ** 2 * (alpha - sin(alpha)) / 2
    elif y_d_cross < down_line < y_u_cross <= up_line:  # with left piece, delete small part of piece
        osn_triangle = abs(y_u_cross - down_line)
        s_triangle = osn_triangle * h_triangle / 2
        from_c_to_down_corner = sqrt((c_x - x_line) ** 2 + (c_y - down_line) ** 2)
        alpha = acos((from_c_to_down_corner ** 2 + r ** 2 - osn_triangle ** 2) / (2 * from_c_to_down_corner * r))
        s_sector = ((r ** 2) * alpha / 2) - s_triangle
    elif down_line <= y_d_cross < up_line < y_u_cross:
        osn_triangle = abs(up_line - y_d_cross)
        s_triangle = osn_triangle * h_triangle / 2
        from_c_to_up_corner = sqrt((c_x - x_line) ** 2 + (c_y - up_line) ** 2)
        alpha = acos((from_c_to_up_corner ** 2 + r ** 2 - osn_triangle ** 2) / (2 * from_c_to_up_corner * r))
        s_sector = (r ** 2 * alpha / 2) - s_triangle
    elif y_d_cross < down_line and y_u_cross > up_line:
        osn_triangle = up_line - down_line
        s_triangle = osn_triangle * h_triangle / 2
        from_c_to_down_corner = sqrt((c_x - x_line) ** 2 + (c_y - down_line) ** 2)
        from_c_to_up_corner = sqrt((c_x - x_line) ** 2 + (c_y - up_line) ** 2)
        alpha = acos((from_c_to_up_corner ** 2 + from_c_to_down_corner ** 2 - osn_triangle ** 2)
                     / (2 * from_c_to_up_corner * from_c_to_down_corner))
        s_sector = (r ** 2 * alpha / 2) - s_triangle

    return s_sector


def cut_sector(c_x, c_y, r):
    s = pi * r ** 2

    a_x = c_x
    a_y = c_y + r
    left_line = 0
    right_line = 1
    y_line = 1

    if a_y > y_line:
        s -= check_dir_up_down(left_line=left_line, right_line=right_line, y_line=y_line, r=r, c_x=c_x, c_y=c_y)

    a_y = c_y - r
    y_line = 0

    if a_y < y_line:
        s -= check_dir_up_down(left_line=left_line, right_line=right_line, y_line=y_line, r=r, c_x=c_x, c_y=c_y)

    #left
    a_x = c_x - r
    up_line = 1
    a_y = c_y
    down_line = 0
    A_x = 0

    if a_x < A_x:
        s -= check_dir_left_right(down_line=down_line, up_line=up_line, x_line=A_x, r=r, c_x=c_x, c_y=c_y)

    #right
    a_x = c_x + r
    A_x = 1

    if a_x > A_x:
        s -= check_dir_left_right(down_line=down_line, up_line=up_line, x_line=A_x, r=r, c_x=c_x, c_y=c_y)

    return s


n, r = input().split()
r = float(r)
n = int(n)

all_s = 1
s = 0
for i in range(n):
    x, y = map(float, input().split())
    s += cut_sector(x, y, r)

print(s / all_s)
