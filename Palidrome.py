##  Palindrome: That is to flip or reverse words


##  Collect input and make it lower case
words_input = input("Enter any single word in lower case: ")

##  To conveert to lower case
words_input = words_input.lower()

##  print the lower case
print(words_input)

##  Flip the string 
flipped_input = words_input[::-1]

##  Flip the input
print(flipped_input)

##  Check if input  words_input equals flipped_input
if words_input == flipped_input:

##  When true, print (it is a palindrome) else print(not palindrome)
  print("it is a palindrome")

##  else:
  print("Not palindrome")


    




