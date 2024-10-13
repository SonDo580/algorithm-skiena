from stack import Stack

# enqueue always takes O(1)
# dequeue takes O(1) if stack_out is not empty
class Queue:
    def __init__(self):
        self.stack_in = Stack()
        self.stack_out = Stack()

    def enqueue(self, x):
        self.stack_in.push(x)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        
        # move items from stack_in to stack_out in reverse order
        if self.stack_out.is_empty():
            while not self.stack_in.is_empty():
                self.stack_out.push(self.stack_in.pop())
        
        return self.stack_out.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Queue is empty")
        
        if not self.stack_out.is_empty():
            return self.stack_out.peek()
        
        return self.stack_in.bottom()

    def is_empty(self):
        return self.stack_in.is_empty() and self.stack_out.is_empty()
    
    def size(self):
        return self.stack_in.size() + self.stack_out.size()

# Usage
def main():
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)

    print("Front element:", q.peek())  
    print("Queue size:", q.size())

    while not q.is_empty():
        print("Dequeued element:", q.dequeue())
        print("Queue size after dequeue:", q.size())
    
    # print(q.dequeue())  # IndexError    

if __name__ == "__main__":
    main()