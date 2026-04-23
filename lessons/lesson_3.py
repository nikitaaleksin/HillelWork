# Нуль на кiнець
list1 = [123, 0, 45, 0, 67, 0, 234]
result_with_zero_at_the_end = list()
count_of_zero_at_the_end = 0
for num in list1:
    if num != 0:
        result_with_zero_at_the_end.append(num)
    else:
            count_of_zero_at_the_end += 1
result_with_zero_at_the_end = result_with_zero_at_the_end + [0] * count_of_zero_at_the_end
print(result_with_zero_at_the_end)



# Три числа
import random

my_list = random.randint(3, 10)
random_list1 = [random.randint(1, 10) for _ in range(my_list)]
print("Перший лист", random_list1)

list2 = [random_list1[0], random_list1[2], random_list1[-2]]
print("Рузультат", list2)

# Множення
numbers2 = [int(x) for x in input("Your numbers: ").split(", ")]
i = 0
for index, num in enumerate(numbers2):
    if index % 2 == 0 and index <= 4:
        i += num
result = i * numbers2[-1]
print(result)













