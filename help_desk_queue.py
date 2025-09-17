# Import the Node class you created in node.py
from node import Node

# using action as value
# Implement your Queue class here
class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, action): #add values
        new_node = Node(action)
        if not self.front:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if not self.front:
            return None
        removed_node = self.front
        self.front = self.front.next # if this was last node then rear should also be updated
        if not self.front:
            self.rear = None
        return removed_node.action

    def peek(self):
        if self.front:
            return self.front.action
        else:
            print("Queue is empty")
            return None
        
    def print_que(self):
        current = self.front
        if not current:
            print("Queue is empty")
            return
        while current:
            print(f"- {current.action}")
            current = current.next # update current to next value



def run_help_desk():
    # Create an instance of the Queue class
    queue = Queue()

    while True:
        print("\n--- Help Desk Ticketing System ---")
        print("1. Add customer")
        print("2. Help next customer")
        print("3. View next customer")
        print("4. View all waiting customers")
        print("5. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            name = input("Enter customer name: ")
            # Add the customer to the queue
            queue.enqueue(name)
            print(f"{name} added to the queue.")

        elif choice == "2":
            # Help the next customer in the queue and return message that they were helped
            customer = queue.dequeue()
            print(f"{customer} has been helped!")

        elif choice == "3":
            # Peek at the next customer in the queue and return their name
            customer = queue.peek()
            print(f"Next customer: {customer}")

        elif choice == "4":
            # Print all customers in the queue
            print("\nWaiting customers:")
            queue.print_que()

        elif choice == "5":
            print("Exiting Help Desk System.")
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    run_help_desk()