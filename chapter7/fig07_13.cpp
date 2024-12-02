// fig07_13.cpp
// Получение аргументов командной строки
#include <fmt/format.h>
#include <iostream>

int main(int argc, char* argv[]) {
    std::cout << fmt::format("Number of arguments: {}\n\n", argc);

    for (int i{0}; i < argc; ++i) {
        std::cout << fmt::format("{}\n", argv[i]);
    }
}