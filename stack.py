class MyStack:
    def __init__(self):
        self.stack = []

    def push(self, arg):
        self.stack.append(arg)

    def pop(self):
        if self.size():
            return self.stack.pop()
        return None

    def peek(self):
        if self.size():
            return self.stack[-1]
        return None

    def size(self):
        return len(self.stack)

    def is_empty(self):
        return bool(self.stack)


if __name__ == '__main__':
    MyStack()
    # stack = MyStack()
    # print(stack.stack)
    # print(stack.is_empty())
    # stack.push('letter')
    # stack.push('2')
    # stack.push(6)
    # print(stack.stack)
    # print(stack.pop())
    # print(stack.peek())
    # print(stack.stack)
    # print(stack.is_empty())
    # print(stack.size())
    # print(stack.pop())
    # print(stack.pop())
    # print(stack.is_empty())
    # print(stack.pop())
    # print(stack.peek())
    # print(stack.size())
    # print(stack.peek())
    # print(stack.pop())