#This question contains solutions to max subarray sum problem
#[-2,1,-3,4,-1,2,1,-5,4]
#output = 6 


#naive Approach 
#to use two loop one for selecting starting element and inside loop for finding max sub 
#T.C = O(n^2)


#optimal Approach using Kadanes algo
#T.C = O(n)

from typing import List


def maxSubArray(nums:List[int]) -> int:
        if(len(nums)==1):
            return nums[0]
        
        max_so_far=nums[0]
        max_ending_here=nums[0]
        
        for i in range(1,len(nums)):
            max_ending_here=max(nums[i],max_ending_here+nums[i])
            if(max_ending_here>max_so_far):
                max_so_far=max_ending_here
        return max_so_far

print(maxSubArray([-3,5,-8,2,4,-1]))
     