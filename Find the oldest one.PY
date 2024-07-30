A=int(input("enter age A: "))
B=int(input("enter age B: "))
C=int(input("enter age C: "))

if A > B and B>C:
    print("A is older than B and C",A)
elif B > A and A > C:
    print("B is older than A and C",B)
else:
    print("C is older than A and B",C)