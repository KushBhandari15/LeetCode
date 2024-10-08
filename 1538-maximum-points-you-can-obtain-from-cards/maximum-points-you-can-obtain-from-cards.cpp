class Solution {
public:
    int maxScore(vector<int>& cardPoints, int k) {
        int total = accumulate(cardPoints.begin(), cardPoints.end(), 0);
        if(k==cardPoints.size()){
            return total;
        }
        int start = 0;
        int sumMax = 0;
        int state = 0;

        for(int end=0;end<cardPoints.size();end++){
            state += cardPoints[end];

            if(end-start+1 == cardPoints.size()-k){
                sumMax = max(sumMax, total-state);
                state -= cardPoints[start];
                start++;
            }
        }

        return sumMax;
    }
};