#This progam Contains solution to  problem find repeating and missing element
#naive Approach :- first to sort array and traverse to find duplicate element at adjacent position and as 
# the element will be in range from 1to N we can look for missing element at coorect position if element at position i does not equal to i+1 it is the missing element
                #T.c = O(nlogn)+o(n)
#better Approach:- using hashMap                
#optimal Approach 1:- use sum of series and sum of square series to find solution

def findByseries(arr):
    n=len(arr)
    sum=(n*(n+1))//2
    sumSq=(n*(n+1)*((2*n)+1))//6
    for i in arr:
        sum=sum-i
        sumSq=sumSq-(i*i)   
    missingNo=0
    duplicateNo=0   
    missingNo=(sum+(sumSq//sum))//2
    duplicateNo=missingNo-sum
    print(missingNo)
    print(duplicateNo)

#Optimal Approach 3:- using XOR operation 
# initially we will assign xor as 0
# we will linearly traverse array and find xor of element in array 
# then we will do the XOR of result with XOR of no in range 1 to n
# then in the new result only xor of missing and duplicate no are left i.e X^Y=result it means that X and y are different
# we can surely say that there is a index where the bit of X and Y are different
# classify no into two bucket on basis of right most bit 
# classify no from range 1 to n on basis of right most bit
# xor these buckets and you will find repeating and missing No.  

def findByXor(nums):
    n=len(nums)
    x=0
    y=0
    xor=0
    for i in nums:
        xor=xor^i
        
    for i in range(1,n+1):
        xor=xor^i
    
    setBit = xor &  (~(xor-1))  
    for i in arr:
        if setBit & i :
            x=x^i
        else:
            y=y^i
    for i in range(1,n+1):
        if setBit&i:
            x=x^i
        else:
            y=y^i
    print(x)
    print(y)            

arr=[1,2,4,4,5]
findByseries(arr)
findByXor(arr) 
    
    
        