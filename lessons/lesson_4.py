#Модифiкований канкультятор
import keyword

while True:
    num1 = float(input("Перше число: "))
    op = input("Дiя(+, -, *, /,) : ")
    num2 = float(input("Друге число: "))
    if op == "+":
        print(num1 + num2)
    elif op == "-":
       print(num1 - num2)
    elif op == "**":
        print(num1 ** num2)
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


#hashtag
while True:
    my_string = input("Введiть слова: ")
    my_string = my_string.title()
    for l in "'!,.?:":
        my_string = my_string.replace(l, "")
    hashtag = "#" + my_string.replace(" ", "")
    hashtag = hashtag[:140]
    print(hashtag)
    choice = input("Продовжити роботу? (y/n):")
    if choice == "y":
        continue
    if choice == "n":
     print("Роботу завершено")
     break







from string import digits, punctuation
user = input('Enter you variable example:')
is_start_with_digits = user[0].isdigit() if user else False
prohibited = punctuation.replace('_', '') + ' '
is_contain_prohibited_symbol = any(s in prohibited for s in user)
is_double_underscore = '__' in user
is_contain_uppercase = False
for s in user:
    if s.isupper():
        is_contain_uppercase = True
        break
is_keyword = user in keyword.kwlist
if not is_start_with_digits and not is_contain_uppercase and not is_contain_prohibited_symbol and not is_keyword and not is_double_underscore and user != "":
    print(True)
else:
    print(False)



