# Check if a string contains properly nested and balanced parentheses


class Stack:
    def __init__(self):
        self.stack = []

    def size(self):
        return len(self.stack)

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]


def balanced_parens(str):
    """
    Check if a parentheses string is balanced.
    Also return the index of the first offending parenthesis.
    """

    stack = Stack()
    str_len = len(str)

    for i in range(str_len):
        c = str[i]

        if c not in ["(", ")"]:
            raise ValueError("Give me only parentheses!")

        if stack.size() == 0:
            if c == ")":
                return False, i
            stack.push(c)
        elif stack.peek() == "(" and c == ")":
            stack.pop()
        else:
            stack.push(c)

    total_remain = stack.size()
    if total_remain > 0:
        return False, str_len - total_remain
    return True, None


def main():
    test_strs = [
        "((())())()",  # balanced
        ")()(",  # unbalanced
        "())()",  # unbalanced
        "()()((((",  # unbalanced
    ]

    for str in test_strs:
        balanced, wrong_index = balanced_parens(str)
        print(f"{str} - balanced: {balanced} - first wrong: {wrong_index}")


if __name__ == "__main__":
    main()
