def longprefsuf(pattern,lps):
	ln=0
	i=1
	m=len(pattern)
	lps[0]=0
	while i<m:
		if (pattern[i]==pattern[ln]):
			ln+=1
			lps[i]=ln
			i+=1
		else:
			if (ln==0):
				lps[i]=0
				i+=1
			else:
				ln=lps[ln-1]
	return lps
				
def kmp(pattern,text):
	n=len(text)
	m=len(pattern)
	lps=[0]*m
	lps=longprefsuf(pattern,lps)
	i=0
	j=0
	while i<n:
		if (pattern[j]==text[i]):
			i+=1
			j+=1
		if (j==m):
			print "found index " + str(i-j)
			
			j=lps[j-1]
		elif (i<n and pattern[j]!=text[i]):
			if (j!=0):
				j=lps[j-1]
			else:
				i+=1
			


#pattern='aabaacaabaa'
pattern="AABA"
m=len(pattern)
text="AABAACAADAABAAABAA"
kmp(pattern,text)
