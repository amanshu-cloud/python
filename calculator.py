def add(a, b):
    return a+b


def sub(a, b):
    if a > b:
        return a-b
    else:
        return b-a


def mul(a, b):
    return a*b


def div(a, b):
    return a/b


print("calculator using python\n1-add\n2-subtract\n3-multiply\n4-divide\n")
choice = int(input("enter choice : "))
if choice == 1:
    num_1 = int(input("enter num1:"))
    num_2 = int(input("enter num2:"))
    print(f"addition of num1 and num2 is {add(num_1,num_2)}")

elif choice == 2:
    num_1 = int(input("enter subrahend: "))
    num_2 = int(input("enter subtractor : "))
    print(f"subtraction of{num_1} and {num_2} is {sub(num_1,num_2)}")
