# Exercise 2: Print the sum of the current number and the previous number

# Write a program to iterate the first 10 numbers, and in each iteration, print the sum of the current and previous number.

# pseudocode
# printing what program run
print("\033[1;32;40mPrinting current and previous number and their sum in a range(10)")

# setting value for first previous number
previous_number = 0

# range for the first 10 numbers
for i in range (0,10):
    sum_of_the_current_number_and_previous_number = previous_number + i
# printing current number value, previous number value, and the sum value    
    print("\033[1;32;40mCurrent Number is", i, "Previous Number is ", previous_number, " Sum: ",sum_of_the_current_number_and_previous_number)
    
    previous_number = i

    
    