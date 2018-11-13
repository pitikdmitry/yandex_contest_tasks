def compare_template(tem_1: str, tem_2: str):
    if tem_1.isdigit() and tem_2.isdigit():
        if int(tem_1) > int(tem_2):
            return True
        else:
            return False

    i, j = 0, 0
    while i < len(tem_1) and j < len(tem_2):
        c_1 = tem_1[i]
        c_2 = tem_2[j]
        if c_1.isdigit() and c_2.isdigit():
            num_1 = int(c_1)
            num_2 = int(c_2)
            if num_1 > num_2:
                return True
            elif num_1 < num_2:
                return False
            else:
                i += 1
                j += 1
                if i == len(tem_1):
                    return False
                elif j == len(tem_2):
                    return True
                continue
        else:
            if c_1 == "X":
                return True
            elif c_2 == "X":
                return False
            else:
                return False


class Node:
    def __init__(self, old_template, new_template):
        self.old_template = old_template
        self.new_template = new_template
        self.left = None
        self.right = None


class Tree:
    def __init__(self):
        self.root = None

    def add(self, node: Node):
        if self.root is None:
            self.root = node
            return

        cur_node = self.root
        while True:
            if not compare_template(node.new_template, cur_node.new_template):
                if cur_node.left is None:
                    cur_node.left = node
                    break
                else:
                    cur_node = cur_node.left
            else:
                if cur_node.right is None:
                    cur_node.right = node
                    break
                else:
                    cur_node = cur_node.right

    def find_template(self, node: Node, number: str) -> Node:
        new_template = node.new_template
        i, j = 0, 0
        while i < len(new_template) and j < len(number):
            c_1 = new_template[i]
            c_2 = number[j]
            if c_1.isdigit() and c_2.isdigit():
                num_1 = int(c_1)
                num_2 = int(c_2)

                if num_1 == num_2:
                    i += 1
                    j += 1
                    continue
                elif num_2 < num_1:
                    if node.left is not None:
                        return self.find_template(node.left, number)
                    else:
                        print("NODE LEFT IS NONE")
                else:
                    if node.right is not None:
                        return self.find_template(node.right, number)
                    else:
                        print("NODE RIGHT IS NONE")
            else:
                if c_1 == "X":
                    if len(new_template) != len(number):
                        if node.right is not None:
                            return self.find_template(node.right, number)
                        else:
                            print("NODE RIGHT IS NONE")
                    return node

        return node


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


N = int(input())
numbers = []
for _ in range(N):
    number = input()
    number = parse_number(number)
    numbers.append(number)


M = int(input())
tree = Tree()
for _ in range(M):
    template = input()
    old_template, new_template = parse_template(template)
    node = Node(old_template, new_template)
    tree.add(node)

for number in numbers:
    node = tree.find_template(tree.root, number)
    print(match_template_with_number(node.old_template, number))
