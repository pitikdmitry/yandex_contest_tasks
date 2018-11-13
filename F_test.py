import unittest
from F import check_direction_up_down, check_direction_left_right


class TestF(unittest.TestCase):

    def test_up_middle(self):
        x_c, y_c, R = 5, 9, 2

        a_x = x_c
        a_y = y_c + R
        A_y = 10
        A_x_l = 0
        A_x_r = 10

        if a_y > A_y:
            s_piece = check_direction_up_down(A_x_l=A_x_l, A_x_r=A_x_r, A_y=A_y, R=R, x_c=x_c, y_c=y_c)
            print("test_up_middle: ", end=" ")
            print(s_piece)
            self.assertAlmostEqual(s_piece, 2.4567393972175116, places=9)

    def test_up_left(self):
        x_c, y_c, R = 1, 9, 2

        a_x = x_c
        a_y = y_c + R
        A_y = 10
        A_x_l = 0
        A_x_r = 10

        if a_y > A_y:
            s_piece = check_direction_up_down(A_x_l=A_x_l, A_x_r=A_x_r, A_y=A_y, R=R, x_c=x_c, y_c=y_c)
            print("test_up_left: ", end=" ")
            print(s_piece)
            self.assertAlmostEqual(s_piece, 2.299166025403653, places=9)

    def test_up_right(self):
        x_c, y_c, R = 9, 9, 2

        a_x = x_c
        a_y = y_c + R
        A_y = 10
        A_x_l = 0
        A_x_r = 10

        if a_y > A_y:
            s_piece = check_direction_up_down(A_x_l=A_x_l, A_x_r=A_x_r, A_y=A_y, R=R, x_c=x_c, y_c=y_c)
            print("test_up_right: ", end=" ")
            print(s_piece)
            self.assertAlmostEqual(s_piece, 2.299166025403653, places=9)

    def test_down_middle(self):
        x_c, y_c, R = 5, 1, 2

        a_x = x_c
        a_y = y_c - R
        A_y = 0
        A_x_l = 0
        A_x_r = 10

        if a_y < A_y:
            s_piece = check_direction_up_down(A_x_l=A_x_l, A_x_r=A_x_r, A_y=A_y, R=R, x_c=x_c, y_c=y_c)
            print("test_down_middle: ", end=" ")
            print(s_piece)
            self.assertAlmostEqual(s_piece, 2.4567393972175116, places=9)

    def test_down_left(self):
        x_c, y_c, R = 1, 1, 2

        a_x = x_c
        a_y = y_c - R
        A_y = 0
        A_x_l = 0
        A_x_r = 10

        if a_y < A_y:
            s_piece = check_direction_up_down(A_x_l=A_x_l, A_x_r=A_x_r, A_y=A_y, R=R, x_c=x_c, y_c=y_c)
            print("test_down_left: ", end=" ")
            print(s_piece)
            self.assertAlmostEqual(s_piece, 2.299166025403653, places=9)

    def test_down_right(self):
        x_c, y_c, R = 9, 1, 2

        a_x = x_c
        a_y = y_c - R
        A_y = 0
        A_x_l = 0
        A_x_r = 10

        if a_y < A_y:
            s_piece = check_direction_up_down(A_x_l=A_x_l, A_x_r=A_x_r, A_y=A_y, R=R, x_c=x_c, y_c=y_c)
            print("test_down_right: ", end=" ")
            print(s_piece)
            self.assertAlmostEqual(s_piece, 2.299166025403653, places=9)

    def test_left_middle(self):
        x_c, y_c, R = 1, 5, 2

        a_x = x_c - R
        a_y = y_c
        A_y_d = 0
        A_y_u = 10
        A_x = 0

        if a_x < A_x:
            s_piece = check_direction_left_right(A_y_d=A_y_d, A_y_u=A_y_u, A_x=A_x, R=R, x_c=x_c, y_c=y_c)
            print("test_left_middle: ", end=" ")
            print(s_piece)
            self.assertAlmostEqual(s_piece, 2.4567393972175116, places=9)

    def test_left_up(self):
        x_c, y_c, R = 1, 9, 2

        a_x = x_c - R
        a_y = y_c
        A_y_d = 0
        A_y_u = 10
        A_x = 0

        if a_x < A_x:
            s_piece = check_direction_left_right(A_y_d=A_y_d, A_y_u=A_y_u, A_x=A_x, R=R, x_c=x_c, y_c=y_c)
            print("test_left_middle: ", end=" ")
            print(s_piece)
            self.assertAlmostEqual(s_piece, 2.299166025403653, places=9)

    def test_left_down(self):
        x_c, y_c, R = 1, 1, 2

        a_x = x_c - R
        a_y = y_c
        A_y_d = 0
        A_y_u = 10
        A_x = 0

        if a_x < A_x:
            s_piece = check_direction_left_right(A_y_d=A_y_d, A_y_u=A_y_u, A_x=A_x, R=R, x_c=x_c, y_c=y_c)
            print("test_left_middle: ", end=" ")
            print(s_piece)
            self.assertAlmostEqual(s_piece, 2.299166025403653, places=9)

    def test_right_middle(self):
        x_c, y_c, R = 9, 5, 2

        a_x = x_c + R
        a_y = y_c
        A_y_d = 0
        A_y_u = 10
        A_x = 10

        if a_x > A_x:
            s_piece = check_direction_left_right(A_y_d=A_y_d, A_y_u=A_y_u, A_x=A_x, R=R, x_c=x_c, y_c=y_c)
            print("test_left_middle: ", end=" ")
            print(s_piece)
            self.assertAlmostEqual(s_piece, 2.4567393972175116, places=9)

    def test_right_up(self):
        x_c, y_c, R = 9, 9, 2

        a_x = x_c + R
        a_y = y_c
        A_y_d = 0
        A_y_u = 10
        A_x = 10

        if a_x > A_x:
            s_piece = check_direction_left_right(A_y_d=A_y_d, A_y_u=A_y_u, A_x=A_x, R=R, x_c=x_c, y_c=y_c)
            print("test_left_middle: ", end=" ")
            print(s_piece)
            self.assertAlmostEqual(s_piece, 2.299166025403653, places=9)

    def test_right_down(self):
        x_c, y_c, R = 9, 1, 2

        a_x = x_c + R
        a_y = y_c
        A_y_d = 0
        A_y_u = 10
        A_x = 10

        if a_x > A_x:
            s_piece = check_direction_left_right(A_y_d=A_y_d, A_y_u=A_y_u, A_x=A_x, R=R, x_c=x_c, y_c=y_c)
            print("test_left_middle: ", end=" ")
            print(s_piece)
            self.assertAlmostEqual(s_piece, 2.299166025403653, places=9)

if __name__ == '__main__':
    unittest.main()