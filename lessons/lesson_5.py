#Діапазон букв
from string import ascii_letters

from lessons.math import minutes

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


#
import time
user_time = input("Input your number:")
for t in divmod(int(user_time), 60):
    

