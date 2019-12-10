set_of_numbers = set()
set_of_numbers.add(1)
set_of_numbers.add(2)

li   = [1, 3, 4, 4.32, 5, 6, 56]
setli = [1, 3, 4, 4.32, 5, 6, 56]
set_of_numbers.update(setli)
set_of_numbers

import random
from random import randint

numbers = []
for num in range(10):
    numbers.append(randint(0,10))

   
for unique_num in set (numbers):
    key = unique_num
    value = numbers.count(unique_num)
    print(f'assigning key{key} to value {value}')
    counter[key] = value

for unique_num in set(numbers):
    key = unique_num
    value = numbers.count(unique_num)
    print(f'assigning key{key} to value {value}')
    counter_list.append((key, value))
