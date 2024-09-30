class CustomStack {
private:
    int *stack, *increment_list;
    int size, top = -1;
public:
    CustomStack(int maxSize) {
        this->size = maxSize;
        this->stack = new int[this->size];
        this->increment_list = new int[this->size];
    }
    
    void push(int x) {
        if (this->top < this->size - 1) {
            this->top += 1;
            this->stack[this->top] = x;
            this->increment_list[this->top] = 0;
        }
    }
    
    int pop() {
        if (this->top == -1) {
            return -1;
        } else {
            if (this->top >= 1) {
                this->increment_list[this->top - 1] += this->increment_list[this->top];
            }
            int lastIndex = this->top--;
            int result = this->stack[lastIndex] + this->increment_list[lastIndex];
            this->increment_list[lastIndex] = 0;
            return result;
        }
    }
    
    void increment(int k, int val) {
        if (this->top != -1) {
            this->increment_list[min(k - 1, this->top)] += val;
        }
    }
};

/**
 * Your CustomStack object will be instantiated and called as such:
 * CustomStack* obj = new CustomStack(maxSize);
 * obj->push(x);
 * int param_2 = obj->pop();
 * obj->increment(k,val);
 */
