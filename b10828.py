import sys

def push(value):
    stack.append(value)

def pop():
    if stack.IsEmpty:
        return -1
    else:
        return stack.pop()
    
def size():
    return len(stack)

def top():
    if stack.IsEmpty:
        return -1
    else:
        return stack[-1]

def empty():
    if stack.IsEmpty:
        return 0
    else:
        return 1

    
stack = []
n = int(sys.stdin.readline())



for i in range(n):
    input_split = sys.stdin.readline().split()
    order = input_split[0]

    if order == "push":
        push(input_split[1])
    elif order == "pop":
        print(pop())
    elif order == "size":
        print(size())
    elif order == "top":
        print(top())
    elif order == "empty":
        print(empty())
