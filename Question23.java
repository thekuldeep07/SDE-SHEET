// It's a common enhanced 3Sum solution with few "tricks":
// (quadruplets are [a, b, c, d] with indicies i, j, k, l on every step)

// if (a > target && a > 0 || a * 4 > target) break;
// If a is the smallest number. So if it's greater then target and positive, all other (possible b,c, and d) numbers are positive too and there's no sense in further iterations.
// Also, as a is the smallest number in every quadruplet, a * 4 is the smallest sum we can achieve at this point. Break if a * 4 > target.
// if (a + b > target && b > 0) break; is pretty much the same thing as above.
// Code:
import java.util.*;
class Question23 {
    public static List<List<Integer>> fourSum(int[] nums, int target) {
        List<List<Integer>> result = new ArrayList<>();
        Arrays.sort(nums);
        for (int i = 0; i < nums.length - 3; i++) {
            int a = nums[i];
            if (a > target && a > 0 || a * 4 > target) break;
            if (i > 0 && a == nums[i - 1]) continue;
            
            for (int j = i + 1; j < nums.length - 2; j++) {   
                int b = nums[j];
                if (a + b > target && b > 0) break;
                if (j > i + 1 && b == nums[j - 1]) continue;

                int k = j + 1;
                int c = nums[k];
                
                int l = nums.length - 1;
                int d = nums[l];
                while (k < l) {
                    c = nums[k];
                    d = nums[l];
                    int sum = a + b + c + d;
                    if (sum < target) {
                        k++;
                    } else if (sum > target) {
                        l--;
                    } else {
                        result.add(List.of(a, b, c, d));
                        k++;
                        l--;
                        while (k < l && nums[k] == nums[k - 1]) k++;
                        while (k < l && nums[l] == nums[l + 1]) l--;
                    }
                }
            }  
        }
        return result;
    }
    public static void main(String[] args) {
        int[] nums = {2,2,2,2,2};
        List<List<Integer>> result=fourSum(nums, 8);
        for(List<Integer> i : result ){
            System.out.println(i);
        }
    }
}