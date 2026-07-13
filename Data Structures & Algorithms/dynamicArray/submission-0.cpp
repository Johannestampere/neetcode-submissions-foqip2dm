class DynamicArray {
    int size;
    int* arr;
    int capacity;
public:

    DynamicArray(int capacity): size{0}, capacity{capacity},
                                arr{new int[capacity]} {
        for (int i = 0; i < capacity; ++i) { 
            arr[i] = 0;
        }
    }
    
    ~DynamicArray() {
        delete[] arr;
    }

    int get(int i) {
        return arr[i];
    }

    void set(int i, int n) {
        arr[i] = n;
    }

    void pushback(int n) {
        if (size == capacity) {
            resize();
        }
        arr[size] = n;
        size++;
    }

    int popback() {
        int popEl = arr[size-1];
        arr[size-1] = 0;
        size--;
        return popEl;
    }

    void resize() {
        capacity *= 2;

        int* newArr = new int[capacity];

        for (int i = 0; i < size; ++i) {
            newArr[i] = arr[i];
        }

        delete[] arr;
        arr = newArr;
    }

    int getSize() {
        return size;
    }

    int getCapacity() {
        return capacity;
    }
};
