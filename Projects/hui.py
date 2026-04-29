import random
#word = input("Your word: ")
#for letter in word:
  #  if letter != "a" and letter != "A":
   #     print(letter)





#user_number = int(input("Enter a number: "))
#while user_number != 7:
   # print("Попробуй ещё раз: ")
  #  user_number = int(input("Enter a number: "))
#if user_number == 7:
  # print("Победа!!")

#height = int(input("Enter a height: "))
#width = int(input("Enter a width: "))
#for i in range(height):
   # for j in range(width):
   #     print("*", end="")
   # print()


#word_1 = input("Enter a word: ")
#letters = "aeiouyAEIOUY"
#for letter in word_1:
   # if letter in letters:
   #     print(letter)



#number = input("Enter word: ")
#i = "0123456789"
#for j in number:
   # if j in i:
   #     print(j)



number = random.randint(1,10)
print ("я загадал число ")
add = 0
while True:
   user = int(input("Enter a number: "))
   add += 1
   if user > number:
       print("много")
   elif user < number:
       print("мало")

   else:
       if add == 1:
           print("c первой попытки!!")
       print(f" Победа, ты угадал с {add} попытки ")
       break

number_1 = int(input("Enter a number: "))
for n in range(1, number_1+1):
    for b in range(1, number_1+1):
        print(f"{n} * {b} = {n*b}")
    print("-" * 10)


size = int(input("Enter a number: "))
s1 = "#"
s2 = "*"
for s in range(size):
    for c in range(size):
        if (s + c) %2 ==0:
            print(s1, end = " ")
        else:
            print(s2, end = " ")
    print()

size = int(input("Enter a number: "))
for s in range(size):
    for c in range(size):
        print(s+c, end = " ")
    print()











