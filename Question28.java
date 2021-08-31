import java.util.HashMap;

class Question28{
    public static int findSubsequenceWihtoutRepeatingChar(String s){
        int ans=0;
        int n = s.length();
        int l =0;
        int r =0;
        HashMap<Character,Integer> hm = new HashMap<>();
        while (r<n){

            if(hm.containsKey(s.charAt(r))){
                l=Math.max(l, hm.get(s.charAt(r))+1);
            }
            hm.put(s.charAt(r),r);
            ans=Math.max(ans, r-l+1);
            r+=1;


        }
        return ans;
    }

    public static void main(String[] args) {
        String s = "geeksforgeeks";
        System.out.println(findSubsequenceWihtoutRepeatingChar(s));
    }
}