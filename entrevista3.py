# DO NOT CHANGE THIS CLASS
class Stack:
    def __init__(self):
        self._items = []

    def push(self, value):
        self._items.append(value)

    def pop(self):
        return self._items.pop()

    def peek(self):
        return self._items[-1]

    def is_empty(self):
        return len(self) == 0

    def __len__(self):
        return len(self._items)


# IMPLEMENT YOUR SOLUTION HERE (DO NOT CHANGE THE ARGUMENTS)
def sort_stack(stack):
    stack2 = Stack()
    
    if stack.is_empty():
        return stack
    tmp = stack.pop()
    stack2.push(tmp)
    tmp = None

    while True:
        if stack.__len__() == 0:
            break
        elif tmp == None:
            tmp = stack.pop()
        
        if stack2.is_empty():
            stack2.push(tmp)
            tmp = None
        elif stack2.peek() > tmp:
            stack.push(stack2.pop())
        else:
            stack2.push(tmp)
            tmp = None
    
    while stack2.__len__() != 0:
        stack.push(stack2.pop())

    
    return stack

