#include <iostream>
using namespace std;
int main()
{
    int i = 0;
    FILE *fp = NULL;
    //create a file
    fp = fopen("sample.txt", "w");
    if(!fp)
    {
        cout << "cannot open file.\n";
        system("pause");
        exit(1);
    }
    //Write A to Z in file
    for(i =65 ; i <= 90 ; i++)
    {
        fputc(i, fp);
        //fputc('c', fp);
    }
    //close the file
    fclose(fp);
    
    return 0;
}