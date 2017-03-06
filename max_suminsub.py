#maximum sum increasing subsequence 
#given a array, find the maximum sum in increasing subsequence
#this problem is similar to longest increasing subsequence
#make two arrays, one to store max values and another to store actual sequence
#input_=[2,3,1,7,3,8,4]
input_=[4,6,1,3,8,4,6]
n=len(input_)
max_value=[0]*n
actual_seq=[0]*n
for i in range(n):
	max_value[i]=input_[i]
for i in range(n):
	actual_seq[i]=i
for i in range(1,n):
	for j in range(i):
		if (input_[j]<input_[i]):
			t=max_value[i]
			max_value[i]=max(max_value[i],max_value[j]+input_[i])
			if (max_value[i]!=t):	
				actual_seq[i]=j
maxvalue=max(max_value)
indexOfmax=max_value.index(maxvalue)
print maxvalue
resultant=[]
print actual_seq
while True:
	resultant.append(input_[indexOfmax])
	indexOfmax=actual_seq[indexOfmax]
	if (indexOfmax==0):
		break
print resultant

