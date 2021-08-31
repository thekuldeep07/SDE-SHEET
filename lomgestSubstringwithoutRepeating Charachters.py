# Length of the longest substring without repeating characters
# Difficulty Level : Medium
 
# Given a string str, find the length of the longest substring without repeating characters. 

# For “ABDEFGABEF”, the longest substring are “BDEFGA” and “DEFGAB”, with length 6.
# For “BBBB” the longest substring is “B”, with length 1.
# For “GEEKSFORGEEKS”, there are two longest substrings shown in the below diagrams, with length 7

# Method 1 (Simple : O(n3)): We can consider all substrings one by one and check for each substring whether it 
# contains all unique characters or not. There will be n*(n+1)/2 substrings. Whether a substring contains 
# all unique characters or not can be checked in linear time by scanning it 
# from left to right and keeping a map of visited characters. Time complexity of this solution would be O(n^3).

# def checkDistinct(s,i,j):
#     li=[False for i in range(26)]
#     for k in range(i,j+1):
#         if(li[ord(s[k])-ord('a')]):
#             return False
#         li[ord(s[k])-ord('a')]= True
        
#     return  True  
        
        
# def findSubString(s):
#     ans=0
#     n=len(s)
#     for i in range(n):
#         for j in range(i,n):
#             if checkDistinct(s,i,j):
#                 ans=max(ans,j-i+1)
#     return ans  

# s="geeksforgeeks"
# print(findSubString(s))

# Method 2 (Better : O(n2)) The idea is to use window sliding. Whenever we see repetition, 
# # we remove the previous occurrance and slide the window.
# def longestUniqueSubsttr(str):
     
#     n = len(str)
     
#     # Result
#     res = 0
  
#     for i in range(n):
          
#         # Note : Default values in
#         # visited are false
#         visited = [0] * 256  
  
#         for j in range(i, n):
  
#             # If current character is visited
#             # Break the loop
#             if (visited[ord(str[j])] == True):
#                 break
  
#             # Else update the result if
#             # this window is larger, and mark
#             # current character as visited.
#             else:
#                 res = max(res, j - i + 1)
#                 visited[ord(str[j])] = True
             
#         # Remove the first character of previous
#         # window
#         visited[ord(str[i])] = False
     
#     return res
 
# # Driver code
# str = "geeksforgeeks"
# print("The input is ", str)
 
# len = longestUniqueSubsttr(str)
# print("The length of the longest "
#       "non-repeating character substring is ", len)


# Method 3 (Linear Time): Let us talk about the linear time solution now. 
# This solution uses extra space to store the last indexes of already visited characters. 
# The idea is to scan the string from left to right, keep track of the maximum length Non-Repeating Character Substring seen so far in res. 
# When we traverse the string, to know the length of current window we need two indexes. 
# 1) Ending index ( j ) : We consider current index as ending index. 
# 2) Starting index ( i ) : It is same as previous window if current character was not 
# present in the previous window. To check if the current character was present in the previous window or not, 
# we store last index of every character in an array lasIndex[]. If lastIndex[str[j]] + 1 is more than previous start, 
# then we updated the start index i. Else we keep same i.  

def findSubsequence(s):
    hm={}
    l=r=0
    n=len(s)
    le=0
    while r < n :
        if s[r] in hm:
            l=max(hm[s[r]]+1,l)
        
        hm[s[r]] =r
        le=max(le,r-l+1)
        r+=1
    return le    
         
# # Driver code
str = "geeksforgeeks"
print(findSubsequence(str))             
    