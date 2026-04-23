while True:
    num1 = float(input("Перше число: "))
    op = input("Дiя(+, -, *, /,) : ")
    num2 = float(input("Друге число: "))
    if op == "+":
        print(num1 + num2)
    elif op == "-":
        print(num1 - num2)
    elif op == "*":
        print(num1 * num2)
    elif op == "/":
        print(num1 / num2 if num2 != 0 else "Ділення на нуль")
    else:
        print("Неправильна дiя")

    choice = input("Продовжити роботу? (y/n):")
    if choice == "y":
        continue
    if choice == "n":
        print("Роботу завершено")
        break



