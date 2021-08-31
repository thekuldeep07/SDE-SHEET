import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collection;
import java.util.Collections;

class Job{
    char id;
    int deadline;
    int profit;

    public Job(){

    }
    public Job(char id, int deadline, int profit)
    {
        this.id = id;
        this.deadline = deadline;
        this.profit = profit;
    }

    public void printJobScheduling(ArrayList<Job> arr , int n){
        Collections.sort(arr,(a,b) -> (b.profit - a.profit));
        int maxi=0;
        for(int i =0 ; i < n ; i++){
            maxi=Math.max(maxi, arr.get(i).deadline);
        }
        int[] result = new int[maxi+1];
        for(int i =0 ; i <= maxi ;i++){
            result[i]=-1;
        }
        System.out.println();
        int count =0 , maxProfit=0;
        for(int i =0 ; i < n ; i++){
            for(int j = arr.get(i).deadline;j>=1;j--){
                if(result[j]==-1){
                    count+=1;
                    maxProfit+=arr.get(i).profit;
                    result[j]=i;
                    System.out.println(arr.get(i).id);
                    break;

                }
            }
        }

    }
}
class JobSequencing{
    public static void main(String[] args) {
        ArrayList<Job> arr = new ArrayList<Job>();
 
        arr.add(new Job('a', 2, 100));
        arr.add(new Job('b', 1, 19));
        arr.add(new Job('c', 2, 27));
        arr.add(new Job('d', 1, 25));
        arr.add(new Job('e', 3, 15));
       
        // Function call
        System.out.println("Following is maximum "
                           + "profit sequence of jobs");
 
        Job job = new Job();
 
        // Calling function
        job.printJobScheduling(arr, arr.size());
        
    }
}