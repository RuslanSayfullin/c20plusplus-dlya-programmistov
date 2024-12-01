// fig07_01.cpp
// Пример работы с операторами & и *
#include <iostream>
using namespace std;

int main() {
    constexpr int a{7}; // Инициализируем переменную a значением 7
    const int* aPtr{&a};// Инициализируем aPtr адресом переменной a

    cout << "The address of a is: " << &a 
    << "\nThe address of aPtr is: " << aPtr << "\n";
    cout << "The value of a is: " << a
    << "\nThe value of *aPtr is: " << *aPtr << "\n";
}