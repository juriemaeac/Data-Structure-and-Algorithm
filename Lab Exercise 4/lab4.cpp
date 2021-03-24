/*by Jurie Mae Castronuevo
from BSCOE 2-6
[February 27, 2021]
*/
#include <iostream>
using namespace std;
int main()
{
    int x(11), y(6), z(22), *p1, *p2;
    p1 = &z;
    p2 = &x;
    cout << "x:" << x << "  y:" << y << "  z:" << z << "  *p1:" << *p1 << "  *p2:" << *p2 << endl;
    *p1 = *p2;
    z = *p1 + 2;
    cout << "x:" << x << "  y:" << y << "  z:" << z << "  *p1:" << *p1 << "  *p2:" << *p2 << endl;
    p2 = p1;
    x = z - y;
    cout << "x:" << x << "  y:" << y << "  z:" << z << "  *p1:" << *p1 << "  *p2:" << *p2 << endl;
    *p1 = y;
    cout << "x:" << x << "  y:" << y << "  z:" << z << "  *p1:" << *p1 << "  *p2:" << *p2 << endl;
    p1 = &y;
    *p1 = y+x;
    cout << "x:" << x << "  y:" << y << "  z:" << z << "  *p1:" << *p1 << "  *p2:" << *p2 << endl;
    x=1; y=2; z=3;
    p1=p2;
    *p2=*p1+x;
    cout << "x:" << x << "  y:" << y << "  z:" << z << "  *p1:" << *p1 << "  *p2:" << *p2 << endl;
    system ("pause>0");
    return 0;
}