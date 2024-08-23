class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int res = 0;
        int buyPrice = prices[0];
        for(int i=1;i<prices.size();i++){
            buyPrice = min(buyPrice, prices[i]);
            res = max(res, prices[i]-buyPrice);
        }
        
        return res;
    }
};