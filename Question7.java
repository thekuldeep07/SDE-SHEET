public class Question7 {
    public static void setZeroMatrix(int[][] arr){
        boolean row_flag = false;
        boolean col_flag = false;
        int nr = arr.length;
        int nc = arr[0].length;
        for(int i =0 ; i< nr;i++){
            for(int j=0; j < nc;j++){
                if(arr[0][j]==0){
                    row_flag=true;
                }
                else if (arr[i][0]==0){
                    col_flag = true;
                }

                else if(arr[i][j]==0){
                    arr[0][j]=0;
                    arr[i][0]=0;
                }
            }
        }
        for(int i =1 ; i< nr;i++){
            for(int j=1; j < nc;j++){
                if((arr[0][j]==0)||(arr[i][0]==0)){
                    arr[i][j]=0;
                }
            }}
        
        if(row_flag){
            for(int i =0 ; i < nc;i++){
                arr[0][i]=0;
            }
        }
        if(col_flag){
            for(int i =0 ; i < nr;i++){
                arr[i][0]=0;
            }
        } 
        
        for(int i =0 ; i< nr;i++){
            for(int j=0; j < nc;j++){
                System.out.print(arr[i][j]);
            }
        System.out.println();} 
    } 

    public static void main(String[] args) {
        int[][] arr = {
            {0,1,2,0},
            {3,4,5,2},
            {1,3,1,5}
        };
        
        setZeroMatrix(arr);
    }
}
