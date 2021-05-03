num1=int(input("enter first operand"))
num2=int(input("enter second operand"))
op=input("enter ur operator")

if op=="*":
    if (num1==45 or num1==3)and(num2==3 or num2==45):
        print(555)
    else:
        print(num1*num2)
elif op=="/":
    if num1==56 and num2==6 :
        print(4)
    else:
        print(num1/num2)
elif op=="+":
    if (num1==56 or num1==9) and (num2==9 or num2==56):
        print(77)
    else:
        print(num1+num2)
elif op=="-":
    print(num1-num2)
else:
    print("invalid operator entered")