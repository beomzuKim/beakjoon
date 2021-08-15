import sys

def push(value):
    stack.append(value)

def pop():
    if stack:
        return stack.pop()
    else:
        return -1

def size():
    return len(stack)

def top():
    if stack:
        return stack[-1]
    else:
        return -1

def empty():
    if stack:
        return 1
    else:
        return 0


stack = []
n = int(sys.stdin.readline())

for i in range(n):
    input_split = sys.stdin.readline().split()  # << 10진수로 변환이 안됨. 왜지?
    order = input_split[0]

    if order == "push":
        push(input_split[1])  # << 띄어쓰기가 있으니까 1이 되는건 이해했음.
    elif order == "pop":
        print(pop())
    elif order == "size":
        print(size())
    elif order == "top":
        print(top())
    elif order == "empty":
        print(empty())

# 첫번재 숫자는 명령의 수를 나타냄. i가 명령의수를 나타내는건가? 어떤식으로 입력되는건지 확실하게 이해가 안됨.
