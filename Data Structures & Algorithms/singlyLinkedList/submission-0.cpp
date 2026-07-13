class LinkedList {

class Node { 
public:
    int n;
    Node* next;


    Node(int value, Node* nextNode = nullptr)
        : n{value}, next{nextNode} {}
};

int size;
Node* head;

public:
    LinkedList(): size{0}, head{nullptr} {}
    ~LinkedList() {
        while (head != nullptr) { 
            Node* tmp = head->next;
            delete head;
            head = tmp;
        }
    }

    int get(int index) {
        if (index >= size) {
            return -1;
        }
        Node* tmp = head;

        for (int i = 0; i<index;++i) {
            tmp = tmp->next;
        }
        return tmp->n;
    }

    void insertHead(int val) {
        head = new Node(val, head);
        ++size;
    }
    
    void insertTail(int val) {
        Node* newNode = new Node(val);

        if (head == nullptr) {
            head = newNode;
            ++size;
            return;
        }

        Node* tmp = head;

        while (tmp->next != nullptr) {
            tmp = tmp->next;
        }

        tmp->next = newNode;
        ++size;
    }

    bool remove(int index) {
        if (index < 0 || index >= size) {
            return false;
        }

        if (index == 0) {
            Node* toDelete = head;
            head = head->next;
            delete toDelete;
            --size;
            return true;
        }

        Node* tmp = head;

        for (int i = 0; i < index - 1; ++i) {
            tmp = tmp->next;
        }

        Node* toDelete = tmp->next;
        tmp->next = toDelete->next;
        delete toDelete;

        --size;
        return true;
    }

    vector<int> getValues() {
        vector<int> v;
        Node* tmp = head;
        int i = 0;

        while (tmp != nullptr) {
            v.push_back(tmp->n);
            tmp = tmp->next;
        }

        return v;
    }
};
