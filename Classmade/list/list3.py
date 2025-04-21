#PILA

stack = []

def push(val):
    if len(stack) < 5:
        stack.append(val)
    else:
        print("Stack overflow")

def pop():
    if len(stack) > 0:
        return stack.pop()
    else: 
        print("Stack underflow")

def menu():
    print("1. Push")
    print("2. Pop")
    print("3. Exit")
    return int(input("Enter choice: "))

while True:
    choice = menu()
    if choice == 1:
        push(int(input("Enter value: ")))
    elif choice == 2:
        print(pop())
    elif choice == 3:
        break
    else:
        print("Invalid choice")