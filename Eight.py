class Node:
    def __init__(self, visitor, time, purpose):
        self.visitor = visitor
        self.time = time
        self.purpose = purpose
        self.left = None
        self.right = None

def insert(root, visitor, time, purpose):
    if root is None:
        return Node(visitor, time, purpose)

    if visitor < root.visitor:
        root.left = insert(root.left, visitor, time, purpose)

    elif visitor > root.visitor:
        root.right = insert(root.right, visitor, time, purpose)

    else:
        print("Visitor already exists")

    return root

def search(root, visitor):
    if root is None:
        return None

    if visitor == root.visitor:
        return root

    if visitor < root.visitor:
        return search(root.left, visitor)

    else:
        return search(root.right, visitor)

def find_min(root):
    while root.left:
        root = root.left

    return root


def delete(root, visitor):
    if root is None:
        return None

    if visitor < root.visitor:
        root.left = delete(root.left, visitor)

    elif visitor > root.visitor:
        root.right = delete(root.right, visitor)

    else:
    
        if root.left is None:
            return root.right
        if root.right is None:
            return root.left

        temp = find_min(root.right)

        root.visitor = temp.visitor
        root.time = temp.time
        root.purpose = temp.purpose

        root.right = delete(root.right, temp.visitor)

    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.visitor, "|", root.time, "|", root.purpose)
        inorder(root.right)


def preorder(root):
    if root:
        print(root.visitor, "|", root.time, "|", root.purpose)
        preorder(root.left)
        preorder(root.right)

def postorder(root):
    if root:
        postorder(root.left)
        postorder(root.right)
        print(root.visitor, "|", root.time, "|", root.purpose)

def count_nodes(root):
    if root is None:
        return 0

    return 1 + count_nodes(root.left) + count_nodes(root.right)


root = None

while True:

    print("\n--- LOG BOOK MENU ---")
    print("1. Insert a Log Entry")
    print("2. Delete a Log Entry")
    print("3. Search for a Log Entry")
    print("4. Inorder Traversal")
    print("5. Preorder Traversal")
    print("6. Postorder Traversal")
    print("7. Count Total Entries")
    print("8. Exit")

    choice = int(input("Enter your choice: "))

    # Insert
    if choice == 1:

        visitor = input("Enter Visitor Name: ")
        time = input("Enter Entry Time: ")
        purpose = input("Enter Purpose: ")

        root = insert(root, visitor, time, purpose)

        print("Log entry inserted successfully.")

    elif choice == 2:

        visitor = input("Enter Visitor Name to delete: ")

        if search(root, visitor):
            root = delete(root, visitor)
            print("Log entry deleted successfully.")

        else:
            print("Visitor not found.")

    elif choice == 3:

        visitor = input("Enter Visitor Name to search: ")

        result = search(root, visitor)

        if result:
            print("\nVisitor Found")
            print("Name   :", result.visitor)
            print("Time   :", result.time)
            print("Purpose:", result.purpose)

        else:
            print("Visitor not found.")

    elif choice == 4:

        print("\nLog Entries in Inorder:")
        inorder(root)

    elif choice == 5:

        print("\nLog Entries in Preorder:")
        preorder(root)

    elif choice == 6:

        print("\nLog Entries in Postorder:")
        postorder(root)

    elif choice == 7:

        print("Total Entries:", count_nodes(root))

    elif choice == 8:

        print("Program terminated.")
        break
    else:

        print("Invalid choice.")
