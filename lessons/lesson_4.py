from operator import truediv  # Модифiкований канкультятор

from prompt_toolkit import choice

#while True:
  #  num1 = float(input("Перше число: "))
   # op = input("Дiя(+, -, *, /,) : ")
   # num2 = float(input("Друге число: "))
   # if op == "+":
   #     print(num1 + num2)
   # elif op == "-":
 #       print(num1 - num2)
   # elif op == "*":
      #  print(num1 * num2)
 #   elif op == "/":
       # print(num1 / num2 if num2 != 0 else "Ділення на нуль")
  #  else:
   #     print("Неправильна дiя")

   # choice = input("Продовжити роботу? (y/n):")
   # if choice == "y":
    #    continue
  #  if choice == "n":
    #    print("Роботу завершено")
     #   break


#hashtag
while True:
    my_string = input("Введiть слова: ")
    my_string = my_string.title().replace(" ", "")
    for l in "'!,.?:":
        my_string = my_string.replace(l, "")
    hashtag = "#" + my_string.lower().replace(" ", "")
    hashtag = hashtag[:140]
    print(hashtag)
    choice = input("Продовжити роботу? (y/n):")
    if choice == "y":
        continue
    if choice == "n":
     print("Роботу завершено")
     break



