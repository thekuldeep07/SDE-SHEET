#find duplicate in array of N+1 Integer 
#input = [1,3,4,2,2]
#Output = 2 

#Method 1
# We can sort the array at its place and then itrate it and look for  case where element at index i == element at index i+1 
#and then  print the element

#Time complexity = O(NLogN)(mergesort) + O(N)(iterating)
#Space = O(N)

#Method 2 
#we can use hashmap and store frequency of numbers as value for keys(elemnt of array )
#then we will iterate the hashmap and look for key having value greater than 2 , those keys will be duplicates
#Time Complexity = O(N){putting values into hashmap}+O(N)(iterating hashmap)
#space COmplexity = O(N)


#MEthod 3 
#we can  use the array as hashmap as size of array is N+1 and it will contains element only from 1 to N there all the elements will 
#be accessibele as Index 
#we will iterate the array 
#for(i=0 to N)
#after this we will be changing the value at arr[arr[i]] as -ve
#and will continue iteration and during iteration if got -ve value then the index of that value is duplicate no.


#method 3 (Optimal approach) using floyds cycle algorithm
#T.C = O(N)

def findDuplicate(arr):
    if(len(arr)<=1):
        return 0
    sp=arr[0]
    fp=arr[arr[0]]
    while(sp!=fp):
        sp=arr[sp]
        fp=arr[arr[fp]]
    fp=0
    while(sp!=fp):
        sp=arr[sp]
        fp=arr[fp] 
    return sp

     
arr=[2,5,9,6,9,3,8,9,7,1]
print(findDuplicate(arr))

