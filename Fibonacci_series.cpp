//Fibonacci series code written by 20/4001 ASWANTH C M
#include <iostream>
using namespace std;

int _Fib(int n){
    if(n<2)
      return n;
    else
      return(_Fib(n-1) + _Fib(n-2));
}

int main() {
  int num, i = 0;
  cout << "Enter the number of terms of series : ";
  cin >> num;
  cout<<"Fibonacci series of "<<num<<" terms :\n";
  while(i<num){
    cout<<_Fib(i)<<" ";
    i++;
  }
  return 0;
}