# Question :- find the majority element i.e which appear more than n//2 times

# method1:- using two nested loops
# o(n2)

# method2:- using hashmap
# O(n)

# mrthod 3 :- using moore voting algorithm


def findMajority(nums):
    maj_index=0
    count=0
    for i in range(len(nums)):
        if nums[i]== nums[maj_index]:
            count+=1
        else:
            count-=1
        if  count==0:
            count=1
            maj_index=i
    c=0        
    for i in range(len(nums)):
        if nums[i]==nums[maj_index]:
            c+=1              
    if c > len(nums)//2 :
        print(nums[maj_index])
    else:
        print("no majority element")                  
        
        
arr=[7,7,5,7,5,1,7]
findMajority(arr)        