class Queue:
    def __init__(self):
        self.items = []

    def dequeue(self):
        self.items.remove(self.items[0])

    def enqueue(self, item):
        self.items.append(item)

    def print(self):
        print(self.items)

    def peek(self):
        print(self.items[len(self.items)-1])


if __name__ == '__main__':
    myLine = Queue()
    myLine.enqueue(20)
    myLine.enqueue(40)
    myLine.enqueue(60)
    myLine.enqueue(80)
    myLine.print()
    myLine.dequeue()
    myLine.peek()
    myLine.print()


