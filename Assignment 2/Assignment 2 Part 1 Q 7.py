# part1 Q 7
num1=int(input("Enter the first numnber :"))
num2=int(input("Enter the second numnber :"))
op= input("Enter operator :")

if op == "+" :
    print(f"{num1} + {num2} :", num1 + num2)
elif op == "-" :
    print(f"{num1} - {num2} :", num1 - num2)
elif  op == "*" :
    print(f"{num1} * {num2} :", num1 * num2)
else :
     print(f"{num1} / {num2} :", num1 / num2)
     

