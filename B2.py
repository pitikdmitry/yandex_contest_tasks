import functools


class Node:
    def __init__(self, old_template, new_template):
        self.old_template = old_template
        self.new_template = new_template
        self.left = None
        self.right = None


def parse_number(number: str) -> str:
    new_number = ""
    for c in number:
        if c.isdigit():
            new_number += c
    return new_number


def parse_template(old_template: str) -> tuple:
    new_template = ""
    for c in old_template:
        # if c == "-":
        #     break

        if c.isdigit() or c == "X" or c =="x":
            new_template += c

    return old_template, new_template


def match_template_with_number(template: str, number: str) -> str:
    new_number, num_i = "", 0
    for c in template:

        if c == "X":
            new_number += number[num_i]
            num_i += 1
        else:
            if c.isdigit():
                if int(c) != int(number[num_i]):
                    print("ERROR IN MATCH")

                num_i += 1

            new_number += c

    return new_number


def good_or_not(number, template) -> tuple:
    i, j, go_to_next = 0, 0, False

    if len(number) != len(template):
        return False, go_to_next

    while i < len(number) and j < len(template):
        if number[i] != template[j] and template[j] != "X":
            go_to_next = True

        if number[i] == template[j]:
            i += 1
            j += 1
        elif template[j] == 'X':
            i += 1
            j += 1
        else:
            return False, go_to_next

    return True, go_to_next


def compare(node_1, node_2):
    tem_1 = node_1[0]
    tem_2 = node_2[0]

    if tem_1.isdigit() and tem_2.isdigit():
        if int(tem_1) > int(tem_2):
            return -1
        else:
            return 1

    i, j = 0, 0
    while i < len(tem_1) and j < len(tem_2):
        c_1 = tem_1[i]
        c_2 = tem_2[j]
        if c_1.isdigit() and c_2.isdigit():
            num_1 = int(c_1)
            num_2 = int(c_2)
            if num_1 < num_2:
                return -1
            elif num_1 > num_2:
                return 1
            else:
                i += 1
                j += 1
                if i == len(tem_1):
                    return -1
                elif j == len(tem_2):
                    return 1
                continue
        else:
            if c_1 == "X":
                return 1
            elif c_2 == "X":
                return -1
            else:
                return 1
    return 1


def find_template_bad(number, templates) -> str:
    new_number = number

    j = len(new_number) - 1
    while j > 0 and new_number[j] == "X":
        j -= 1

    while True:
        if new_number in templates:
            node = templates[new_number]
            return node
        else:
            a= new_number[:j]
            b = new_number[j + 1:]
            new_number = new_number[:j] + "X" + new_number[j + 1:]
            j -= 1


N = int(input())
numbers = []
for _ in range(N):
    number = input()
    number = parse_number(number)
    numbers.append(number)

sorted_numbers = sorted(numbers)

M = int(input())
templates_dict = dict()
templates = []

for _ in range(M):
    template = input()
    old_template, new_template = parse_template(template)
    templates.append((new_template, old_template))
    templates_dict[new_template] = old_template

sorted_templates = sorted(templates, key=functools.cmp_to_key(compare))

pairs = {}#number - old temp
previous_i, previous_j = 0, 0
i, j = 0, 0
flag = False
while i < len(sorted_numbers) and j < len(sorted_templates):
    num = sorted_numbers[i]
    new_temp = sorted_templates[j][0]
    res, go_to_next = good_or_not(num, new_temp)
    if go_to_next and not flag:
        flag = True
        previous_j += 1

    if res:
        i += 1
        # print(match_template_with_number(sorted_templates[j][1], num))
        pairs[num] = sorted_templates[j][1]
        j = previous_j
        flag = False
    else:
        j += 1

    if j == len(sorted_templates) - 1 and len(pairs) < len(sorted_numbers):
        j = previous_j
        # old_temp = find_template_bad(num, templates_dict)
        # pairs[num] = old_temp
        # i += 1





for num in numbers:
    old_temp = pairs[num]
    print(match_template_with_number(old_temp, num))
