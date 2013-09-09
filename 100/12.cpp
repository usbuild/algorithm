#include <iostream>
using namespace std;
class Empty 
{
public:
    static int i, sum;
    Empty() {
        ++i;
        sum += i;
    }
};
int Empty::i = 0;
int Empty::sum = 0;
int main(int argc, const char *argv[])
{
    int n = 10;
    Empty a[10];
    cout << Empty::sum << endl;
    return 0;
}
