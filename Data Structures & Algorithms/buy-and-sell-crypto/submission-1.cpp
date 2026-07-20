class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int i,j,profit;
        int length = prices.size();
        int maxprofit = 0;
        for (i=0;i<length;i++){
            for (j=i+1;j<length;j++){
                profit = prices[j]-prices[i];
                if (profit>maxprofit){
                    maxprofit = profit;
                }
            }
        }
        return maxprofit;
    }
};
