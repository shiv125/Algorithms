#find convex hull in O(n^2) #best O(nh)

def direction(p,i,q):
	r=(i[1]-p[1])*(q[0]-i[0])-(i[0]-p[0])*(q[1]-i[1])
	if r<0:
		return -1
	else:
		return 0
def jarvis(points):
	n=len(points)
	if n<3:
		return 
	hull=[]
	#choose left most point
	lf=0
	for i in range(n):
		if points[i][0]<points[lf][0]:
			lf=i
	p=lf
	tr=0
	while p!=lf or tr<1:
		hull.append(points[p])
		q=(p+1)%n
	#choose most counterclock wise point
		for i in range(n):
			if (direction(points[p],points[i],points[q])==-1):
				q=i
		p=q
		tr+=1
	return hull


points=[[0,3],[2,2],[1,1],[3,0],[0,0],[3,3],[2,1]]
print jarvis(points)
