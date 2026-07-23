queue = []
MAX = 5
def enqueue():
    if len(queue) >= MAX:
        print("Queue Overflow! Parking is Full.")
    else:
        car = input("Enter car number: ")
        queue.append(car)
        print(car, "entered the Parking")

def dequeue():
    if len(queue) == 0:
        print("Queue Underflow! Parking is Empty.")
    else:
        removed_car = queue.pop(0)
        print(removed_car, "left the Parking.")

def display():
    if len(queue) == 0:
        print("Parking is Empty.")
    else:
        print("\nCars in Parking.")
        for car in queue:
            print(car)

while True:
    print("\n------ CAR PARKING QUEUE MENU -----")
    print("1. Enqueue car")
    print("2. Dequeue Car")
    print("3. Display Car")
    print("4. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 1:
        enqueue()
    elif choice == 2:
        dequeue()
    elif choice == 3:
        display()
    elif choice == 4:
        print("Exiting Program...")
        break
else:
    print("Invalid choice")
    
