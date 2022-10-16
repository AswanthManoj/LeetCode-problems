//Tower of Hanoi recursive function program written by 20/4001 Aswanth C M
#include <iostream>
using namespace std;

void _Hanoi(int n, char firstRod, char auxyRod, char lastRod){
  if (n==1){
    cout<<"\nMove disk 1 from "<<firstRod<<" to "<<lastRod;
    return;
  }
  
  _Hanoi(n-1, firstRod, auxyRod, lastRod);
  cout<<"\nMove disk "<<n<<" from "<<firstRod<<" to "<<lastRod;
  _Hanoi(n-1, auxyRod, lastRod, firstRod);
}

int main() {
  int n_disk;
  cout<<"Enter the number of disks : ";
  cin>>n_disk;
  _Hanoi(n_disk,'A','B','C');
  return 0;
  
}