class LRUCache {
    struct Node {
        int key;
        int val;
        Node* prev;
        Node* next;

        Node(int key, int val)
            : key{key}, val{val}, prev{nullptr}, next{nullptr} {}
    };

    int capacity;
    Node* left;
    Node* right;
    unordered_map<int, Node*> hashmap;

public:
    LRUCache(int capacity)
        : capacity{capacity},
          left{new Node(0, 0)},
          right{new Node(0, 0)} {
        left->next = right;
        right->prev = left;
    }

    int get(int key) {
        if (hashmap.find(key) == hashmap.end()) {
            return -1;
        }

        Node* node = hashmap[key];

        node->prev->next = node->next;
        node->next->prev = node->prev;

        Node* oldMRU = left->next;

        left->next = node;
        node->prev = left;
        node->next = oldMRU;
        oldMRU->prev = node;

        return node->val;
    }

    void put(int key, int value) {
        if (hashmap.find(key) != hashmap.end()) {
            Node* node = hashmap[key];
            node->val = value;

            node->prev->next = node->next;
            node->next->prev = node->prev;

            Node* oldMRU = left->next;

            left->next = node;
            node->prev = left;
            node->next = oldMRU;
            oldMRU->prev = node;

            return;
        }

        Node* node = new Node(key, value);
        hashmap[key] = node;

        Node* oldMRU = left->next;

        left->next = node;
        node->prev = left;
        node->next = oldMRU;
        oldMRU->prev = node;

        if (hashmap.size() > capacity) {
            Node* lru = right->prev;

            lru->prev->next = right;
            right->prev = lru->prev;

            hashmap.erase(lru->key);
            delete lru;
        }
    }
};