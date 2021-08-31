def lcs(s1,s2,i,j,memo):
    if i>=len(s1) or j>=len(s2):
        return 0
    
    if memo[i][j]!=-1:
        return memo[i][j]
    
    if s1[i]==s2[j]:
        return 1+lcs(s1,s2,i+1,j+1,memo) 
    
    else:
        left=lcs(s1,s2,i+1,j,memo)
        right=lcs(s1,s2,i,j+1,memo)
        memo[i][j]=max(left,right)
        return memo[i][j]
        
    
    
    
    

if __name__ == '__main__':
    s1="acd"
    s2="ced4"
    memo=[[-1 for i in range(len(s2))] for j in range(len(s1))]
    print(lcs(s1,s2,0,0,memo)) 