import unittest
from F import check_direction


class TestF(unittest.TestCase):

    def test_up_middle(self):
        x_c, y_c, R = 5, 9, 2

        a_x = x_c
        a_y = y_c + R
        A_y = 10
        A_x_l = 0
        A_x_r = 10

        if a_y > A_y:
            s_piece = check_direction(A_x_l=A_x_l, A_x_r=A_x_r, A_y=A_y, R=R, x_c=x_c, y_c=y_c)
            print(s_piece)

    def test_up_left(self):
        x_c, y_c, R = 1, 9, 2

        a_x = x_c
        a_y = y_c + R
        A_y = 10
        A_x_l = 0
        A_x_r = 10

        if a_y > A_y:
            s_piece = check_direction(A_x_l=A_x_l, A_x_r=A_x_r, A_y=A_y, R=R, x_c=x_c, y_c=y_c)
            print(s_piece)

if __name__ == '__main__':
    unittest.main()