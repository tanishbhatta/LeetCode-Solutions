class Solution {
public:
    bool check(vector<int>& nums) {
        int count = 0;
        for (size_t i=0; i < nums.size(); i++){
            if (nums.at(i) > nums.at((i+1)%nums.size())) count++;
        };
        return count <=1;
    };
};