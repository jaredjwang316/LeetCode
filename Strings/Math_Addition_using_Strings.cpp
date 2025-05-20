#include <iostream>
#include <string>

using namespace std;

string addStrings(string num1, string num2) {
    if (num1 == "0")
        return num2;
    else if (num2 == "0")
        return num1;
    
    if (num1.length() < num2.length())
    {
        string temp = num1;
        num1 = num2;
        num2 = temp;
    }

    while(num2.length() < num1.length())
    {
        num2 = "0" + num2;  //add appending zeros to num2 until its length equal to 1 for easier iterative addition
    }
    
    int carry = 0;
    string addition_result = "";
    for (int i = num1.length() - 1; i > -1; i--)
    {
        addition_result = to_string(( (num1[i] - 48) + (num2[i] - 48) + carry) % 10) + addition_result;
        carry = ((num1[i] - 48) + (num2[i] - 48) + carry) / 10; //carry over to the next iterative addition 
    }
    
    if (carry != 0)
    {
        addition_result = to_string(carry) + addition_result;
    }
    return addition_result;
}

int main()
{
    cout << "11 + 123 = " << addStrings("11", "123") << endl;
    cout << "456 + 77 = " << addStrings("456", "77") << endl;    
    cout << "0 + 0 = " << addStrings("0", "0") << endl;
    cout << "1 + 9 = " << addStrings("1", "9") << endl;   
    return 0;
}