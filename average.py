#Author: Dennis Lam
#GitHub username: dennislam4
#Date: 6/21/2022
#Description: Asks the user to input ANY five numbers and then prints the average of those numbers.

print("Please enter five numbers.")
num_1 = float(input())
num_2 = float(input())
num_3 = float(input())
num_4 = float(input())
num_5 = float(input())
avg = round(((num_1 + num_2 + num_3 +num_4 + num_5) / 5),1)
print(f"The average of those numbers is: \n{avg}")
