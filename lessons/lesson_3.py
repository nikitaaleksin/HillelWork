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





# Множення
numbers2 = [2, 5, 7, 12, 45, 13, 56]
sum_lst5 = numbers2[0] + numbers2[2] + numbers2[4]
print(sum_lst5)
multiply_lst2 = sum_lst5 * numbers2[-1]
print(multiply_lst2)

# Три числа
import random

my_list = random.randint(3, 10)
random_list1 = [random.randint(1, 10) for _ in range(my_list)]
print("Перший лист", random_list1)

list2 = [random_list1[0], random_list1[2], random_list1[-2]]
print("Рузультат", list2)

