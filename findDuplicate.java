import java.util.ArrayList;

class Question1{

    public static int findDuplicate(int[] arr){

        int sp=arr[0];
        int fp=arr[0];
        do{
            sp=arr[sp];
            fp=arr[arr[fp]];
        }
        while(sp!=fp);
        fp=arr[0];
        while(sp!=fp){
            sp=arr[sp];
            fp=arr[fp];
        }

        return sp;
    }

    public static void main(String[] args) {
        int arr[] = {1,3,4,2,2};
        int ans = findDuplicate(arr);
        System.out.println(ans);
    }
}