class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> h;
        int len = nums.size();

        for (int i = 0; i < len; ++i) {
            if (!h.contains(target - nums[i])) {
                h[nums[i]] = i;
            } else {
                vector<int> res = {h[target-nums[i]], i};
                return res;
            }
        }
    }
};
