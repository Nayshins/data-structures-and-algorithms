class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)

def divideBy2(decNumber):
    remainderStack = Stack()
    
    while decNumber >0:
        remainder = decNumber % 2
        remainderStack.push(remainder)
        decNumber = decNumber // 2
        print remainderStack.peek()

    binaryString = ""
    while not remainderStack.isEmpty():
        binaryString = binaryString + str(remainderStack.pop()) 
        print binaryString
    return binaryString

print(divideBy2(42))           