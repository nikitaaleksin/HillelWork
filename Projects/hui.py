word = input("Your word: ")
for letter in word:
    if letter != "a" and letter != "A":
        print(letter)





user_number = int(input("Enter a number: "))
while user_number != 7:
    print("Попробуй ещё раз: ")
    user_number = int(input("Enter a number: "))
if user_number == 7:
   print("Победа!!")

height = int(input("Enter a height: "))
width = int(input("Enter a width: "))
for i in range(height):
    for j in range(width):
        print("*", end="")
    print()











