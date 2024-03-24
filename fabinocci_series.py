#Program to find fabinocci series upto n terms.

#input validation
try:
    n_terms = int(input("Enter no. of Fabinocci series:"))
#Error message
except ValueError:
    print("You have to enter a positive number!")
#
else:
    n1 = 0
    n2 = 1
    cnt = 0
    if n_terms == 0 or n1 == 1:
        print(n1)
    else:
        for i in range(0, n_terms):
            print(n1)
            res = n1 + n2
            n1 = n2
            n2 = res
            cnt += 1
