from typing import List


def nFibonacci(n,dp:List):
    if n<=1:
        return n
    if dp[n]!=-1:
        return dp[n]
    dp[n]=nFibonacci(n-1,dp)+nFibonacci(n-2,dp)
    return dp[n]


if __name__=="__main__":
    n=int(input())
    dp=[-1 for i in range(n+1)]
    print(nFibonacci(n,dp))
    
    