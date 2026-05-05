#Вітання
from collections import namedtuple
def say_hi(name, age):
    return f"Hi. My name is {name}, I am {age} years old"
assert say_hi("Alex", 32) == "Hi. My name is Alex, I am 32 years old"
assert say_hi("Frank", 64) == "Hi. My name is Frank, I am 64 years old"
print('OK')


#Модифікувати рядок
def correct_sentence(text):
    text = text[0].upper() + text[1:]
    if not text.endswith('.'):
        text += '.'
    return text
assert correct_sentence("greetings, friends") == "Greetings, friends."
assert correct_sentence("hello") == "Hello."
assert correct_sentence("Greetings. Friends") == "Greetings. Friends."
print('OK')



#Пошук підрядка
def second_index(text:str, some_str:str):
    first_index = text.find(some_str)
    if first_index == -1:
        return -1
    second_index = text.find(some_str, first_index + 1)
    if second_index == -1:
        return None
    return second_index
assert second_index("sims", "s") == 3, 'Test1'
assert second_index("find the river", "e") == 12, 'Test2'
assert second_index("hi", "h") is None, 'Test3'
assert second_index("Hello, hello", "lo") == 10, 'Test4'
print('ОК')



#Пошук спільних елементів
def common_elements():
    list_3 = [ x for x in range(100) if x % 3 ==0  ]
    list_5 = [ x for x in range(100) if x % 5 ==0 ]
    result = set(list_3) & set(list_5)
    return result
assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
print("OK")




