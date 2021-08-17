import java.lang.reflect.Array;
import java.util.Arrays;
import java.util.Comparator;
import java.util.Stack;

public class Question6 {

    public static void mergeInterval(Interval[] aIntervals){
        if(aIntervals.length <=1){
            System.out.println("jkbjh");
        }

        Arrays.sort(aIntervals,new Comparator<Interval>(){

            public int compare(Interval i1 , Interval i2){
                return i1.i - i2.i;
            }
            
        });


        
        Stack<Interval> st = new Stack<>();
        st.push(aIntervals[0]);
        for(int i =1 ; i< aIntervals.length ; i++){
            Interval top = st.peek();
            if(top.j>aIntervals[i].i){
                top.j=aIntervals[i].j;
                st.pop();
                st.push(top);
            }
            else{
                st.push(aIntervals[i]);
            }
        }
    
        while(!st.isEmpty()){
            Interval t = st.pop();
            System.out.print("["+t.i+","+t.j+"]");
        }

    }

    public static void main(String[] args) {
        Interval[] aIntervals = new Interval[5];
        aIntervals[0]=new Interval(1,3);
        aIntervals[1]=new Interval(2, 6);
        aIntervals[2]=new Interval(8, 10);
        aIntervals[3]= new Interval(9, 13);
        aIntervals[4]= new Interval(14, 18);
        mergeInterval(aIntervals);

        
    }
    
}

class Interval{
    int i , j ;
    Interval(int i , int j){
        this.i=i;
        this.j=j;
    }
}


