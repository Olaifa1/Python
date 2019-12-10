
#   Initializing our list
my_list = [5,1,4,2,8, 9,10, 220,1,-2,-3,23]

#   To  assign the size of the list to varaible list_size
list_size = len(my_list)

#   Initializing swapped as tppe boolean
swapped = True

while swapped:
#   loop from the first element in the list through the size of the list    
    for current_index in range(1, list_size):
        prev_index = current_index - 1
#   Multiple assignment: Assigning the previous index to previous value and current index to current value
        prev_value, current_value =  my_list[prev_index], my_list[current_index]

#   If the previous value is greater than the current value,
        if prev_value > current_value:
#   then slice the list between the  previous index and the current index, assign the current value to the previous index
#   assign the previous value to the current index
            my_list[prev_index:current_index+1]  = current_value, prev_value

#   Check if swapped is true, if false that means the value on the right side, between two values beside eachother in my_list,
#   is greater than the value on the left side. So, if swapped is false, the swapping stops.
            swapped = True

#   Print my_list            
            print(my_list)
                                       
