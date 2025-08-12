# part 1 Q3
# which numbe ris larger from thre numbers

num1= int(input("Enter the first number :"))
num2= int(input("Enter the second number :"))
num3= int(input("Enter the third number :"))

if num2 < num1 > num3 :
    print(f"{num1} is larger than {num2} and {num3}")
elif num1 < num2 > num3  :
    print(f"{num2} is larger than {num1} and {num3}")
else :
    print(f"{num3} is larger than {num1} and {num2}")
          


