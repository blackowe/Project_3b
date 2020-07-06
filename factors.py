# Author: Erik Blackowicz
# Date: 7/6/20
# Description: Code asks the user to enter a positive integer, then prints a list
# of all positive integers that divide that number evenly, including itself and 1.

user_int = int(input("Please enter a positive integer: "))
print("The factors of", user_int, "are:")

for i in range(1,user_int+1):  # want to include user_int into test range, so use +1
    if user_int % i ==0:    # Asking if the user_int is evenly divisible by the iterating value
        print(i)
