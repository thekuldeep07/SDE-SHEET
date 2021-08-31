#Printing Nth row of pascal triangle

#Approach 1 :-

# creating whole pascal triangle upto Nth row and then printing nth row
#If we take a closer at the triangle, we observe that every entry is sum 
# of the two values above it. So we can create a 2D array that stores previously generated values. 
# To generate a value in a line, we can use the previously stored values from array. 

#T.C = O(n^2)
#S.C=O(n^2)

def printPascalTriangleBy2dArray(n):
    arr= [[0 for i in range(n)]for y in range(n)]
    for i in range(0,n):
        for j in range(0,i+1):
            if j==0 or i==j:
                arr[i][j]=1
                print(arr[i][j],end=" ")
            else:
                arr[i][j]=(arr[i-1][j-1]+arr[i-1][j])
                print(arr[i][j],end=" ")
        print()        


#best approach (O(n^2) and O(1))
def printPascalBynCr(n): 
    for i in range(1,n+1):
        c=1
        for j in range(1,i+1):
            print(c,end=" ")
            c= int(c* (i-j)//j);
        print()        
#printPascalBynCr(5)                      
# printPascalTriangleBy2dArray(5)

#printNowthR
def printNthrow(n):
    curr=1
    print(curr,end=' ')
    for i in range(1,n):
        next=(curr*(n-i))//i
        print(next,end=" ") 
        curr=next 
printNthrow(5)            
        