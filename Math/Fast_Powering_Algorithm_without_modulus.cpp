#include <iostream>
using namespace std;

double myPow(double x, int n) {
        if (n == 0 || x == 1)
            return 1.0;
        if (x == -1)
        {
            if (n % 2 == 0)     //multiplying an even amounts of negative numbers always results in an positive output
                return 1.0;
            else
                return -1.0;    //multiplying an odd amounts of negative numbers always results in an negative output
        }
        int starting_n = n;
        double result = 1;
        
        if (starting_n == -2147483648)  //handling an edge case
        {
            n = 2147483647;
        }

        while(abs(n) > 0)
        {
            if (abs(n) % 2 == 1)
            {
                result = result * x;
            }
            x = x * x;
            n = n / 2;
        }

        if (starting_n == -2147483648)  //handling an edge case
        {
            result = result * x;
        }

        if (starting_n < 0)
            return 1/result;
        return result;

}

int main()
{
    cout << myPow(2, 10) << endl;
    cout << myPow(-2, -2147483648) << endl;
    cout << myPow(-1, -2147483648) << endl;
    cout << myPow(2, -2147483648) << endl;
    return 0;
}