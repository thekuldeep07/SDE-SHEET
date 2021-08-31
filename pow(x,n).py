# Qusetion :- pow(x,n)

# method1 :- use a loop from 1 to n and do operation ans = ans*x
# T.C = O(N)
# for edge case as to convert -n to +n please convert it into long type


# method2:- 

def findPow(x:float,n:int):
    ans=float(1.0)
    nn=n
    if nn<0:
        nn=-1*nn
    while nn>0:
        if nn%2==0:
            x=x*x
            nn=nn//2
        else:
            ans=ans*x
            nn-=1
    if n < 0:
        ans = (float)(1.0)/float(ans)       
    return ans  
print(findPow(2,-31))      

