#Counting Inversion in array
#input = [9,6,8,4]
#output=[5]

#approach 1 :- traverse the array and for every i element again traverse the array from i+1 and
#if i<j and arr[i]>arr[j] then increase the counter
#t.c = O(n2) #s.c =1


#approach 2 :- 
#merge sort technque

def _mergeSort(arr):
    n=len(arr)
    tempArr=[0]*n
    return mergeSort(arr,tempArr,0,n-1)

def mergeSort(arr,tempArr,left,right):
    invCount=0
    if left< right:
        mid=left+((right-left)>>1)

        invCount+=mergeSort(arr,tempArr,left,mid)
        invCount+=mergeSort(arr,tempArr,mid+1,right)
        invCount+=merge(arr,tempArr,left,mid,right)
    
    return invCount


def merge(arr,tempArr,left,mid,right):
    i=left
    j=mid+1
    k=left
    inv_count=0
    c=0
    while i <= mid and j <= right:
     
        # There will be no inversion if arr[i] <= arr[j]
 
        if arr[i] <= arr[j]:
            tempArr[k] = arr[i]
            k += 1
            i += 1
        else:
            # Inversion will occur.
            tempArr[k] = arr[j]
            inv_count += (mid-i + 1)
            k += 1
            j += 1
 
    # Copy the remaining elements of left
    # subarray into temporary array
    while i <= mid:
        tempArr[k] = arr[i]
        k += 1
        i += 1
 
    # Copy the remaining elements of right
    # subarray into temporary array
    while j <= right:
        tempArr[k] = arr[j]
        k += 1
        j += 1
 
    # Copy the sorted subarray into Original array
    for loop_var in range(left, right + 1):
        arr[loop_var] = tempArr[loop_var]
         
    return inv_count

myList = [54,26,93,17,77,31,44,55,20]
n=_mergeSort(myList)
print(n)