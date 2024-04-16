class Node:
    def __init__(self, item, next=None):
        self.item = item
        self.next = next
class Stack:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def push(self, item):
        self.head = Node(item, self.head)

    def pop(self):
        item = self.head.item
        self.head = self.head.next
        return item

    @property
    def peek(self):
        return self.head.item

    def __len__(self):
        count = 0
        current = self.head
        while current is not None:
            count +=1
            current = current.next
        return count
class MyQueue:
    def __init__(self):
        self.stack = Stack()
        self.reverse_stack = Stack()

    def push(self, x: int) -> None:
        probe = self.stack.head
        while probe is not None:
            self.reverse_stack.push(self.stack.pop())
            probe = probe.next
        self.stack.push(x)
        probe_reverse = self.reverse_stack.head
        while probe_reverse is not None:
            self.stack.push(self.reverse_stack.pop())
            probe_reverse = probe_reverse.next
        return self.stack
    def pop(self) -> int:
        item = self.stack.head.item
        self.stack.head = self.stack.head.next
        return item

    def peek(self) -> int:
        return self.stack.head.item

    def empty(self) -> bool:
        return self.stack.head is None


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
