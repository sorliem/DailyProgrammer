#include <iostream>

using namespace std;

int genBinary(int n) {
	if (n == 0) {
		return 0;
	} else {
		return (n % 2 + 10 * genBinary(n / 2));
	}
}

int main(int argc, char** argv) {
	
	int num;
	std::cout << "Decimal to binary converter." << std::endl;
	std::cout << "Enter a number (under 1,023 please): ";
	std::cin >> num;
	std::cout << "You entered " << num << std::endl;
	int ans = genBinary(num);
	std::cout << "ans = " << std::to_string(ans) << std::endl;
	return 0;
}