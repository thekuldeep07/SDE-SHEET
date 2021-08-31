#print permutation of string

# method1 = Recusrssion
# tc=n*n!
def permutation(question,ans=""):
    if len(question)==0:
        print(ans)
    for i in range(len(question)):
        lp=question[0:i]
        rp=question[i+1:]
        nq=lp+rp
        permutation(nq,ans+question[i])
st="ABC" 
permutation(st)  

# method2 = backtracking
# tc=n*n! 

def permute(a,l,r):
    if l==r:
        print(a)
    for i in range(l,r):
        a[l],a[i]=a[i],a[l]
        permute(a,l+1,r)
        a[l],a[i]=a[i],a[l]
k=["a","b","c"]      
permute(k,0,len(k))        
            