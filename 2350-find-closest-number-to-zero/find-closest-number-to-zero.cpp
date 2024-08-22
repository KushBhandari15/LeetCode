class Solution {
public:
    int findClosestNumber(vector<int>& nums) {
        int temp = INT_MAX;
        for(auto i:nums){
            if(abs(i) < abs(temp)){
                temp = i;
            }
            else if(abs(i)==abs(temp)){
                if(i > temp){
                    temp = i;
                }
            }
        }
        return temp;

    }
};