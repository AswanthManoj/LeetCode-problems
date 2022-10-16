//sum of array elements using pointer arithematics 
//20/4001 ASWANTH C M
#include <iostream>
using namespace std;

int Sum(int a[]){
  int sum = *a;
  for(int *i = a+1 ; i < a+8 ; i++){
    sum += *i;
  }
  return sum;
}

int main() {
  int a[] = {3,6,10,7,3,6,3,8};
  cout<<Sum(a);
  return 0;
}