# find pairs of numbers whose sum equals to a given number

list1 = [] 
list2 = []
x = int(input("enter the number of elements : "))
for i in range(0,x):
    y = int(input())
    list1.append(y)
value = int(input("enter sum value : "))
for i in range(0,len(list1)):
    temp = value-list1[i]
    if temp in list1:
        list2.append((list1[i],temp))
pairs = set(list2)
pairs = set((a,b) if a<=b else (b,a) for a,b in pairs)
print(pairs)
         

