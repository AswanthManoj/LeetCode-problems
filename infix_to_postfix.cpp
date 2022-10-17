// Infix to postfix expressions code written by 20/4001 ASWANTH C M
#include <iostream>
#include <string>
#include <stack>
using namespace std;

#include <bits/stdc++.h>
using namespace std;
 

int prec(char c)
{
    if (c == '^')
        return 3;
    else if (c == '/' || c == '*')
        return 2;
    else if (c == '+' || c == '-')
        return 1;
    else
        return -1;
}
 
void infixToPostfix(string s)
{
    stack<char> st; 
    string result;
    for (int i = 0; i < s.length(); i++) {
        char c = s[i];
        if (isdigit(c))
            result += c;  
        else if (c == '(')
            st.push('(');
        else if (c == ')') {
            while (st.top() != '(') {
                result += st.top();
                st.pop();
            }
            st.pop();
        }
        else {
            while (!st.empty()
                   && prec(s[i]) <= prec(st.top())) {
                result += st.top();
                st.pop();
            }
            st.push(c);
        }
    }
    while (!st.empty()) {
        result += st.top();
        st.pop();
    }
    cout << result << endl;
}
 

int main()
{
    string exp = "(34+66)/4*34-(2^3)";
    infixToPostfix(exp);
    return 0;
}