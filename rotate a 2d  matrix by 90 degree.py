#rotate a 2d n*n matrix by 90 degree clockwise

# method 1 :
#     take a new 2d matrix and insert every ith row as n-1-ith complex
#     t.c = o(n^2) = s.c


# mehtod 2 :
#     transpose the matrix first and then reverse the lement of every row    

# method 3 :
#     #every square matrix will have n//2 cycles \, we will swap element in those cycles


def rotateMatrix(mat):
    n=len(mat)
    for i in range(n//2):
        for j in range(i,n-1-i):
            temp=mat[i][j]
            mat[i][j]=mat[n-1-j][i]
            mat[n-1-j][i]=mat[n-1-i][n-1-j]
            mat[n-1-i][n-1-j]=mat[j][n-1-i]
            mat[j][n-1-i]=temp
    print(mat)        
mat=[[1,2,3],[4,5,6],[7,8,9]]
rotateMatrix(mat)
            
    