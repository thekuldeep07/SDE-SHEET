# Question :- print next permutation
#input = [1,3,2]
#output = [2,1,3]

# method1:- find all permutation and iterate through them and print next permutation
# t.c = O(n)*n!


#optimal method
# linearly traverse the array from backward and look for the element at ith position such that arr[i]< arr[i+1]
# after that again traverse the array and find element at jth position such that it should be greater than arr[i]
# swap ith and jth element 
# after this reverse the element after ith position
# t.c = O(n)

def nextPermutation(nums):
    i=len(nums)-2
    while i >=0:
        if nums[i]<nums[i+1]:
            break
        i-=1
    if i >=0 :
        j=len(nums)-1
        while nums[i]>=nums[j]:
            j-=1
        swap(nums,i,j)
    reverse(nums,i+1,len(nums)-1)
    print(nums)

def swap(nums, i,j):
    nums[i],nums[j]=nums[j],nums[i]

def reverse(nums,i,n):
    while (i<n):
        swap(nums,i,n)
        i+=1
        n-=1
             

q=[3,2,1]
nextPermutation(q)                   
        
            
