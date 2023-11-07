def print_menu():
    print("Choose an option:")
    print("1 - Put a number onto the stack")
    print("2 - Pop the top number from the stack")
    print("3 - Print the biggest number in the stack")
    print("4 - Print the smallest number in the stack")
    print("5 - Print the length of the stack")
    print("6 - Quit")

print("Enter how many options you want to run: ")
n = int(input())
stack = []

print_menu()

for _ in range(n):
    command = input().split()
    action = int(command[0])

    if action == 1:
        number = int(command[1])
        stack.append(number)
    elif action == 2:
        if stack:
            stack.pop()
    elif action == 3:
        if stack:
            print(max(stack))
    elif action == 4:
        if stack:
            print(min(stack))
    elif action == 5:
        print(len(stack))
    elif action == 6:
        break

while stack:
    if len(stack) > 1:
        print(stack.pop(), end=", ")
    else:
        print(stack.pop())
