# Exercise 2: Print the sum of the current number and the previous number

# Write a program to iterate the first 10 numbers, and in each iteration, print the sum of the current and previous number.

# pseudocode
# printing what program run
print("Printing current and previous number and their sum in a range(10)")
# setting value for first previous number
previous_number = 0

# range for the first 10 numbers
for i in range (1,10):
    sum_of_the_current_number_and_previous_number = previous_number + i
    print("Current Number", i, "Previous Number ", previous_number, " Sum: ",sum_of_the_current_number_and_previous_number)
    # modify previous number
    # set it to the current number
    previous_number = i
# printing current number value, previous number value, and the sum value
    
    