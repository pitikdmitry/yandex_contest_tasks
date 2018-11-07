def check_distance(dot, center, r) -> bool:
    if abs(dot[0] ** 2 - center[0] ** 2) + abs(dot[1] ** 2 - dot[1] ** 2) <= r ** 2:
        return True

    return False


def count_in_circle(chips, center, r) -> int:
    counter = 0

    for dot in chips:

        if check_distance(dot, center, r):
            counter += 1

    return counter


N, R = map(int, input().split())
chips = []
for _ in range(N):
    x, y = map(int, input().split())
    chips.append((x, y))

