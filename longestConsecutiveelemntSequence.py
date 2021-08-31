# Question : 
# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

# You must write an algorithm that runs in O(n) time.

 

# Example 1:

# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 

# approach 1 :- first sort the array and the iterate through the array to find the longest subsequence length
# t.c = O(nlogn) + O(n)

# #optimal approach :- store all the elemnts of the array into a set and the iterate the array if for ith element , ith-1 is in set then 
# continue otherwise increase the counter and search for ith+1 in set 


def findSubsequence(nums):
    s=set()
    for i in nums:
        s.add(i)
    longestStreak=0    
    for i in nums:
        if i-1 not in s:
            currentNum=i
            currentStreak=1
            while currentNum+1 in s:
                currentStreak+=1
                currentNum+=1
            longestStreak=max(longestStreak,currentStreak)
    return longestStreak
       
nums = [100,4,200,1,3,2]
print(findSubsequence(nums))            
            

