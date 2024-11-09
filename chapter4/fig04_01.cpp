// fig04_01.cpp
// Цикл while со счетчиком (с управляющей переменной)
#include <iostream>
using namespace std;

int main() {
    int counter{1}; // Объявляем и инициалихируем управляющую переменную

    while (counter <= 10) {
        cout << counter << " ";
    ++counter; // Инкремент управляющей переменной
    }

    cout << "\n";
}
