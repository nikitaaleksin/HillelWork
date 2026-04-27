#Діапазон букв
from string import ascii_letters



while True:
 string_1 = input("Введiть двi лiтери через дефiс: ")
 start_str, end_str = string_1.split('-')
 start_pos = ascii_letters.find(start_str)
 end_pos = ascii_letters.find(end_str)
 print(ascii_letters[start_pos:end_pos + 1] )
 user = input("Продовжити: Y/N")
 if user == "Y":
     continue
 if user == "N":
    print("Робота завершена")
    break


#Конвертер із числа в дату
import time
user_time = input("Input your number:")
days, second = divmod(int(user_time), 86400)
hours, second = divmod(second, 3600)
minutes, seconds = divmod(second, 60)
if days % 10 == 1 and days % 100 != 11:
    day_l = "день"
elif 2<= days % 10 <=4 and days % 100 < 10 or days % 100 >=20:
    day_l = "днi"
else:
    day_l = "днiв"
h = str(hours).zfill(2)
m = str(minutes).zfill(2)
s = str(seconds).zfill(2)
print(f"{days}, {day_l}, {h} : {m} : {s}")



#Добуток чисел


user_numbers = input("Input your numbers:")
while int(user_numbers) > 9:
    res = 1
    for digit in str(user_numbers):
        res *= int(digit)
    user_numbers = res
print(f"{user_numbers}")






    

