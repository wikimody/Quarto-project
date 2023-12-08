#include <iostream>

using namespace std;

int main(int argc, char *argv[]) {
    // Extract the name from the command-line argument
    string name = argv[1];

    // Output the greeting
    cout << "Hello, " << name << "!" << endl;

    return 0;
}
