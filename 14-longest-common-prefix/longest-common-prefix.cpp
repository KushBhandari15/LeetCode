class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        
        string compare = strs[0];
        if(compare==""){
            return "";
        }
        int res = INT_MAX;
        for(int i=1;i<strs.size();i++){
            int temp = 0;
            string compare2 = strs[i];
            int j = 0;
            while(j<compare.size() && compare[j]==compare2[j]){
                temp++;
                j++;
            }
            res = min(res, temp);
        }

        return compare.substr(0, res);
    }
};