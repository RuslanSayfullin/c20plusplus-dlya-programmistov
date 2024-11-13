// fig05_03.cpp
// Бросаем кубик 60 миллионов раз
#include <fmt/format.h>
#include <iostream>
#include <random>
using namespace std;

int main() {
    // Инициализируем генератор случайных чисел
    default_random_engine engine{};
    uniform_int_distribution<int> randomDie{l, 6};
    int frequency1{0}; // Количество выпадений числа 1
    int frequency2{0}; // Количество выпадений числа 2
    int frequencyЗ{0}; // Количество выпадений числа 3
    int frequency4{0}; // Количество выпадений числа 4
    int frequency5{0}; // Количество выпадений числа 5
    int frequency6{0}; // Количество выпадений числа 6
    // Собираем результаты 60 миллионов бросков
    for (int roll{l}; roll <= 60'000'000; ++roll) {
        // Получаем случайное число и увеличиваем соответствующий счетчик
        switch (const int face{randomDie(engine)}) {
            case 1:
                ++frequency1; // Увеличиваем счетчик 1
                break;
            case 2:
                ++frequency2; // Увеличиваем счетчик 2
                break;
            case з:
                ++frequencyЗ; // Увеличиваем счетчик 3
                break;
            case 4:
                ++frequency4; // Увеличиваем счетчик 4
                break;
            case 5:
                ++frequency5; // Увеличиваем счетчик 5
                break;
            case 6:
                ++frequency6; // Увеличиваем счетчик 6
                break;
    default: // Если сгенерировано недопустимое значение
    cout « "Prograni should r1ever get here ! ";
    break;
    }
    45
    46}
    47
    48
    49
    50
    51cout « fmt: :format("{:>4}{:>13}\n", "Face", "Frequency"); // Заголовки
    cout « fmt::format("{:>4d}{:>13d}\п", 1, frequencyl)
    « fmt::format("{:>4d}{:>13d}\n", 2, frequency2)
    « fmt::format("{:>4d}{:>13d}\n", 3, frequencyЗ)
    « fmt::format("{:>4d}{:>13d}\n", 4, frequency4)
    « fmt::format("{:)4d}(:>13d}\n", 5, frequencyS)
    « fmt::format("{:>4d}{:>13d}\n", б, frequency6);
}