#given a set of coins like 1,5,6,8 and value 11 
#find the min no. of coins to achieve value 11
#make a dp table with m rows and n cols
#m is the length of coin array and n is Value
coins=[1,5,6,8]
V=11
m=len(coins)
table = [[0 for col in range(V+1)] for row in range(m)]
for i in range(m):
	for j in range(V+1):
		if (j>=coins[i]):
			table[i][j]=min(table[i-1][j],1+table[i][j-coins[i]])
			if (table[i][j]==0):
				table[i][j]=j
		else:
			table[i][j]=table[i-1][j]

#print table[m-1][V]
#backtracking
i=m-1
j=V
result=[]
while j>0:
	if (table[i-1][j]==table[i][j]):
		i=i-1
		#result.append(coins[i])
	else:
		j=j-coins[i]
		result.append(coins[i])
print result		
