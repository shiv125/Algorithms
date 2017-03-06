import math
class Heap:
	def __init__(self):
		self.heap=[]
		self.heapsize=0
	def parent(i):
		return i/2
	def left(self,i):
		if 2*i<self.heapsize:
			return 2*i
		else:
			return -1
	def right(self,i):
		if 2*i+1<self.heapsize:
			return 2*i+1
		else:
			return -1
	def swap(self,i,j):
		temp=self.heap[i]
		self.heap[i]=self.heap[j]
		self.heap[j]=temp
	#build max heap
	def BuildMaxHeap(self,Arr):
		self.heapsize+=len(Arr)
		self.heap+=Arr
		for i in range(int(math.floor(len(Arr)/2)),-1,-1):
			self.MaxHeapify(i)
	def MaxHeapify(self,i):
		l=self.left(i)
		r=self.right(i)
		largest=i
		if l!=-1:
			if l<=self.heapsize and self.heap[l]>self.heap[i]:
				largest=l
		if r!=-1:
			if r<=self.heapsize and self.heap[r]>self.heap[largest]:
				largest=r
		if largest!=i:
			self.swap(i,largest)
			self.MaxHeapify(largest)
	def insert(self,key):
		self.heapsize+=1
		self.heap.append(key)
		self.MaxHeapify(self.heapsize)
	def ExtractMax(self):
		k=self.heap[0]
		self.heap[0]=self.heap[self.heapsize-1]
		self.heapsize-=1
		self.MaxHeapify(0)
		return k
	def heapSort(self,Arr):
		self.BuildMaxHeap(Arr)
		y=[]
		for i in range(self.heapsize-1,-1,-1):
			y.append(self.heap[0])
			self.swap(i,0)
			self.heapsize-=1
			self.MaxHeapify(0)
		return self.heap

Arr=[2,1,3,0,1,3,12,5,8,7,2,1,12]
t=Heap()
t.BuildMaxHeap(Arr)
t.insert(4)
print t.ExtractMax()
