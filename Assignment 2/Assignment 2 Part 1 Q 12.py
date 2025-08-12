# part 1 Q 12

c=int(input("Enter the temperature in Celsius :"))

if c < 0 :
    print(f"{c} is freezing temperature .")
elif 0 < c < 26 :
    print(f"{c} is moderate temperature .")
else :
    print(f"{c} is hot  temperature .")

