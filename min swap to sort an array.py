# This problem contain solution to min swap in array problem
# ex:-
# [2,4,3,1,5]
# ans= 2

# method 1 :- using selection sort 
# t.c = O(n2)

# method 2 :- if no in array are from 1 to n and does not conatin any duplicate , we can traverse the array to 
# check whether the elemnt is not in correct position and if not we will swap it with its original position and increase the 
# counter

# def min_swaps(arr):
#     count =0
#     i=0
#     while i < len(arr):
#         if arr[i] != i+1:
#             while (arr[i] != i+1):
#                 arr[arr[i]-1],arr[i] = arr[i],arr[arr[i]-1]
#                 count+=1
#         i+=1        
#     print(count)            
# arr=[3,4,2,1,5]
# min_swaps(arr)


# we can also do this using hashmap , we will store all the element in  a list as pair of element and index , 
# we will sort he pair array on basis of first elemnt , the idea is that after sorting we will try to conver the pair array 
# to its original form
#also this methid can be used for any sequence
#t.c = O(nlogn)

def minSwaps(arr):
    n = len(arr)
    pl=[[arr[i],i] for i in range(n)]
    pl.sort(key= lambda i : i[0])
    count =0
    print(pl)
    for i in range(n):
        if pl[i][1] != i :
             while pl[i][1] !=i:
                 pl[pl[i][1]],pl[i]= pl[i],pl[pl[i][1]]
                 count+=1
    print(count)
arr=[3,4,2,1,5]
minSwaps(arr)







    
   
    
                 
                
                