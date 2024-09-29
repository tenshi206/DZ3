a=int(input("введите начальный член: "))
r=int(input("введите знаменатель: "))
n=int(input("введите количество членов: "))
s=a
for i in range(a,n+2):
    s=a*(r**(i-1))
    print(s)
