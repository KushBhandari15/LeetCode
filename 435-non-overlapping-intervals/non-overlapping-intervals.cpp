class Solution {
public:
    static bool compareIntervals(vector<int>& a, vector<int>& b) {
        return a[1] < b[1];
    }
    int eraseOverlapIntervals(vector<vector<int>>& intervals) {
        sort(intervals.begin(), intervals.end(), compareIntervals);
        int count =1;
        int end = intervals[0][1];
        cout<<intervals[0][0]<<" "<<intervals[0][1]<<endl;
        for(int i=1;i<intervals.size();i++){

            if(intervals[i][0]>=end){
                end = intervals[i][1];
                count++;
            }
        }
        return intervals.size()-count;
    }
};