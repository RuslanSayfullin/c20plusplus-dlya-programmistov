// fig04_04.cpp
// Расчёт сложных процентов в цикле for
#include <iostream>
#include <iomanip>
#include <cmath>    // Для функции возведения в степень
using  namespace std;

int main() {
    // Устанвливаем формат чисел с плавающей точкой
    //cout << fixed << setpresision(2);

    double principal{10000.00}; // Первоначальный вклад
    double rate{0.05};  // Процентная ставка

    cout << "Initial principal: " << principal << "\n";
    cout << "Interest rate: " << rate << "\n";

    // Выводим заголовок таблицы
    cout << "\nYear" << setw(20) << "Amaunt on deposit" << "\n";

    // Расчитываем сумму на счёте в конце каждого кода из демсяти
    for (int year{1}; year <= 10; ++year) {
        // Расситываем сумму на счёте в конце текущего года
        double amount{principal * pow(1.0 + rate, year)};

        // Выводим на экран год и сумму
        cout << setw(4) << year << setw(20) << amount << "\n";
    }

}