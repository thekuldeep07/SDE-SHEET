public class Question17 {

    public static Double findPow(double x , int n ){
        Double ans= Double.valueOf(1.0);
        Long nn = Long.valueOf(n);
        if(n<0){
            nn = -1 * nn;
        }
        while(nn>0){
            if (nn%2==0){
                x=x*x;
                nn=nn/2;

            }
            else{
                ans=ans*x;
                nn=nn-1;
            }
        }
        if(n<0){
            ans = Double.valueOf(1.0)/Double.valueOf(ans);
        }
        return ans;
    }
    public static void main(String[] args) {
        System.out.println(findPow(2, -31));
    }
    
}
