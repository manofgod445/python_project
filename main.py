from calculattor import plus, minus, division, multiplication, modules, infrential

arith = input("Enter operator: ")
first_num = int(input("enter first num: "))
sec_num = int(input("enter your second num: "))

if arith == "+":
    print(plus(first_num, sec_num))
elif arith == "-":
    print(minus(first_num, sec_num))
elif arith == "/":
    print(division(first_num, sec_num))
elif arith == "*":
    print(multiplication(first_num, sec_num))
elif arith == "%":
    print(modules(first_num, sec_num))
elif arith == "**":
    print(infrential(first_num, sec_num))
else:
    print("error")
