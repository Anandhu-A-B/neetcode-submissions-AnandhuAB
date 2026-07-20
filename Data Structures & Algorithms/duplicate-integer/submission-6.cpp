class Solution {
public:
    bool hasDuplicate(vector<int>& nums) {
        int i,n,num;
        n = nums.size();
        unordered_set<int> seen;
        for (i=0;i<n;i++){
            num = nums[i];
            if (seen.find(num)!=seen.end()){
                return true;
        }
            else{
                seen.insert(num);
            }
            }
        return false;
    }
};