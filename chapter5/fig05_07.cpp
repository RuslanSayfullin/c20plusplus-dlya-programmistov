// fig05_07.cpp
// inline-функция, вычисляющая обьем куба
#include <iostream>
using namespace std;

// Определение функции cube предшествует ее вызову,
// поэтому прототип не нужен, строка определения функции
// выступает в качестве прототипа
inline double cube(double side) {
    return side * side * side;  // Вычисляем обьём куба
}

int main() {
    double sideValue;   // Сторона куба
    cout << "Enter the side length of your cube: ";
    cin >> sideValue;   // Считываем число, введенное пользователем

    // Вычисляем объём куба и выводим результат
    cout << "Volune of cube with side " << sideValue << " is " << cube(sideValue) << "\n";
}