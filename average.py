#Author: Dennis Lam
#GitHub username: dennislam4
#Date: 6/21/2022
#Description: Asks the user to input ANY five numbers and then prints the average of those numbers.

num_1 = float(input("Please enter 5 more numbers: "))
num_2 = float(input("Please enter 4 more numbers: "))
num_3 = float(input("Please enter 3 more numbers: "))
num_4 = float(input("Please enter 2 more numbers: "))
num_5 = float(input("Please enter 1 more number: "))
avg = ((num_1 + num_2 + num_3 +num_4 + num_5) / 5)
print(f"The average of your numbers entered is : {avg}.")
