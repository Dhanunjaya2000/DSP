##program to perform append operation on two lists
a=[1,2,3,4,5,6,7,8,9]
b=[4,5,6,7]
c=[16,76,90,23,56,34,78,65,77,99,101]
print("Here three pre defined lists are a,b and c",a,"\t,",b,"\t",c)
for i in range(0,len(a)):
    b.append(a[i])
print("the new list formed is=",b)
print("now with condition")
for i in range(0,len(c)):
    if(c[i]%2==1):
        a.append(c[i])
print("new appended list with some condition",a)
print("***Thank you***")