// fig05_06.cpp
// Пример области видимости
#include <iostream>
using namespace std;

void useLocal();    // Прототип функции
void useStaticLocal();  // Прототип функции
void useGlobal;  // Прототип функции

int x{1};   // Глобальная переменная

int main() {
    cout << "global x in main is " << x << "\n";

    const int x{5}; // Локальная переменная
    cout << "local x is main's outer scope is " << x << "\n";

    { // Внутренний блок создаёт новую область видимости
        const int x{7}; // переменная скрывает ранее обьявленные переменные
        cout << "local x is main's inner scope is " << x << "\n";
    }
    cout << "local x is main's outer scope is " << x << "\n";

    uselocal(); // Функция с локальной переменной х
    useStaticLocal(); // Функция с локальной статической переменной х
    useGlobal(); // Функция, использующая глобальную переменную х
    uselocal(); // Функция заново инициализирует свою локальную переменную х
    useStaticlocal(); // Локальная статическая переменная х сохраняет значение
    useGlobal(); // Глобальная переменная х сохраняет значение
    cout << "\nlocal х in main ls "<< х << '\n';
}

// uselocal инициализирует переменную х при каждом вызове
void uselocal() {
    int х{25}; // Инициализация при каждом вызове функции
    cout << "\n1oca1 х is" << х << "on eпtering uselocal\n";
    ++x;
    cout << "local х is " << х << " оп ex.itiпg useloca1\n";

}

// Функция useStaticLocal инициализирует статическую локальную переменную х
// только при своем первом вызове; значение переменной сохраняется между вызовами функции
void useStaticlocal() {
    static int x{50}; // Инициализация только при первом вызове функции
    cout << "\nlocal static х is " << x << " on eпtering useStaticLocal\n";
    ++x;
    cout << "local static х is" << x << " on exiting useStaticLocal\n";
}

// useGlobal изменяет глобальную переменную х при каждом вызове
void useGlobal() {
    cout << "\nglobal х i~ " << x << " on ent:ering useGlobal \n";
    x *=10;
}