// fig04_02.cpp
// Цикл fot со счетчиком (с управляющей переменной)
#include <iostream>
using namespace std;

int main() {
    for (int counter{1}; counter <= 10; ++counter) {
        cout << counter << " ";
    }

    cout << "\n";
}