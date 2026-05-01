#
from collections import namedtuple
def say_hi(name, age):
    return f"Hi. My name is {name}, I am {age} years old"
assert say_hi("Alex", 32) == "Hi. My name is Alex, I am 32 years old"
assert say_hi("Frank", 64) == "Hi. My name is Frank, I am 64 years old"
print('OK')


#
def correct_sentence(text):
    text = text[0].upper() + text[1:]
    if not text.endswith('.'):
        text += '.'
    return text
assert correct_sentence("greetings, friends") == "Greetings, friends."
assert correct_sentence("hello") == "Hello."
assert correct_sentence("Greetings. Friends") == "Greetings. Friends."
print('OK')



#

