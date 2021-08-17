def permute(nums):
   ans=permuteUtils(nums,res=[],ans=[])
   print(ans)

def permuteUtils(nums,res=[],ans=[]):
    if len(nums)==0:
        res.append(ans)
        
    for i in range(len(nums)):
        nq=nums[0:i]+nums[i+1:]
        permuteUtils(nq,res,ans+[nums[i]]) 
    return res
nums=[1,2,3]
permute(nums)         
            