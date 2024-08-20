class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        vector<int> temp = nums1;
        int x=0; //Tracking index of array 1
        int y=0; //Tracking index of array 2
        for (int i=0; i<m+n;i++){
            if (temp.empty()){
                temp=nums2;
                break;
            }
            else if (nums2.empty()){
                break;
            }
            
            if (x==m){
                nums1[i] = nums2[y];
                y++;
            }
            else if (y==n){
                nums1[i] = temp[x];
                x++;
            }
            else if (temp[x] >= nums2[y]){
                nums1[i] = nums2[y];
                y++;
            } 
            else {
                nums1[i] = temp[x];
                x++;
            } 
        }
    }
};