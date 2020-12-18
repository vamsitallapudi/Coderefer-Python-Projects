class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)


if __name__ == "__main__":
    s = Stack()
    print(s.isEmpty())
    s.push(5)
    s.push("Vamsi")
    s.push(True)
    print(s.peek())
    s.pop()
    print(s.peek())
    s.pop()
    print(s.peek())
    print("size is " + str(s.size()))
