// Evaluation of postfix expressions code written by 20/4001 ASWANTH C M
#include <iostream>
#include <string>
#include <stack>
using namespace std;

int evaluatePostFix(char *exp){
    stack<char> stack;
    int i;
    for (i=0; exp[i]; ++i){
        if (isdigit(exp[i]))
            stack.push(exp[i]-'0');
        else{
            int val1=stack.top();stack.pop();
            int val2=stack.top();stack.pop();
            switch(exp[i]){
              case '+': 
                  stack.push(val2+val1);break;
              case '-': 
                  stack.push(val2-val1);break;
              case '*': 
                  stack.push(val2*val1);break;
              case '/': 
                  stack.push(val2/val1);break;
            }
        }
    }
    char el = stack.top();
    stack.pop();
    return el;
}

int main() {
    char exp[100];
    cout<<"Enter a postfix expression :";
    cin>>exp;
    cout<<"\nPostfix evaluation result : "<<evaluatePostFix(exp);
    return 0;
}