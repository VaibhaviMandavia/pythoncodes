#find the missing number from an array of first n numbers

x = int(input("enter number of elements : "))
print("enter "+str(x)+" elements : ")
lst = []
ans = 0
n = x + 1
for i in range(0,x):
    y = int(input())
    lst.append(y)
if all(item >= 0 for item in lst) == True:
    res = n*(n+1)/2
else :
    res = -(n*(n+1)/2)
ans = sum(lst)
misnum = res - ans
print("missing number is : ",int(misnum))
