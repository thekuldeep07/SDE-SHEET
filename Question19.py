# Question :- find all the majority element i.e which appear more than n//3 times

# method1:- using two nested loops
# o(n2)

# method2:- using hashmap
# O(n)

# mrthod 3 :- using BAyers-moore voting algorithm


def findMajority(nums):
    maj_index1=0
    maj_index2=0
    count1=0
    count2=0
    for i in range(len(nums)):
        if nums[i]== nums[maj_index1]:
            count1+=1
        elif nums[i]== nums[maj_index2]:
            count2+=1   
        elif count1==0:
            count1=1
            maj_index1=i
        elif count2==0:
            count2=1
            maj_index2=i
        else:
            count2-=1
            count1-=1
    c1=0       
    c2=0  
    for i in range(len(nums)):
        if nums[i]==nums[maj_index1]:
            c1+=1        
        elif nums[i]==nums[maj_index2]:
            c2+=1          
    if c1 > len(nums)//3 :
        print(nums[maj_index1])
    if c2 > len(nums)//3 :
        print(nums[maj_index2])                    
        
        
arr=[1,1,1,3,3,2,2,2]
findMajority(arr)        