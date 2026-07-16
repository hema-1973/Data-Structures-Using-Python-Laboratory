class Node:
    def __init__ (self, data):
        self.data = data
        self.next = None
class Stack:
    def __init__(self):
        self.top = None
    def push(self, data):
        newNode = Node(data)
        newNode.next = self.top
        self.top = newNode
        print(data, "added to stack")
    def pop(self):
        if self.top is None:
            print("Stack is Empty")
        else:
            temp = self.top
            self.top = self.top.next
            print(temp.data, "removed from stack")
    def display(self):
        if self.top is None:
            print("Stack is Empty")
        else:
            temp = self.top
            print("\nStack Elements:")
        while temp:
            print(temp.data)
            temp = temp.next
stack = Stack()
while True:
    print("\n-----STACK MENU-----")
    print("1. Push")
    print("2. Pop")
    print("3. Display")
    print("4. Exit")
    choice = int(input("Enter your choice:"))
    if choice == 1:
        item = input("Enter book title: ")
        stack.push(item)
    elif choice == 2:
        stack.pop()
    elif choice == 3:
        stack.display()
    elif choice == 4:
        print("Exiting Program")
        break
    else:
            print("Invalid choice")
