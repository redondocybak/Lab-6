#3ARCLAB6

# Define the Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Create individual nodes
node1 = Node(10)
node2 = Node(20)
node3 = Node(30)

# Link the nodes
node1.next = node2
node2.next = node3

def print_linked_list(head):
    current = head
    while current:
        print(current.data, end=" - ")
        current = current.next
    print("No more nodes")

#print function
print_linked_list(node1)

#Exercise 1
node2.data = 75
print_linked_list(node1)

#Exercise 2
node4 = Node(40)
node3.next = node4
print_linked_list(node1)

#Exercise 3
def print_linked_list_with_count(head):
    current = head
    count = 0
    while current:
        print(current.data, end=" - ")
        current = current.next
        count += 1
    print("No more nodes")
    print("Nodes:", count)

print_linked_list_with_count(node1)