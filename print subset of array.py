# Question to print all subsets of array
# input = [a,b,c]
# output = [],[a],[b],[c],[a,b],[a,c],[b,c],[a,b,c]

# method 1 :- taking help from binary reprsentation as there will be 2^n subsests and 
# for every binary reprsentation of no from 0 to 2^n we can find set bits and print ith index of arr


# import math
# def printSubsets(arr):
#     n=len(arr)
#     subet=[]
#     limit= int(math.pow(2,n))
#     for i in range(0,limit):
#         ans=[]
#         for j in range(0,n):
#             if(i & (1<<j)):
#                 ans.append(arr[j])
#         subet.append(ans)
#     print(subet)

# a=[1,2,3]
# printSubsets(a)   

# t.c=O(n*2^n)

# method 2 :- using backtracking 

def subset(nums):
    res=[]
    n=len(nums)
    def backtrack(curr,pos):
        res.append(curr[:])
        if pos==n:
            return
        for i in range(pos,n):
            curr.append(nums[i])
            backtrack(curr,i+1)
            curr.pop()
    backtrack([],0)
    print(res) 
a=[1,2,3]
subset(a)       
             
                