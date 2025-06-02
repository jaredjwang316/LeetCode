#include <iostream>
#include <vector>
using namespace std;

string multiply(string num1, string num2) {
    if (num1 == "0" || num2 == "0") //edge case: multiplying by 0 akways results in 0
        return "0";
    
    if (num1.length() < num2.length())
    {
        swap(num1, num2);
    }

    vector<int> result;
    for(int i = 0; i < num1.length() + num2.length(); i++)
    {
        result.push_back(0);
    }

    for(int i = num1.length() - 1; i >= 0; i--)
    {
        for(int j = num2.length() - 1; j >= 0; j--)
        {
            result.at(i + j + 1) += (num1[i] - '0') * (num2[j] - '0');
            result.at(i + j) += result.at(i + j + 1) / 10;
            result.at(i + j + 1) = result.at(i + j + 1) % 10;
        }
    }

    string answer = "";

    int index = 0;
    while (result.at(index) == 0)
    {
        index++;
    }
    for (int i = index; i < result.size(); i++)
    {
        answer += to_string(result.at(i));
    }
    return answer;
}

int main()
{
    cout << "2 x 3 = " << multiply("2", "3") << endl;
    cout << "0 x 1 = " << multiply("0", "1") << endl;
    cout << "17 * 17 = " << multiply("17", "17") << endl;
    cout << "9 * 9 = " << multiply("9", "9") << endl;    
    cout << "123 * 456 = " << multiply("123", "456") << endl;   
      
    return 0;
}