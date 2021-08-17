public class Question3 {
    public static void main(String[] args) {
        int[] arr = {1,2,4,4,5};
        find(arr);
        

    }

    public static void find(int[] arr){
        int xor=0,x=0,y=0;
        for(int i : arr){
            xor=xor^i;
        }
        for(int i =0 ; i < arr.length+1;i++){
            xor=xor^i;
        }
        int setBit = xor & (~(xor-1));

        for(int i : arr){
            if ((setBit & i )== 0){
                x=x^i;
            }
            else{
                y=y^i;
            }
        }

        for(int i =0 ; i < arr.length+1;i++){
            if ((setBit & i )== 0){
                x=x^i;
            }
            else{
                y=y^i;
            }
        }


        System.out.println(x + "\n"+y);

       

    }
    
}
