class Solution {
public:
    int totalFruit(vector<int>& fruits) {
        int start = 0;
        unordered_map<int, int> map;
        int maxCount = 0;

        for(int end = 0; end<fruits.size();end++){
            map[fruits[end]]++;

            while(map.size()>2){
                map[fruits[start]]--;
                if(map[fruits[start]]==0){
                    map.erase(fruits[start]);
                }
                start++;
            }

            maxCount = max(maxCount, end-start+1);
    
        }

        return maxCount;
    }
};