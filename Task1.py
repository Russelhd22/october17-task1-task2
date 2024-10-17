def calculations1(num1, num2):
    resultadd = num1 + num2
    return 'total : ', resultadd
def calculations2(num1, num2):
    resultsub = num1 - num2
    return 'total : ', resultsub
def calculations3(num1, num2):
    resultmul = num1 * num2
    return 'total : ', resultmul
def calculations4(num1, num2):
    resultdiv = num1 / num2
    return 'total : ', resultdiv
num1 = int(input("Enter a fnum: "))
num2 = int(input("Enter a snum: "))
operation = str(input("Enter a operation (+,-,*,/): "))

if operation == "+":
    print(calculations1(num1, num2))
elif operation == "-":
    print(calculations2(num1, num2))
elif operation == "*":
    print(calculations3(num1, num2))
elif operation == "/":
    print(calculations4(num1, num2))
else:
    print("Error")