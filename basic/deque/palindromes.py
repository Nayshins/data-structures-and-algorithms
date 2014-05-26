class Deque:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def addFront(self, item):
        self.items.append(item)

    def addRear(self, item):
        self.items.insert(0,item)

    def removeFront(self):
        return self.items.pop()

    def removeRear(self):
        return self.items.pop(0)

    def size(self):
        return len(self.items)

def palindromeChecker(string):
    testdeque = Deque()

    for char in string:
        testdeque.addRear(char)


    stillEqual = True

    while testdeque.size() > 1 and stillEqual:
        first = testdeque.removeFront()
        last = testdeque.removeRear()
        if first != last:
            stillEqual = False

    return stillEqual

print(palindromeChecker("lsdkjfskf"))
print(palindromeChecker("radar")) 