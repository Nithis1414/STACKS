class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.top = None

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            print("Underflow")
        else:
            self.top = self.top.next

    def peek(self):
        if self.top is None:
            print("Stack is empty.")
        else:
            print(self.top.data)

obj = Stack()

while True:
    print("1. Push, 2. Pop, 3. Peek, 4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        data = int(input("Enter a number: "))
        obj.push(data)
    elif choice == 2:
        obj.pop()
    elif choice == 3:
        obj.peek()
    elif choice == 4:
        break
