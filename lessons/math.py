# Тренувальнi вправи
a = 50
b = 25
print ( a+b )

int1 = 4
int2= 2
float1 = 2.5
float2 = 2.5
print(int1 // int2)
print(float1 / float2)

a = 3
b = 3
print(a ** b)

# Середне число
numbers = [7,9,8,5]
average = sum(numbers) / len(numbers)
print(average)

# час та хвилина
minutes = 125
hours, mins = divmod(minutes, 60)
print(hours, mins)

# Цiна зi знижкою
prise = 200
discount_percent = 80
print ( prise * (discount_percent / 100) )



# Perimeter
a = 4
b = 3
perimeter = 2 * (a + b)
print (perimeter)

# Last digit
int3 = 5490
last_digit = int3 % 10
print ( last_digit )




# Enter your numbers
numbers = (input("Your numbers"))
num = int(numbers)
digit1 =   num// 1000
digit2 = (num // 100) % 10
digit3 = (num // 10) % 10
digit4 = num % 10
print (digit1)
print (digit2)
print (digit3)
print (digit4)

