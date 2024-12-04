// fig08_03.cpp
// Создание подстроки
#include <iostream>
#include <string>

int main() {
    const std::string s{"airplane"};
    std::cout << s.substr(3, 4) << '\n';    // Получаем подстроку "plan"
}