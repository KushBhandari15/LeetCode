class Solution {
public:
    int lengthOfLongestSubstring(string s) {
        unordered_map<int, int> map;
        int start = 0;
        int maxCount = 0;

        for(int end = 0; end < s.size(); end++){

            map[s[end]]++;
            while(map[s[end]]>1){
                map[s[start]]--;
                start++;
            }
            maxCount = max(maxCount, end-start+1);
        }

        return maxCount;
    }
};