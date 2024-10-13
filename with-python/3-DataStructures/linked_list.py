class ListNode:
    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    # Insert new node at the head
    def insert(self, x):
        new_node = ListNode(x)
        new_node.next = self.head
        self.head = new_node

    def search(self, x):
        current = self.head
        while current is not None:
            if current.val == x:
                return current
            current = current.next
        return None

    # Delete a node by value
    def delete(self, x):
        current = self.head
        predecessor = None

        while current is not None:
            if current.val == x:
                if predecessor is None:
                    # deleting the head
                    self.head = self.head.next
                else:
                    # skip the current node
                    predecessor.next = current.next
                return

            predecessor = current
            current = current.next

        print(f"{x} not found in list")

    def print(self):
        current = self.head
        while current is not None:
            print(current.val, end=" -> ")
            current = current.next
        print("None")


# Usage
def main():
    linked_list = LinkedList()

    # Insert elements into the list
    linked_list.insert(3)
    linked_list.insert(5)
    linked_list.insert(7)
    linked_list.insert(9)
    print("List after inserts:")
    linked_list.print()

    # Delete an element
    linked_list.delete(5)
    print("List after deleting 5:")
    linked_list.print()

    # Attempt to delete a non-existent element
    linked_list.delete(12)
    print("List after trying to delete 12:")
    linked_list.print()


if __name__ == "__main__":
    main()
