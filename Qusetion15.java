import java.util.*;

public class Qusetion15 {

    public static List<List<Integer>> subset (int[] nums){
        int n= nums.length;
        List<List<Integer>> res = new ArrayList<>();
        backtrack(res,nums,0,new ArrayList<>());
        return res;

    }

    public static void backtrack(List<List<Integer>> res , int[] nums , int pos, ArrayList<Integer> sub){
        res.add(new ArrayList(sub));
        for(int i=pos;i<nums.length;i++)
        {
            sub.add(nums[i]);
            backtrack(res,nums,i+1,sub);
            sub.remove(sub.size()-1);
        }

    }

    public static void main(String[] args) {
        int[] nums = {1,2,3};
        List<List<Integer>> res=subset(nums);
        for(int i =0 ; i < res.size();i++){
            System.out.println(res.get(i));
        }
    }
    
}
