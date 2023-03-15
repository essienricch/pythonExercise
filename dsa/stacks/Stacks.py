class stacks:
    def __int__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        self.items.pop(len(self.items)-1)

    def peek(self):
        return len(self.items - 1)

    def size(self):
        return len(self.items)

    def isEmpty(self):
        if not self.items:
            print(True)
        else:
            print(False)

    def print_stack(self):
        print(self.items)


if __name__ == '__main__':
    fresh_stack = stacks()
    fresh_stack.__int__()
    fresh_stack.push(10)
    fresh_stack.push(45)
    fresh_stack.push(20)
    fresh_stack.print_stack()

