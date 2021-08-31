#Best time to buy and sell stocks
#input = [7,1,5,3,6,4]
#output = pofit (6-1) = 5

# we will linearly traverse the array and will maintain to variable 
# max profit = 0 
# minprice = prices[0]
# then we will linearly iterate and will update the value of minprice if we find any price less than minprice
# and update maxprofit if p- minprice > profit 


def findProfit(nums):
    if len(nums) <=1:
        return 0
    minprices=nums[0]
    profit=0
    for p in nums:
        if p < minprices:
            minprices=p
        if p- minprices > profit:
            profit = p- minprices
    return profit

prices=[7,1,5,3,6,4]
print(findProfit(prices))            