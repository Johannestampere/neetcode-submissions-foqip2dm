class Solution {
public:
    bool isValid(string s) {
        // dict for matching brackets
        unordered_map<char, char> parens = {
            {')', '('},
            {']', '['},
            {'}', '{'}
        };

        vector<char> st;

        // ]
        // st = 

        for (char c : s) {
            if (!parens.contains(c)) {
                st.push_back(c);
            } else {
                if (!st.empty() && st.back() == parens[c]) {
                    st.pop_back();
                } else {
                    return false;
                }
            }
        }

        if (st.empty()) {
            return true;
        } else {
            return false;
        }
    }
};
