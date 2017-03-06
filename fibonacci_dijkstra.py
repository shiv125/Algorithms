fib={0:1,1:1}
def fun(n):
    
    if n==0:
        return 0
    if n==1:
        return 1
    if n in fib:
        return fib[n]
    if n%2==0:
       fib[n]= (2*fun(n//2-1)+fun(n//2))*fun(n//2)%1000
       return fib[n]
    if n%2!=0:
        fib[n]= ((fun((n-1)/2))**2+(fun((n+1)/2))**2)%1000
        return fib[n]
        

