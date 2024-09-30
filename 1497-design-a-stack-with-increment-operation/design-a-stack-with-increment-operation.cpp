class CustomStack {
    vector<int> stack;
    vector<int> increment_list;
    int size;
    int count = 0;
    int diff = 0;

public:
    CustomStack(int maxSize) {
        this->size = maxSize;
        this->stack.resize(this->size);
        this->increment_list.resize(this->size);
    }
    
    void push(int x) {
        if (count == size)
            return;

        if (count >= 1)
            increment_list[count - 1] += diff;
        diff = 0;

        stack[count] = x;
        increment_list[count] = 0;
        count++;
    }
    
    int pop() {
        if (count == 0)
            return -1;

        diff += increment_list[count-1];
        int result = stack[count-1] + diff;
        count--;
        return result;
    }
    
    void increment(int k, int val) {
        if (count == 0)
            return;
        increment_list[min(k - 1, count - 1)] += val;
    }
};
/**
 * Your CustomStack object will be instantiated and called as such:
 * CustomStack* obj = new CustomStack(maxSize);
 * obj->push(x);
 * int param_2 = obj->pop();
 * obj->increment(k,val);
 */
