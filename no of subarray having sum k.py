# Given an unsorted array of integers, find the number of subarrays having sum exactly equal to a given number k.

# Examples: 

# Input : arr[] = {10, 2, -2, -20, 10}, 
#         k = -10
# Output : 3
# Subarrays: arr[0...3], arr[1...4], arr[3..4]
# have sum exactly equal to -10.

# Naive Solution – 
# A simple solution is to traverse all the subarrays and calculate their sum. If the sum is equal to 
# the required sum then increment the count of subarrays. 
# Print final count of subarray.

#optimal Approach 
# we will use the property x+k = sum that we have used in Find all subarray with xor k problem

def findSubarrayWithSumK(nums,k):
    ans=0
    sum=0
    hm={}
    n=len(nums)
    for i in range(n):
        sum+=nums[i]
        if sum == k:
            ans+=1
        x=sum-k
        if x in hm:
            ans+=hm[x]
        
        hm[sum]=hm.get(sum,0)+1   
    return ans

if __name__ =="__main__":
    nums=[9, 4, 20, 3, 10, 5]     
    print(findSubarrayWithSumK(nums,33))    
