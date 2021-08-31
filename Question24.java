import java.util.HashSet;
import java.util.Set;
import java.util.*;
class Question24{
    public static int findSubsequence(int[] nums){
        int ans=0;
        Set<Integer> set = new HashSet<Integer>();
        for(int i : nums){
            set.add(i);
        }
        for(int i =0 ; i < nums.length;i++){
            if(!set.contains(nums[i]-1)){
                int currAns=1;
                int currNum=nums[i];
                while(set.contains(currNum+1)){
                    currAns+=1;
                    currNum+=1;
                }
                ans=Math.max(ans, currAns);
            }
        }
        return ans;
    }
    public static void main(String[] args) {
        int[] nums ={100,4,200,1,3,2};
        System.out.println(findSubsequence(nums));
    }
}