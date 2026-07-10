class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        unordered_map<int, int> h;

        for (int i = 0; i < nums.size(); ++i) {
            if (!h.contains(target - nums[i])) {
                h[nums[i]] = i;
            } else {
                vector<int> res = {min(i, h[target-nums[i]]), max(i, h[target-nums[i]])};
                return res;
            }
        }
    }
};
