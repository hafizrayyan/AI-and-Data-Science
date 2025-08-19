l=[32,54,66,11,77,10,90]
l.pop()<20
print(l)

l.sort()
print(l)

l.sort(reverse=True)
print(l)
b= len(l)
average = sum(l) / b
print("The average value of list is",average)
