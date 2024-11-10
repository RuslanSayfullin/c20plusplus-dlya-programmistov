// fig04_05.cpp
// Цикл do...while
#include <iostream>
using namespace std;

int main() {
    int counter{1};

    do {
        cout << counter << " ";
        ++counter;
    } while (counter <= 10);    // Конец цикла

    cout << "\n";
}
