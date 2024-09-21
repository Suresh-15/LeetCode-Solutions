class Solution {
    public List<String> fizzBuzz(int n) {
        return new java.util.AbstractList<String>() {
            @Override
            public String get(int i) {
                i++;
                return (
                    i % 15 == 0 ? "FizzBuzz" :
                    i % 5 == 0 ? "Buzz" :
                    i % 3 == 0 ? "Fizz" :
                    String.valueOf(i)
                );
            }
            @Override
            public int size() {
                return n;
            }
        };

    }
}