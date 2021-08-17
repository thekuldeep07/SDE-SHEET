# ouestion :- search in a 2d matrix where the first index of every row is greater than the last index of previus ResourceWarning

# ex :-  [
#     [1,3,5,7],
#     [10,11,16,20],
#     [23,30,34,50]
# ]
# target = 3:
#     op = True


# Approach 1 :- using linear search
# t.c =O(n x m)    

#appproach 2:- using binary search for every row
# t.c = O(n x log m)


#approach 3 :- best approach if the row and coloumn both are sorted , but better approach if only rows are sorted
#if both row and columns are sorted we will start looking for the element from the last element of first row if the searching elemnt is greater then we will 
#move downwards in the column and if the it is smaller then we will move left , we will continue this until we find the elemnt or the reach the boundary of array

# def searchIn2dmatrix(nums,ele):
#     n=len(nums) 
#     m=len(nums[0])
#     i=0
#     j=m-1
#     while i < n and j>=0:
#         if nums[i][j]==ele:
#             return 1
#         if nums[i][j]>ele:
#             j=j-1
#         else:
#             i +=1
#     return 0        
 
# li=[
#     [1,3,5,7],
#     [10,11,16,20],
#     [23,30,34,50]
# ]  
# print(searchIn2dmatrix(li,7))       

# t.c = O(n+m)   

# method 4 :- optimla approach if only rows are sorted i.e last index of row is smaller than first index of another row , and all the elemnt in 
# particular row are sorted    
# we will treat the whole array as 1-d array and will do binary search on it 
# suppose there are n elemnts in array then the index of ith element in 2-d array will be
# row = i/m       col= i%m
# t.c= log(n*m)

def searchMatrix(matrix,target):
    if len(matrix) == 0:
        return False
    n=len(matrix)
    m=len(matrix[0])
    lp=0
    hp=(n*m)-1
    while lp <= hp:
        mid=lp+(hp-lp)//2
        if(matrix[mid//m][mid%m]==target):
            return True
        if(matrix[mid//m][mid%m]<target):
            lp=mid+1
        else:
            hp=mid-1
    return False            
        
li=[
    [1,3,5,7],
    [10,11,16,20],
    [23,30,34,50]
]  
print(searchMatrix(li,7))         