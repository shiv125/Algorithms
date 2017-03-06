import math
f=[0 for i in range(100002)]
f[0]=0
f[1]=1
for i in range(100000):
    f[i+2]=f[i]+f[i+1]
n=1000
#fun(n)
print math.log(f[99999], 10)
