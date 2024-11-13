// fig05_02.cpp
// Генерация случайных целых чисел ы диапозоне от 1 до 6
#include <iostream>
#include <random>   // Средства генерации случайных чисел, введенные в C++11
using namespace std;

int main() {
    // механизм генерации случайных чисел
    default_random_engine engine{};

    // функция распределения случайных чисел (равновероятное int от 1 до 6)
    uniform_int_distribution<int> randomDie{1, 6};

    // Показывает результаты 10 бросков кубика
    for (int counter{1}; counter <= 10; ++counter) {
        cout << randomDie(engine) << " ";
    }
    cout << '\n';
}