public class Question9{
    public static int _mergeSort(int[] arr){
        int n = arr.length;
        int[] temp = new int[n];
        return mergeSort(arr,temp,0,n-1);
    }

    public static int mergeSort(int[] arr , int[] temp,int left , int right){
        int inv =0;
        if (left<right){
           int  mid=left+(right-left>>1);
           inv+=mergeSort(arr, temp, left, mid);
           inv+=mergeSort(arr, temp, mid+1, right);
           inv+=merge(arr, temp, left,mid, right);

        }
        return inv;
    }

    public static int merge(int[] arr , int[] temp , int left , int mid , int right){
        int inv =0;
        int i = left;
        int j = mid+1;
        int k = left;
        while(i<=mid && j<=right){
            if (arr[i] <= arr[j]){
                temp[k] = arr[i];
                k += 1;
                i += 1;
            }
            else{
             temp[k] = arr[j];
             inv+= (mid-i + 1);
             k += 1;
             j += 1;
            }
        }

        while (i <= mid){
            temp[k] = arr[i];
            k += 1;
            i += 1;
        }
        while (j <= right){
            temp[k] = arr[j];
            k += 1;
            j += 1;

        }

        for(int counter = left ; counter<=right; counter++){
            arr[counter] = temp[counter];
        }
        return inv;
    }

    public static void main(String[] args) {
        int[] arr ={ 54,26,93,17,77,31,44,55,20};
        System.out.println(_mergeSort(arr));
    }
}