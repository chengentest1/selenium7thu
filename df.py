demo=['aycc','kh','llc','u','l']
h=-3
f=[]
a=""
for i in range(len(demo)):
    if i<3:
        u=demo[i][i+h]
    else:
        u=demo[i]
    f.append(u)
for u in range(len(f)):
    b=f[len(f)-1-u]
    a=a+b
print(a.upper())
