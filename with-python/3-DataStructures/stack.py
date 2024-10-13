class Stack:
    def __init__(self):
        self.items = []

    def push(self, x):
        self.items.append(x)

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.items[-1]
    
    # a trick for faster peek() of a queue (see queue.py)
    def bottom(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.items[0]

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty")
        return self.items.pop()
    
    def is_empty(self):
        return len(self.items) == 0
    
    def size(self):
        return len(self.items)

# Usage
def main():
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)

    print("Top element:", s.peek())  # Output: Top element: 3
    print("Stack size:", s.size())    # Output: Stack size: 3

    while not s.is_empty():
        print("Popped element:", s.pop())
        print("Stack size after pop:", s.size())
    
    # print(s.pop())  # IndexError
        
if __name__ == "__main__":
    main()