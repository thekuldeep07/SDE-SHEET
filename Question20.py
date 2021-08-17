# Question :- A robot islocated at the top-left corner of m x n grid.
# the robotb can only move right and down at any point of time. the robot is trying to reach the
# bottom-right of the grid 
# How many possible unique paths are there

# brute force:- use recursion to find all the possible paths
# t.c= exponential

# def findPosssiblePaths(i,j,m,n):
#     if i==m-1 and j==n-1:
#         return 1
#     elif i>=m or j>=n:
#         return 0
#     else:
#         return findPosssiblePaths(i+1,j,m,n) + findPosssiblePaths(i,j+1,m,n)
    



# grid=[[0 for i in range(3)]for i in range(2)]
# print(findPosssiblePaths(0,0,len(grid),len(grid[0])) )


#better approach : we can use dynamic programming to store result of sub-problem
# t,c = O(n x m) as there will be not more than O(nxm) repetiiotion of probblem as there will be only n x m combinnation
# def findPosssiblePaths(i,j,m,n,hm):
#     if i>=m or j>=n:
#         return 0
#     elif i==m-1 and j==n-1:
#         return 1
#     elif(hm[i][j]!=0):
#         return hm[i][j]
#     else:
#         hm[i][j]=findPosssiblePaths(i+1,j,m,n,hm) + findPosssiblePaths(i,j+1,m,n,hm)
#         return hm[i][j]
    



# grid=[[0 for i in range(3)]for i in range(2)]
# m=len(grid)
# n=len(grid[0])
# print(findPosssiblePaths(0,0,m,n,grid))

# optimal approach: first we will right all the path and then observe that for 2 x 3 problem grid , we always have 

# no. of right turn = 3-1
# no of down turn as = 2-1
# Total no of steps are = n-1 + m-1 = (n+m)-2
# so for 2x 3 grid we will have 3 steps to reach the destination , comprises of n-1 right steps and m-1 down 
# we have to fill three empty spaces _ _ _ 
# so if we are able to choose 1 down or 2 right then we can figure out all the paths
# ex R R _ , _ R R , R _ R
# do we can find the combonotrics for (m+n-2)Cm-1 or (m+n-2)C3n-1

# T.c = O(m-1) or O(n-1)

def findUniquePaths(m,n):
    noSteps=m+n-2
    r=m-1
    res=1
    for i in range(1,r+1):
        res=res*(noSteps-r+i)//i
    return res    

grid=[[0 for i in range(3)]for i in range(2)]
m=len(grid)
n=len(grid[0])
print(findUniquePaths(m,n))
