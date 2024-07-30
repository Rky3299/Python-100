num1 = int(input("enter first: "))
num2 = int(input("enter second: "))

num1 = num1 ^ num2
num2 = num1 ^ num2
num1 = num1 ^ num2

print("after swapping the first nunmber is: ", num1)
print("after swapping the second number is: ", num2)