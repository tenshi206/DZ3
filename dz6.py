n=int(input("введите год"))
p=int(input("введите начальную численность населения "))
r=int(input("введите процент прироста "))
s=0
for i in range (0,n):
    s= n*p*r
print (s)
