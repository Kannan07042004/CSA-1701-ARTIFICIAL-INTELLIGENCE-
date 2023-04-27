a=[[5,8],
    [2,4]]
b=[[2,7],
     [4,6]]
c=[[0,0],
    [0,0]]
for i in range(len(a)):
    for j in range(len(a[0])):
        c[i][j]=a[i][j]+b[i][j]
for k in c:
    print(k)
