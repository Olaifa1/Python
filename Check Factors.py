

#   Collect a value from user
end_of_range = int(input("Enter any number"))
for num in range(2, end_of_range):
    sum_of_factors = 0

    for factors in  range(1, num):
        if num  % factors == 0:
            sum_of_factors += factors

    if sum_of_factors == num:
        print(num, 'is a perfect number')
                   
    elif sum_of_factors > num:
         print(num, 'is abundant')

    else:
        print(num, 'is deficient')
             
             



             
             
             

             
