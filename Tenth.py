class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, job, priority):
        self.heap.append([priority, job])
        i = len(self.heap) - 1

        while i > 0:
            parent = (i - 1) // 2

            if self.heap[i][0] > self.heap[parent][0]:
                temp = self.heap[i]
                self.heap[i] = self.heap[parent]
                self.heap[parent] = temp

                i = parent
            else:
                break

    def delete_max(self):
        if len(self.heap) == 0:
            print("Heap is Empty!")
            return

        highest = self.heap[0]
        last = self.heap.pop()

        if self.heap:
            self.heap[0] = last
            self.heapify(0)

        print("Deleted Job :", highest[1])
        print("Priority :", highest[0])

    def heapify(self, i):
        n = len(self.heap)

        while True:
            left = 2 * i + 1
            right = 2 * i + 2
            largest = i

            if left < n and self.heap[left][0] > self.heap[largest][0]:
                largest = left

            if right < n and self.heap[right][0] > self.heap[largest][0]:
                largest = right

            if largest == i:
                break

            self.heap[i], self.heap[largest] = \
                self.heap[largest], self.heap[i]

            i = largest

    def peek(self):
        if self.heap:
            print("Highest Priority Job :", self.heap[0][1])
            print("Priority :", self.heap[0][0])
        else:
            print("Heap is Empty!")

    def display(self):
        if not self.heap:
            print("Heap is Empty!")
            return

        print("\nJobs in Heap:")
        for priority, job in self.heap:
            print("Job:", job, " Priority:", priority)

def switch(choice, heap):

    if choice == 1:
        job = input("Enter Job Name: ")
        priority = int(input("Enter Priority: "))
        heap.insert(job, priority)
        print("Job Inserted Successfully!")

    elif choice == 2:
        heap.delete_max()

    elif choice == 3:
        heap.peek()

    elif choice == 4:
        heap.display()

    elif choice == 5:
        print("Program Ended!")
        return False

    else:
        print("Invalid Choice!")

    return True

h = MaxHeap()

while True:

    print("\n===== MAX HEAP JOB SCHEDULER =====")
    print("1. Insert Job")
    print("2. Delete Highest Priority Job")
    print("3. Peek Highest Priority Job")
    print("4. Display All Jobs")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if not switch(choice, h):
        break
