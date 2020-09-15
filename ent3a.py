# How would you design a stack which, in addition to push and pop, has a function min which returns the minimum element? Push, pop and min should all operate in O(1) time.

class Stack:
    def __init__(self):
        # Your subclass must not access this attribute
        self._items = []
        self._mitems = []

    def push(self, value):
        self._items.append(value)
        StackWithMin.check_min_push(self,value)

    def pop(self):
        value = self._items.pop()
        StackWithMin.check_min_pop(self,value)
        return value

    def peek(self):
        return self._items[-1]

    def empty(self):
        return len(self) == 0

    def __len__(self):
        return len(self._items)

class StackWithMin(Stack):
    def __init__(self):
        self._items = []
        self._mitems = []
        
    def check_min_push(self, value):
        if self._mitems:
            if value <= self.minimum() :
                self._mitems.append(value)

        else:
             self._mitems.append(value)

    def check_min_pop(self, value):
        if self._mitems:
            if value<= self.minimum():
                self._mitems.pop()

    def minimum(self):
        if self._mitems:
            return self._mitems[-1]
