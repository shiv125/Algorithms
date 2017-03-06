def egcd(a,b):
	if b==0:
		return 1,0,a
	else:
		x,y,d=egcd(b,a%b)
		return y,x-(a/b)*y,d

x=10
y=4
print egcd(x,y)
