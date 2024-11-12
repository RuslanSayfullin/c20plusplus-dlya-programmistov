// fig 05_01.cpp
// Пользовательская функция maximum c прототипом
#include <iostream>
#include <iomanip>
using namespace std;

int maximum(int x, int y, int z);   // Прототип функции

int main() {
    cout<< "Enter three integer values: ";
    int int1, int2, int3;
    cin >> int1 >> int2 >> int3;

    // Вызовем функцию maximum
    cout << "The maximum integer values is: " << maximum(int1, int2, int3) << "\n";

}

// Функция, возвращающая наибольшее из трех чисел
int maximum(int x, int y, int z) {
    int maximumValue{x};    // Сначала предположим, что число x - наибольшее

    // Проверяем: число y больше, чем maximumValue?
    if (y > maximumValue) {
        maximumValue = y;
    }

    // Проверяем: число z больше, чем maximumValue?
    if (z > maximumValue) {
        maximumValue = z;
    }

    return maximumValue;

}