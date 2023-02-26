class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def __str__(self) -> str:
        return "Node({0})".format(self.data)
