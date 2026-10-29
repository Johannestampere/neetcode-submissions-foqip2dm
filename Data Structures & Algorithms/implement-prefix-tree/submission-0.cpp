class PrefixTree {
    struct TrieNode {
        char c;
        TrieNode* children[26];
        bool isWord;
        TrieNode(): isWord(false) {
            for (int i = 0; i < 26; ++i) {
                children[i] = nullptr;
            }
        }
    };
    TrieNode* root;
public:
    PrefixTree(): root(new TrieNode()) {}
    
    void insert(string word) {
        TrieNode* cur = root;
        for (char c : word) {
            int idx = c - 'a';
            if (cur->children[idx] == nullptr) {
                cur->children[idx] = new TrieNode();
            }
            cur = cur->children[idx];
        }
        cur->isWord = true;
    }
    
    bool search(string word) {
        TrieNode* cur = root;
        for (char c : word) {
            int idx = c - 'a';
            if (!cur->children[idx]) {
                return false;
            }
            cur = cur->children[idx];
        }
        return cur->isWord;
    }
    
    bool startsWith(string prefix) {
        TrieNode* cur = root;
        for (char c : prefix) {
            int idx = c - 'a';
            if (!cur->children[idx]) {
                return false;
            }
            cur = cur->children[idx];
        }
        return true;
    }
};
