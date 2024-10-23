# Determine whether a linked list contains a loop as quickly as possible 
# without using any extra storage.

import random

class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, x):
        new_node = ListNode(x)
        new_node.next = self.head
        self.head = new_node
    
    def insert_many(self, vals):
        for val in vals:
            self.insert(val)

    def create_random_loop(self):
        if self.head is None:
            print("Empty list")
            return
        
        # traverse the list and collect all nodes
        current = self.head
        nodes = []
        while current is not None:
            nodes.append(current)
            current = current.next

        if len(nodes) < 2:
            print("Cannot create a loop with less than 2 nodes")
            return

        # randomly select a node from the list
        loop_target = random.choice(nodes)

        # point the last node to the target
        last_node = nodes[-1]
        last_node.next = loop_target

    def has_loop(self):
        # Use slow and fast pointers
        slow = self.head
        fast = self.head

        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
            
    def detect_loop(self):
        has_loop = self.has_loop()
        if has_loop:
            print('Loop detected')
        else:
            print('No loop')

# Usage
def main():
    linked_list = LinkedList()
    linked_list.insert_many([3, 5, 7, 9, 11, 13])
    linked_list.detect_loop()

    linked_list.create_random_loop()
    linked_list.detect_loop()


if __name__ == "__main__":
    main()
