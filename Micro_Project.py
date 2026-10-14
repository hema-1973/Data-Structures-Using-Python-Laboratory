class QuestionNode:
    def __init__(self, question_id, text, options, answer, section):
        self.question_id = question_id
        self.text = text
        self.options = options
        self.answer = answer
        self.selected_option = None
        self.marked_for_review = False
        self.section = section
        self.prev = None
        self.next = None


class ExamQuestionNavigator:
    def __init__(self):
        self.head = None
        self.tail = None
        self.current = None

    def add_question(self, question_id, text, options, answer, section):
        new_node = QuestionNode(question_id, text, options, answer, section)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

        if self.current is None:
            self.current = self.head

        print(f"Question {question_id} added to section {section}")

    def show_current(self):
        if self.current is None:
            print("No questions loaded yet")
            return

        node = self.current
        print(f"\n[{node.section}] Q{node.question_id}: {node.text}")

        for i, opt in enumerate(node.options, start=1):
            print(f" {i}. {opt}")

        if node.selected_option:
            print(f" Your answer: {node.selected_option}")

        if node.marked_for_review:
            print(" Marked for review")

    def answer_current(self, option):
        if self.current is None:
            print("No question loaded")
            return

        self.current.selected_option = option
        print(f"[Answered] Q{self.current.question_id}: {option}")

    def next_question(self):
        if self.current and self.current.next:
            self.current = self.current.next
            self.show_current()
        else:
            print("This is the last question")

    def previous_question(self):
        if self.current and self.current.prev:
            self.current = self.current.prev
            self.show_current()
        else:
            print("This is the first question")

    def mark_current_for_review(self):
        if self.current is None:
            print("No question loaded")
            return

        self.current.marked_for_review = True
        print(f"[Marked for review] Q{self.current.question_id}")

    def go_to_next_marked(self):
        if self.current is None:
            print("No question loaded")
            return

        node = self.current.next

        while node:
            if node.marked_for_review:
                self.current = node
                self.show_current()
                return

            node = node.next

        print("No more marked questions ahead")

    def jump_to_question(self, question_id):
        node = self.head

        while node:
            if node.question_id == question_id:
                self.current = node
                self.show_current()
                return

            node = node.next

        print(f"Question {question_id} not found")

    def auto_submit_section(self, section_name):
        node = self.head
        found = False

        print(f"\n[Submitting section: {section_name}]")

        while node:
            if node.section == section_name:
                found = True
                status = (
                    node.selected_option
                    if node.selected_option
                    else "Not answered"
                )
                print(f" Q{node.question_id}: {status}")

            node = node.next

        if not found:
            print(f"No questions found in section {section_name}")


def get_new_question_id(navigator):
    if navigator.head is None:
        return 1

    return navigator.tail.question_id + 1


def add_question_flow(navigator):
    text = input("Enter question text: ")
    section = input("Enter section name (e.g. Math, Science): ")
    option_count = int(input("How many options? "))

    options = []

    for i in range(option_count):
        opt = input(f" Option {i + 1}: ")
        options.append(opt)

    answer = input("Enter correct answer (must match one option exactly): ")
    question_id = get_new_question_id(navigator)

    navigator.add_question(question_id, text, options, answer, section)


def run_menu():
    navigator = ExamQuestionNavigator()

    menu = """
--- Online Exam Question Navigator ---

1. Add a question
2. Show current question
3. Answer current question
4. Next question
5. Previous question
6. Mark current question for review
7. Go to next marked question
8. Jump to a question by ID
9. Submit a section
10. Exit
"""

    while True:
        print(menu)
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_question_flow(navigator)

        elif choice == "2":
            navigator.show_current()

        elif choice == "3":
            option = input("Enter your answer: ")
            navigator.answer_current(option)

        elif choice == "4":
            navigator.next_question()

        elif choice == "5":
            navigator.previous_question()

        elif choice == "6":
            navigator.mark_current_for_review()

        elif choice == "7":
            navigator.go_to_next_marked()

        elif choice == "8":
            q_id = int(input("Enter question ID: "))
            navigator.jump_to_question(q_id)

        elif choice == "9":
            section = input("Enter section name to submit: ")
            navigator.auto_submit_section(section)

        elif choice == "10":
            print("Exiting exam navigator")
            break

        else:
            print("Invalid choice, try again")


if __name__ == "__main__":
    run_menu()
