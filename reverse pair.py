# Question : - find reverse pair in array such that for reverse pair(i,j) , 0<=i<=j<nums.length and nums[i]>2*nums[j]

# example1:- [1,3,2,3,1]
# output=2

# Approach 1 :- using two nested  loop
# t.c = (On2)



#approach 2 : using merge sort




def findReversePair(nums):
    n=len(nums)
    rc=0
    tempArr=[0]*n
    rc= mergeSort(nums,tempArr,0,n-1)
    return rc    

def mergeSort(nums,tempArr,left,right):
    rc=0
    if left < right:
        mid=left+((right-left)>>1)
        rc+=mergeSort(nums,tempArr,left,mid)
        rc+=mergeSort(nums,tempArr,mid+1,right)
        rc+=merge(nums,tempArr,left,mid,right)
    return rc

def merge(nums,tempArr,left,mid,right):
    i=left
    k=left
    j=mid+1
    c=0
    while i <=mid and j <=right:
        if nums[i]>2*nums[j]:
            c=c+(mid-i+1)
            j+=1
        else:
            i+=1
                
    i=left
    j=mid+1
    while i <= mid and j <= right:
         
        # There will be no inversion if nums[i] <= nums[j]
 
        if nums[i] <= nums[j]:
            tempArr[k] = nums[i]
            k += 1
            i += 1
        else:
            # Inversion will occur.
            tempArr[k] = nums[j]
            k += 1
            j += 1
 
    # Copy the remaining elements of left
    # subnumsay into temporary numsay
    while i <= mid:
        tempArr[k] = nums[i]
        k += 1
        i += 1
 
    # Copy the remaining elements of right
    # subnumsay into temporary numsay
    while j <= right:
        tempArr[k] = nums[j]
        k += 1
        j += 1
 
    # Copy the sorted subnumsay into Original numsay
    for loop_var in range(left, right + 1):
        nums[loop_var] = tempArr[loop_var]
         
    return c


ques=[1,3,2,3,1]
print(findReversePair(ques))
    
        
    
    