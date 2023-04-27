n=int(input("Enter n"))
a=0
b=1
c=1
print(a)
print(b)
print(c)
for i in range(1,n+1):
    d=b+c
    b=c
    c=d
    print(d)
