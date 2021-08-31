# Count the number of subarrays having a given XOR
# Given an array of integers arr[] and a number m, count the number of subarrays having XOR of their elements as m.
# Examples: 

# Input : arr[] = {4, 2, 2, 6, 4}, m = 6
# Output : 4
# Explanation : The subarrays having XOR of 
#               their elements as 6 are {4, 2}, 
#               {4, 2, 2, 6, 4}, {2, 2, 6},
#                and {6}

# approach 1 :- A Simple Solution is to use two loops to go through
# all possible subarrays of arr[] and count the number of subarrays having XOR of their elements as m. 

# t.c = O(n2)


# Efficient Approach:
# An Efficient Solution solves the above problem in O(n) time. Let us call the XOR of all elements in the range [i+1, j]
# as A, in the range [0, i] as B, and in the range [0, j] as C. If we do XOR of B with C, the overlapping elements in [0, i] 
# from B and C zero out, and we get XOR of all elements in the range [i+1, j], i.e. A. Since A = B XOR C, 
# we have B = A XOR C. Now, if we know the value of C and we take the value of A as m, we get the count of A as 
# the count of all B satisfying this relation. Essentially, we get the count of all subarrays having XOR-sum m for 
# each C. As we take the sum of this count overall C, we get our answer.

# 1) Initialize ans as 0.
# 2) Compute xorArr, the prefix xor-sum array.
# 3) Create a map mp in which we store count of 
#    all prefixes with XOR as a particular value. 
# 4) Traverse xorArr and for each element in xorArr
#    (A) If m^xorArr[i] XOR exists in map, then 
#        there is another previous prefix with 
#        same XOR, i.e., there is a subarray ending
#        at i with XOR equal to m. We add count of
#        all such subarrays to result. 
#    (B) If xorArr[i] is equal to m, increment ans by 1.
#    (C) Increment count of elements having XOR-sum 
#        xorArr[i] in map by 1.
# 5) Return ans.


def countArrayXorK(nums,k):
    ans=0
    xor=0
    n=len(nums)
    hm={}
    for i in range(0,n):
        xor=xor^nums[i]
        if xor == k:
            ans+=1
        y=xor^k
        if y in hm:
           
            ans+=hm[y]
        hm[xor]=hm.get(xor,0)+1     
    return ans      
        
if __name__ == '__main__':
    nums=[4,2,2,6,4]
    print(countArrayXorK(nums,6))
    
                
        
            
        
    