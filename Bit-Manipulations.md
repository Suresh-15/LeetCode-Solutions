### Bit Manipulation
1.  To count the number of 1-bits in the binary form of a number. <br>
```cpp
#include <iostream>
int main() {
    // __builtin_popcount(number), where number parameter is an unsigned integer.
    unsigned int num = 50; // Binary of 50 is 110010
    cout << __builtin_popcount(num) << endl; // output: 3

    // specialised class (std::bitset<fixed_size> variable_name(unsigned_integer)).
    num = 12345; // Binary of 12345 = 11000000111001, length of binary representation = 14.
    std::bitset<8> var1(num); // stores the last 8 bits of the binary representation, since 8 < 14.
    std::bitset<16> var2(num); // stores all bits with 2 0-bits as prefix, since 16 > 14.
    cout << var1 << "  " << var2 << endl; // ouptut: 00111001   0011000000111001
    cout << var1.count() << "  " << var2.count() << endl; // ouptut: 4  6
    return 0;
}
```

```java
public class Main {
    public static void main(String[] args) {
        // in java, you can find the number of 1-bits in both positive and negative number.
        // in java, we use Integer.bitCount(number) to accomplish it.
        int num = 50;
        System.out.println(Integer.bitCount(num)); // output: 3
    }
}
```

```python
num = 50
# In python, int class has a pre-builtin method to find number of 1-bits => bit_count()
print(num.bit_count()) # 3 
```
