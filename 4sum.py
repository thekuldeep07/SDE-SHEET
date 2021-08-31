# Question :- 4SUM
# example:-
# nums=[1,0,-1,0,-2,2] target=0
# answer=[
#     [-1,0,0,1],
#     [-2,-1,1,2],
#     [-2,0,0,2]
# ]

#Approach1 :- sort the Array , then use 3 pointer nad then binary search and after that store all the unique quads in set.
# sort the array then put i pointer on 0 initially and j at i+1 and k at j+1
# now look for target - nums[i]+nums[j]+nums[k] in the remaining array using binary search
# t.c= o(nlogn) + O(n3logn)

#approach2 :- to sort the array at first , and at the next use two pointers such that i =0 inintialy and j =i+1 , 
# perform two pointer approach in the remaining array 
# note:- jump the duplicates in every loop iterations
# t.c=O(n3)
# s.c=o(1)

from typing import List

class Solution:
    def fourSum(self, nums, target) :
        res =[]
        n =len(nums)
        if n <4:
            return ans
        nums.sort()
        for i in range(n-3):
            if i> 0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1,n-2):
                if j >i+1 and nums[j]==nums[j-1]:
                    continue
                newTarget=target-nums[i]-nums[j]
                left=j+1
                right=n-1
                while left < right:
                    currSum=nums[left]+nums[right]
                    if currSum < newTarget:
                        l=nums[left]
                        while left < right and nums[left]==l:
                            left+=1
                    elif currSum > newTarget :
                        r=nums[right]
                        while left < right and nums[right]==r:
                            right-=1
                    else:
                        li=[nums[i],nums[j],nums[left],nums[right]]
                        res.append(li)
                        while left < right and nums[left]==li[2]:
                            left+=1
                        while left < right and nums[right]==li[3]:
                            right-=1          
        return res                     
        

ob = Solution()
print(ob.fourSum([2,2,2,2,2],8))        