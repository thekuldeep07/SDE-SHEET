class Qusetion10{
    public static void permute(String ques , String ans ){
        if (ques.length()==0){
            System.out.println(ans);
        } 
        for(int i =0 ; i < ques.length();i++){
            char c = ques.charAt(i);
            String nq = ques.substring(0,i)+ques.substring(i+1);
            permute(nq, ans+c);
        }

    }


    public static void main(String[] args) {
        String question = "ABC";
        permute("ABC","");
        
    }
}