class Question12{
    public static int findProfit(int[] prices){
        if (prices.length <=1){
            return 0 ;
        }
        int minPrice = prices[0];
        int profit =0;
        for(int i =0 ; i < prices.length;i++){
            if (prices[i] < minPrice){
                minPrice=prices[i];
            }
            if(prices[i]-minPrice >profit){
                profit= prices[i]-minPrice;
            }
        }

        return profit;
    }
    public static void main(String[] args) {
        int[] prices = {7,1,5,3,6,4};
        int ans = findProfit(prices);
        System.out.println(ans);

    }
}