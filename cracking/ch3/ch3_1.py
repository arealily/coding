source = list()

def padding_insert(l, index, item):
    if len(l) <= index:
        for _ in range(index - len(l) + 1):
            l.append(None)
    l[index] = item

stack_num = 3

class Stack:
    def __init__(self, stack_id):
        self.index = stack_id - stack_num
        self.stack_id = stack_id

    def push(self, item):
        self.index = self.index + stack_num
        padding_insert(source, self.index, item)
    
    def peek(self):
        if self.is_empty():
            return None
        return source[self.index]

    def pop(self):
        if self.is_empty():
            return None
        item = source[self.index]
        self.index = self.index - stack_num
        return item
    
    def is_empty(self):
        return self.index < stack_num
    
    def __str__(self) -> str:
        result = "Stack" + str(self.stack_id) + "*"
        for i in source[self.stack_id:self.index + 1:stack_num]:
            result += "->" + str(i)
        return result

if __name__ == '__main__':
    stack1 = Stack(0)
    stack2 = Stack(1)

    stack1.push(2)
    stack1.push(3)
    stack1.push(10)

    print(stack1)
    stack1.pop()
    print(stack1)
    stack1.push(9)
    print(stack1)

    stack2.push(3)
    stack1.push(100)
    stack2.push(3)
    stack2.push(10)
    print(stack2)
    stack2.pop()
    print(stack2)
    print(stack1)