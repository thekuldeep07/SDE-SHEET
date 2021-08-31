# Question :- 2Sum

# find idices of the no. x and y in array such that there sum equals to target 
# input=[2,8,7,0] target=9
# output=[0,2]

# Approach 1 :- we can use two nested loops 
# t.c = O(n2)

# Approach 2: first sort the array and then use the concept of two pointers
# t.c=O(nlogn)


# approach 3 :- use the hashmap
def find2Sum(nums,target):
    li=[]
    di={}
    for i in range(len(nums)):
        temp= target-nums[i]
        if temp not in di:
            di[nums[i]]=i
        else:
            return [di[temp],i]    

print(find2Sum([2,7,6,4],9))     