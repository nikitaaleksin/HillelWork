# Списки ( остання цифра )
numbers = [1, 3, 5, 10, 44, 123, 1044]
numbers.insert(0, 1044)
numbers.pop(-1)
print(numbers)

# Список подiл
things = [ "bread", "butter", "cucumber", "tomato" ]
print("First list", things)
things_2 = ["tangerin", "sausage", "coconut"]
print("Second list:", things_2)
things.extend(things_2)
print("Final list", things)

# Калькулятор
num1 = float(input("Перше число: "))
op = input("Дiя(+, -, *, /,) : " )
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
