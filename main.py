n = int(input("Enter the length of the list: "))

l1 = []


for c in range(n):
    e = int(input("Enter an element to the list: "))
    l1.append(e)

print("The main list is :", l1)

l2 = [i for i in l1 if i%2 == 0]
print("The even numbers are: ", l2)

l3 = [x for x in l1 if x%2!=0 ]
print("The odd number on the list are: ", l3)