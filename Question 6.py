#This question contains solution to problem of merging sub intervals
#Input :- [[1,3][2,6],[8,10],[9,13],[14,18]]
#output :- [[1,6],[8,13],14,18]

#Approach 1 : - If the array is not sorted then sort the array  on basis of first element
#traverse the array and look 2for the all other merging interval for ith element , after merging put it into another list
#T.Cc = O(NlogN) +O(n^2)(
#S.C= O(n)



#Approach 2 : - If the array is not sorted then sort the array  on basis of first element
#take the first elemnt as pair
#traverse the array and keep merging the lement until it is merging with pair , and if the traversed lement is not merging with pa
#store pair in stack and update the value of pair with traversed element
#T.Cc = O(NlogN) +O(n^2)(
#S.C= O(n)


def mergeSubInterval(arr1):
    if len(arr1)<=1:
        return arr1
    pair=arr1[0]
    stack=[]
    arr1.sort(key=lambda x:x[0])
    print(arr1)
    for element in arr1:
        if element[0]<=pair[1]:
            pair=[pair[0],max(element[1],pair[1])]
        else:
            stack.append(pair)
            pair=element
    stack.append(pair)            
    print(stack)      

arr1=[[1,3],[2,6],[8,10],[9,13],[14,18]]

mergeSubInterval(arr1)      
            
                
    