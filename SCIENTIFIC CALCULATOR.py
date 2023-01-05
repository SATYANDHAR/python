import math
c = input("Enter an operator: ")
if c in ["+","-","*","/","//","%","**"]:
    a = float(input("Enter the 1st number: "))
    b = float(input("Enter the second number: "))
    if  c == "+":
        print("result:",a + b)
    elif c == "-":
        print("result:",a-b)
    elif c == "*":
        print("result:",a*b)
    elif c == "/":
        print("result:",a/b)
    elif c == "/":
        print("result:",a/b)
    elif c == "//":
        print("result:",a//b)
    elif c == "%":
        print("result:",a%b)
    elif c == "**":
        print("result:",a**b)
elif c in ["sin","cos","tan","cosec","sec","cot"]:
    d = float(input("Enter the number: "))
    if c == "sin":
        print("result:",math.sin(d))
    elif c == "cos":
        print("result:",math.cos(d))
    elif c == "tan":
        print("result:",math.tan(d))
    elif c =="cot":
        print("result:",math.cot(d))
    elif c =="sec":
        print("result:",math.sec(d))
    elif c =="cosec":
        print("result:",math.cosec(d))
elif c in ["radian","degree"]:
    if c == "radians":
        e = float(input("Enter value in degree: "))
        print("result:",math.radians(e))
    elif c == "degrees":
        e = float(input("Enter value in radian: "))
        print("result:",math.degrees(e))
else:
    print("Enter correct value! ")