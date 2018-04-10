class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def peek(self):
        return self.items[len(self.items) - 1]

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def size(self):
        return len(self.items)


a = Stack()

print(a.isEmpty())
a.push("Exercise 1")
a.push("Exercise 2")
print(a.peek())
a.push("Exercise 3")
print('i have done', a.size(), 'exercises in data structure')
a.push("Exercise 4")
print(a.pop())
a.push("Exercise 5")
print(a.pop())
print(a.pop())
print(a.pop())
print(a.size())
print(a.isEmpty())
print(a.pop())
print(a.isEmpty())