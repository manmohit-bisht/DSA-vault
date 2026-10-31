#include <climits>
class Solution
{
public:
    int reverse(int x)
    {
        int rev = 0;
        while (x)
        {
            int digit = x % 10;
            x /= 10;
            if ((rev > INT_MAX / 10) || (rev == INT_MAX && digit > 7)) // This condition checks for overflow when rev is positive, the digit > 7 check is for the last digit of INT_MAX which is 7, because INT_MAX is 2147483647 and digit can only be 0-9, so if rev is 214748364 and digit is greater than 7, it will overflow
                return 0;
            if ((rev < INT_MIN / 10) || (rev == INT_MIN && digit < -8)) // This condition checks for overflow when rev is negative, the digit < -8 check is for the last digit of INT_MIN which is -8, because INT_MIN is -2147483648 and digit can only be 0-9, so if rev is -214748364 and digit is less than -8, it will overflow
                return 0;
            rev = rev * 10 + digit;
        }
        return rev;
    }
};