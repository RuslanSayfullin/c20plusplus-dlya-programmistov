// fig07_14.cpp
// Создание std::array из строкового литера функцией to_array (C++20)
#include <fmt/format.h>
#include <iostream>
#include <array>

int main() {
    // Лямбда-выражение для отоброжения элементов items
    const auto display {
        [](const auto& items) {
            for (const auto& item : items) {
                std::cout << fmt::format("{} ", item);
            }
        }
    };

    // инициализация std::array строковым литералом
    // создаёт одноэлементный array
    const auto array1{std::array{"abc"}};
    std::cout << fmt::format("array1.size() = {}\narray1: ", array1.size());
    display(array1); // используем лямбду для отоброжения содержимого
    // Создаёт из строкового литера массив символов
    const auto array2{std::to_array("C++20")};
    std::cout << fmt::format("\n\narray2.size() = {}\narray2: ", array2.size());
    display(array2);    // используем лямбду для отоброжения содержимого
    std::cout << '\n';
    
}
