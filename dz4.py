n=int(input("введите колл во дней "))
a=int(input("введите курс "))
c=int(input("введите процент изменения "))
s=0
for i in range (0,n):
    s= a*i*c
print (s)
