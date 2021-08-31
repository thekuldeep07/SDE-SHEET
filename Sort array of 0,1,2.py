#sort array of 0's ,1's and 2's

#Method 1 
#use sorting algorith to sort the given array 
#T.C=O(NlogN)(merge sort) 

#Method 2 
#use counting sort 

#Method 3 
#using Dutch National Flag Algorihtm
#T.c =



def sort(arr):
    if(len(arr)<=1):
        return arr
    lp=mp=0
    hp=len(arr)-1
    while(mp<=hp):
        if arr[mp] == 0 :
            arr[mp],arr[lp]=arr[lp],arr[mp]
            lp+=1
            mp+=1
        
        elif arr[mp] == 1 :
            mp+=1
        
        else:
            arr[hp],arr[mp]=arr[mp],arr[hp]
            hp-=1
    
    return arr  

arr=[2,0,1,1,1,0,2,1] 
print(sort(arr))     
                    
            
        
    
