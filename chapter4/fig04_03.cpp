// fig04_03.cpp
// Суммирование целых чисел в цикле for
#include <iostream>
using namespace std;

int main() {
    int total{0};

    // Суммтрование всех четных чисел от 2 до 20
    for (int number{2}; number <= 20; number +=2) {
        total += number;
    }

    cout << "Sum is " << total << "\n";
}