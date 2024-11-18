// fig06_05.cpp
// Суммирование элементов массива
#include <iostream>
#include<array>
#include<ranges>
#include <format>

int main() {
    std::array items{10, 20, 30, 40};   // Автоопределение типа: array<int, 4>
    int total{0};

    // Суммирование элементов
    fot (const int& item : items) {
        total += item;
    }

    std::cout << fmt::format("Total of array elements: {}\n", total);
}