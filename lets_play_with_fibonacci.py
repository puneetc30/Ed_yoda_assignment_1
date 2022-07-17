num3 = 0
num1, num2 = 0, 1
while num3 < 50:
    num3 = num1+num2
    num1 = num2
    num2 = num3
    print(num1, end = " ")