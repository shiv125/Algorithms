#given a set of points P={(x1,y1),(x2,y2),(x3,y3),...,(xn,yn)}
#where x1,x2..,xn are in sorted order
#consider a segment {pi,pi+1,..,pj}
#penalties
#1. no. of segments into which we partition P, times a fixed, given multiplier C>0
#2. for each segment, the error value of optimal line through that segment
#line is y=ax+b
#find partitions with minimum penalty
def SegmentedLeastSquares(n):
	M=[0]*n
	#to calculate e(i,j)
	E=[[0]*n]*n
	for j in range(1,n):
		t1=0
		t2=0
		t3=0
		t4=0
		templen=0
		for i in range(j):
			templen=j-i+1
			t1+=x[i]*y[i]
			t2+=x[i]
			t3+=y[i]
			t4+=x[i]**2
		a=(templen*t1-t2*t3)/(templen*t4-t2**2)
		b=(t3-a*t2)/templen
		for i in range(j):
			E[i][j]+=(y[i]-a*x[i]-b)**2
	for j in range(n):
		temp=[]
		for i in range(j+1):
			temp.append(E[i][j]+C+M[i-1])
		M[j]=min(temp)
	return M[n-1]
			
C=5
P=[[1,2],[2,4],[3,0],[4,8],[5,7]]
x=[1,2,3,4,5]
y=[2,4,0,8,7]


SegmentedLeastSquares(5)
print SegmentedLeastSquares(5)
