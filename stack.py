class Stack:
    def __init__(self):
        self.stack = []
    def push(self, var):
        self.stack.append(var)
    def pop(self):
        self.stack.pop()
    def max(self):
        if (len(self.stack) == 0):
            return -1
        maximum = self.stack[0]
        for element in self.stack:
            if (element > maximum):
                maximum = element
        return maximum
    def printStack(self):
        for element in self.stack:
            print(str(element))

def main():
    stack = Stack()
    stack.push(3)
    stack.push(4)
    stack.push(5)
    stack.push(0)
    stack.push(1)
    stack.push(6)
    print("After pushing: ")
    stack.printStack()
    stack.pop()
    stack.pop()
    stack.pop()
    print("After popping: ")
    stack.printStack()
    print("Max is " + str(stack.max()))

if __name__ == "__main__":
    main()