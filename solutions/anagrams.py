"""
Problem: write a function, reverse_list, that takes in the head of a
linked list as an arguement. The function should return the reversed
order of the nodes in the linked list in-place and return the new head 
of the linked list

Cases & Edge Cases:
1. Empty list
2. Only contains the head
3. Reversed list

Algorithm:
1. Initialize variables
    1a. previous = None
    1b. current = head
2. Initialize while loop -> while elements in list
    2a. Initlaize next = next element after current
    2b. Update next pointer to point to prev element
    2c. Move prev pointer to current element
    2d. Move current pointer to next element
3. Return prev

"""
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
        
def reverse_list(head):
    prev = None 
    current = head
    
    while current is not None:
        next = current.next
        current.next = prev
        prev = current
        current = next
    return prev

# creating nodes
a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")
    
# creating linked list
a.next = b
b.next = c
c.next = d
d.next = e
e.next = f

# print original list
print("Original list:")
current = a
while current is not None:
    print(current.value, end = " -> ")
    current = current.next
print("End")

# reversing linked list
a = reverse_list(a)

#printing reversed list
print("Reversed list:")
current = a
while current is not None:
    print(current.value, end = " -> ")
    current = current.next
print("End")