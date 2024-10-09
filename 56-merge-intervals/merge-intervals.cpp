class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {
        if(intervals.size()<=1){
            return intervals;
        }
        vector<vector<int>> merged;
        sort(intervals.begin(),intervals.end());
        
        int i=1;
        while(i<intervals.size()){
            if(intervals[i][0] <= intervals[i-1][1]){
                intervals[i][0] = min(intervals[i][0], intervals[i-1][0]);
                intervals[i][1] = max(intervals[i][1], intervals[i-1][1]);
            }
            else{
                merged.push_back(intervals[i-1]);
            }
            i++;
        }
        merged.push_back(intervals[i-1]);
        return merged;
    }
};