# Given an array of integers, find the length of the longest sub-array with a sum that equals 0.

# Examples: 

# Input: arr[] = {15, -2, 2, -8, 1, 7, 10, 23};
# Output: 5
# Explanation: The longest sub-array with 
# elements summing up-to 0 is {-2, 2, -8, 1, 7}

# BruteForce:- This involves the use of brute force where two nested loops are used. 
# The outer loop is used to fix the starting position of the sub-array, and the inner loop is used for
# the ending position of the sub-array and if the sum of elements is equal to zero, then increase the count

# Efficient Approach: The brute force solution is calculating the sum of each and every sub-array and checking whether 
# the sum is zero or not. Let’s now try to improve the time complexity by taking an extra space of ‘n’ length. 
# The new array will store the sum of all the elements up to that index. The sum-index pair will be stored in a hash-map. 
# A Hash map allows insertion and deletion of key-value pair in constant time. Therefore, the time complexity remains unaffected.
# So, if the same value appears twice in the array, it will be guaranteed that the particular array will be a zero-sum sub-array. 

def findLongestSubarrayZero(nums):
    ans=0
    hmp={}
    s=0
    for i in range(len(nums)):
        s+=nums[i]
        if s== 0:
            ans=i+1
        else:
            if s not in hmp:
                hmp[s]=i
            else:
                ans=max(ans,i-hmp[s])
    return ans

nums=[15, -2, 2, -8, 1, 7, 10, 23]
print(findLongestSubarrayZero(nums))
            
                
        