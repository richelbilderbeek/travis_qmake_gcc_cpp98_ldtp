#include <iostream>

int main() {
  std::cout << "Please type something and press enter:\n";
  std::string s;
  std::getline(std::cin, s);
  std::cout << "You typed '" << s << "'\n";
}
