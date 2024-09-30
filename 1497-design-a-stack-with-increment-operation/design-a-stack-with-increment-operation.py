class CustomStack:

    def __init__(self, maxSize: int):
        self.size = maxSize
        self.stack = []
        self.increment_list = []

    def push(self, x: int) -> None:
        if len(self.stack) < self.size:
            self.stack.append(x)
            self.increment_list.append(0)

    def pop(self) -> int:
        if not self.stack:
            return -1
        if len(self.increment_list) > 1:
            self.increment_list[-2] += self.increment_list[-1]
        return self.stack.pop() + self.increment_list.pop()        

    def increment(self, k: int, val: int) -> None:
        if self.increment_list:
            self.increment_list[min(k-1, len(self.stack) - 1)] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)