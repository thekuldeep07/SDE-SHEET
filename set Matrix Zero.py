# Set MAtrix Zero 
# input = [
#     [0,1,2,0],
#     [3,4,5,2],
#     [1,3,1,5]
# ]
# output=[
#     [0,0,0,0],
#     [0,4,5,0],
#     [0,3,1,0]
# ]
#Brute Force :- traverse 2d Array and for every arr[i][j]==0 , make ith row element nad jth column elemnt = -1 , again traverrese the row 
#and for every -1 encountered make that elemnt as 0
#T.C = O(n*m)*O(n+m)
# s.c=1

#better : - using row and coloumn hashmap
#T.C = O(n*m)+O(n*m)
# s.c=O(n)+O(m)

#optimal approach
#use first row and first column as hashmap , use two variable row_flag and col_flag for status of first row and col

def setMatrixZero(arr):
    row_flag=0
    col_flag=0
    for i in range(0,len(arr)):
        for j in range(0,len(arr[0])):
            if i==0 and arr[i][j]==0:
                row_flag=True
            if j==0 and arr[i][j]==0:
                col_flag=True
            if arr[i][j]==0:
                arr[0][j]=0
                arr[i][0]=0
    for i in range(1,len(arr)):
        for j in range(1, len(arr[0])):
            if arr[0][j]==0 or arr[i][0]==0:
                arr[i][j]=0
    if row_flag:
        for i in range(0,len(arr[0])):
            arr[0][i]=0
    if col_flag:n
        for i in range(0,len(arr)):
            arr[i][0]=0

arr=  [[0,1,2,0],[3,4,5,2],[1,3,1,5]]

setMatrixZero(arr)    
print(arr)
                                             
            


