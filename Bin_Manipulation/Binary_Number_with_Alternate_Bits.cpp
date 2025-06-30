/**
 * Given a positive integer, check whether it has alternating bits: namely, 
 * if two adjacent bits will always have different values.
 * 
 * Constraint: 1 <= n <= 2^31 - 1
 */

#include <iostream>
using namespace std;

string convertToBinary(int n)   {
    string bin_result = "";
    while (n > 0)
    {   
        bin_result = to_string(n % 2) + bin_result;
        n = n / 2;
    }
    return bin_result;
}

bool hasAlternatingBits(int n) {
    string bin_form = convertToBinary(n);
    for(int i = 1; i < bin_form.length(); i++)
    {
        if (bin_form[i] == bin_form[i - 1])
        {
            return false;
        }
    }

    return true;
}

int main()
{
    cout << hasAlternatingBits(5) << endl;  //True
    cout << hasAlternatingBits(7) << endl;  //False
    cout << hasAlternatingBits(11) << endl; //False
    cout << hasAlternatingBits(2) << endl;  //True
    cout << hasAlternatingBits(4) << endl;  //False

    return 0;
}