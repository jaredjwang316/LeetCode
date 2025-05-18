#include <iostream>
#include <string>
using namespace std;

string addBinary(string a, string b) {
    string added_binary = "";
    if (a.length() < b.length())
    {
        swap(a, b);
    }

    while(b.length() < a.length())
    {
        b = "0" + b;
    }

    char carry = '0';
    for(int i = b.length() - 1; i >= 0; i--)
    {
        if ( (b[i] == '0' && a[i] == '1') || (b[i] == '1' && a[i] == '0') )
        {
            if (carry == '0')
            {
                added_binary = "1" + added_binary;
            }
            else
            {
                added_binary = "0" + added_binary;
            }
        }
        else if ((b[i] == '0' && a[i] == '0'))
        {
            if (carry == '0')    
            {
                added_binary = "0" + added_binary;
            }
            else
            {
                added_binary = "1" + added_binary;
                carry = '0';
            }
        }
        else    //b[i] = a[i] = '1'
        {
            if (carry == '0')
            {
                added_binary = "0" + added_binary;
            }
            else
            {
                added_binary = "1" + added_binary;
            }
            
            carry = '1';
        }
    }
    
    if (carry == '1')
    {
        added_binary = '1' + added_binary;
    }
    return added_binary;
}

int main()
{
    cout << "adding 11 + 1 = " << addBinary("11", "1") << endl;
    cout << "adding 11 + 1 = " << addBinary("1", "11") << endl; 
    cout << "adding 1010 + 1011 = " << addBinary("1010", "1011") << endl;    
    cout << "adding 100 + 10 = " << addBinary("100", "10") << endl;    

    return 0;
}