class Question4{
    public static void main(String[] args) {
        int[] arr1 ={3,5,9};
        int[] arr2={0,1,4,7,90};

        mergeByInsertion(arr1, arr2);
        System.out.println();

        mergeByGAP(arr1, arr2);



    }

    public static void mergeByInsertion(int[] arr1,int[] arr2){
        for(int i =0 ; i < arr1.length;i++){
            if (arr1[i] > arr2[0]){
                int temp=arr1[i];
                arr1[i]=arr2[0];
                arr2[0]=temp;
                int j=1;
                while ((j< arr2.length) && (temp>arr2[j])){
                    arr2[j-1]=arr2[j];
                j+=1;

                }
                arr2[j-1]=temp;   
            }
        }

        printArrays(arr1, arr2);

    }

    public static int findGap(int gap){
        if (gap<=1){
            return 0;
        }
        else{
            return (gap/2) +(gap%2);

        }
        

    }

    public static void mergeByGAP(int[] arr1 , int[] arr2){
        int n= arr1.length;
        int m = arr2.length;
        int gap = findGap(n+m);
        while (gap >0){
            int i =0;
            while (i+gap< n){
                if(arr1[i]>arr1[i+gap]){
                    int temp = arr1[i];
                    arr1[i]=arr1[i+gap];
                    arr1[i+gap]=temp;
                }
                i++;
            }
            int j=0;
            if (gap>n){
                j =gap-n;
            }
            while ((i < n) && (j < m)){
                if (arr1[i] > arr2[j]){
                    int temp = arr1[i];
                    arr1[i]=arr2[j];
                    arr2[j]=temp;
                }
                i++;
                j++;
            }

            if(j<m){
                j =0;
                while (j+gap<m){
                    if (arr2[j]>arr2[j+gap]){
                        int temp=arr2[j];
                        arr2[j]=arr2[j+gap];
                        arr2[j+gap]=temp;
                    }
                    j++; 
                }
                
            }

            gap = findGap(gap);

        }

        printArrays(arr1, arr2);
    }

    public static void printArrays(int[] arr1 , int[] arr2){
        for(int i =0; i< arr1.length ; i++){
            System.out.print(arr1[i]+" ");
        }
        System.out.println();
        for(int i =0; i< arr2.length ; i++){
            System.out.print(arr2[i]+" ");
        }

    }


}