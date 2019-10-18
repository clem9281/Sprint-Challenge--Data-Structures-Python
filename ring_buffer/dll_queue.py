from dll import DoublyLinkedList
class Queue:
    def __init__(self):
        self.storage = DoublyLinkedList()
    def __str__(self):
        return f"Queue: storage: {self.storage}"
        
    def enqueue(self, value):
        self.storage.add_to_tail(value)

    def dequeue(self):
        if self.storage.length is 0:
            return
        old_head = self.storage.head
        self.storage.remove_from_head()
        return old_head.value

    def __len__(self):
        return len(self.storage)