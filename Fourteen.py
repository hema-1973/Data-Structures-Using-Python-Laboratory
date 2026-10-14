SIZE = 10
hash_table = [None] * SIZE
DELETED = "DELETED"


def insert_student():
    roll = int(input("Enter Roll Number: "))
    name = input("Enter Student Name: ")
    index = roll % SIZE

    for i in range(SIZE):
        pos = (index + i) % SIZE

        if hash_table[pos] is None or hash_table[pos] == DELETED:
            hash_table[pos] = {"roll": roll, "name": name}
            print("Student record inserted successfully")
            return

        if hash_table[pos]["roll"] == roll:
            print("Roll Number already exists")
            return

    print("Hash Table is full")


def search_student():
    roll = int(input("Enter Roll Number to search: "))
    index = roll % SIZE

    for i in range(SIZE):
        pos = (index + i) % SIZE

        if hash_table[pos] is None:
            break

        if hash_table[pos] != DELETED:
            if hash_table[pos]["roll"] == roll:
                print("Student Found:", hash_table[pos])
                return

    print("Student not found")


def delete_student():
    roll = int(input("Enter Roll Number to delete: "))
    index = roll % SIZE

    for i in range(SIZE):
        pos = (index + i) % SIZE

        if hash_table[pos] is None:
            break

        if hash_table[pos] != DELETED:
            if hash_table[pos]["roll"] == roll:
                hash_table[pos] = DELETED
                print("Student record deleted successfully")
                return

    print("Student not found")


def display_table():
    print("\nIndex\tRoll Number\tName")

    for i in range(SIZE):
        if hash_table[i] is None:
            print(i, "\tEmpty")
        elif hash_table[i] == DELETED:
            print(i, "\tDeleted")
        else:
            print(i, "\t", hash_table[i]["roll"],
                  "\t\t", hash_table[i]["name"])


while True:
    print("\n--- Student Registration System ---")
    print("1. Insert Student")
    print("2. Search Student")
    print("3. Delete Student")
    print("4. Display Hash Table")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        insert_student()
    elif choice == 2:
        search_student()
    elif choice == 3:
        delete_student()
    elif choice == 4:
        display_table()
    elif choice == 5:
        print("Program terminated")
        break
    else:
        print("Invalid choice")
