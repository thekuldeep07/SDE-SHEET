public class Question8 {

    public static void printPascalTriangleBySum(int n){
        int[][] arr = new int[n][n];

        for(int i = 0 ; i < n;i++){
            for(int j=0 ; j < i+1; j++){

                if(j==0||i==j){
                    arr[i][j]=1;
                }
                else{
                    arr[i][j]=arr[i-1][j-1]+arr[i-1][j];
                }
                System.out.print(arr[i][j]+" ");

            }
            System.out.println();
        }
    
    }

    public static void printBYnCr(int n){
       
        for(int i = 1 ; i < n+1;i++){
            int c =1;
            for(int j=1; j<i+1;j++){
                System.out.print(c);
                c=(c*(i-j))/j;
            }
            System.out.println();
        }

    }

    public static void printNthRow(int n){
        int c=1;
        for(int i =1 ; i < n+1;i++){
            System.out.print(c+" ");
            c=(c*(n-i))/i;
        }

    }

    public static void main(String[] args) {
        printPascalTriangleBySum(5);
        System.out.println();
        printBYnCr(5);
        System.out.println();
        printNthRow(5);
    }
    
}
