n=int(input("Enter the number of elements:"))
print("Enter the elements(in ascending order):")
a=[]
t=0
for i in range(n):
    t=int(input())
    a.insert(i,t)
ele=int(input("Enter the element to be found:"))
l=0
h=n-1
while(h>=l):
    m=(h+l)//2
    if(a[m]==ele):
        print(ele,"is found in the postion",m+1,"of the set of elements.")
        break
    elif(a[m]<ele):
        l=m+1
    else:
        h=m-1
if h<l:
    print(ele,"is not found in the set of elements.")
