from cracking.ch2.node import Node

class Queue:
    def __init__(self):
        self.node = None
        self.first = None

    def add(self, item):
        if self.is_empty():
            self.node = Node(item)
            self.first = self.node
        else:
            self.node.next = Node(item)
            self.node = self.node.next
    
    def remove(self):
        if self.is_empty():
            return None
        
        data = self.first.data
        if self.first == self.node:
            self.first = self.node = None
        else:
            self.first = self.first.next
        return data
    
    def is_empty(self):
        return self.node is None

    def __str__(self) -> str:
        result = "*"
        if not self.is_empty():
            current = self.first
            while current:
                result += "<-" + str(current)
                current = current.next
            return result
            
if __name__ == '__main__':
    queue = Queue()
    queue.add(4)
    queue.add(5)
    queue.add(2)
    queue.add(10)

    print(queue)

    print(queue.remove())
    print(queue.remove())
    print(queue.remove())

    queue.add(8)

    print(queue)