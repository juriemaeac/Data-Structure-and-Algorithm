
#include <iostream>
using namespace std;

//Certificate of Deposit Account Structure
struct CDAccount{
    double balance;
    double interestRate;
    int term;

};

CDAccount doubleInterest(CDAccount oldAccount);

void accountBalance(CDAccount& _account);

int main()
{
    CDAccount account;

    cout << "Enter account blance: PhP ";
    cin >> account.balance;
    cout << "Enter account interest: ";
    cin >> account.interestRate;
    cout << "Enter the number of months until maturity: ";
    cin >> account.term;

    accountBalance(account);

    cout << "\nOld Account \n"
            << "When your CD matures in "
            << account.term << " months,\n"
            << "it will have a balance of PhP"
            << account.balance << endl;

    CDAccount accountNew;
    accountNew = doubleInterest(account);

    accountBalance(accountNew);

    cout << "\nNew Account \n"
            << "When your CD matures in "
            << accountNew.term << " months,\n"
            << "it will have a balance of PhP"
            << accountNew.balance << endl;

    system("pause > 0");
    return 0;
}

void accountBalance(CDAccount& _account)
{
    double rateFraction, interest;
    rateFraction = _account.interestRate/100.0;
    interest = _account.balance*(rateFraction*(_account.term/12.0));
    _account.balance = _account.balance + interest;

}

CDAccount doubleInterest(CDAccount oldAccount)
{
    CDAccount temp;
    temp = oldAccount;
    temp.interestRate = 2*oldAccount.interestRate;
    return temp;
}