n=int(input("введите число: "))
s=0
a=1
b=1
for i in range (1,n):
    s +=i
    a *= i
    b /= s/n
print (s,a,b)

    
