#include <iostream>
#include <string>

using namespace std;

int main(int argc, char **argv) {

	char str[64];
	int rot;
	std::cout << "Enter a word: ";
	std::cin >> str;
	std::cout << "Enter a rotation (0-25): ";
	std::cin >> rot;

	for (int i = 0; i < strlen(str); i++) {
		char newLetter = tolower(str[i]) + rot;
		if ((int) newLetter > 122) {
			str[i] = 96 + ((int) newLetter - 122);
		} else {
			str[i] = newLetter;
		}
	}
	std::cout << "converted word: " << str << std::endl;
	return 0;
}