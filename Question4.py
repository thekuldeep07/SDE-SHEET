#Merge Two Sorted array
#Approach 1 
# take third array with size of arr1 + arr2 and put all elemnts of arr1 and arr2 into arr3 
# after that sort the array 
#T.C= O(NlogN) +O(n)+O(n)
#S.c = O(N)

#Better Approach 
#we will use insertion type algorithm
#we will traverse arr1 and compare the element with arr2[0] and if 
#elemnt is greater than we will swap both element and after that we will again sort arr2 

#T.C = O(N*M)

def sortInsertionAlgo(arr1 , arr2):
    for i in range(0,len(arr1)):
        if arr1[i] > arr2[0]:
            element = arr1[i]
            arr2[0],arr1[i]=arr1[i],arr2[0]
            
            j=1
            while j<len(arr2) and element>arr2[j]:
                arr2[j-1]=arr2[j]
                j+=1
            arr2[j-1]=element 
    print(arr1)
    print(arr2)        
#optimal Approach :- using GAP method
#we will find  gap by (len(Arr1)+len(Arr2))//2 we will always take cieling
#initially we will keep 1st pointer to 0 and 2nd pointer to gap and swap elemnt if gap pointer elemnt is greater 
#we will move both pointer by 1 
#and continue the process while gap is greater than 0

def findGap(gap):
    if gap<=1:
        return 0
    return (gap//2)  + (gap%2) 
def mergeUsingGap(arr1,arr2):
    n=len(arr1)
    m=len(arr2)
    gap=findGap(n+m)
    while gap>0:
        i=0
        while i+gap<n:
            if arr1[i] > arr1[i+gap]:
                arr1[i],arr1[i+gap]=arr1[i+gap],arr1[i]
            i+=1
        j= gap-n if gap > n else 0
        while i<n and j<m:
            if arr1[i] > arr2[j]:
                arr1[i],arr2[j]=arr2[j],arr1[i]
            i+=1
            j+=1
        if j<m:
            j=0
            while j+gap<m:
                if arr2[j]>arr2[j+gap]:
                    arr2[j],arr2[j+gap]=arr2[j+gap],arr2[j]
                j+=1
        gap=findGap(gap) 
    print(arr1)
    print(arr2)
     
                     
              
arr1=[3,5,9]
arr2=[0,1,4,7,90]      
sortInsertionAlgo(arr1,arr2)
mergeUsingGap(arr1,arr2)

      
                            