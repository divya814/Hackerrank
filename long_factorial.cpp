#include <iostream>
using namespace std;

long int fact(long int n){
    if(n==0 || n==1){
        return 1;
    }
    return n*fact(n-1);
}
int main() {

    cout<<fact(18);

	return 0;
}
