# part 1 Q 9
# number is divisible by 2 or 3 or both
num = int(input("Enter the number :"))

x = num % 2
y = num % 3 

if x == 0 and y == 0 :
    print(f"{num} is divisible by both 2 and 3 .")
elif x == 0 :
    print(f"{num} is divisible by 2 .")
elif y == 0 :
    print(f"{num} is divisible by 3 .")
else :
    print(f"{num} is not divisible by both 2 and 3 .")
        


     

