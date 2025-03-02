#include <iostream>
#include <unordered_map>
#include <string>

using namespace std;

int main() {
    unordered_map<string, string> memory;
    string input, response;

    cout << "Huobz AI: Ask me anything..." << endl;

    while (true) {
        cout << "You: ";
        getline(cin, input);

        // Convert input to lowercase
        for (auto &c : input) c = tolower(c);

        // Check if AI already learned this response
        if (memory.find(input) != memory.end()) {
            cout << "Huobz AI: " << memory[input] << endl;
            continue;
        }

        // AI asks for learning
        cout << "Huobz AI: I need more training..." << endl;
        cout << "Huobz AI: What should I say next time? ";
        getline(cin, response);

        // Store new response
        memory[input] = response;
        cout << "Huobz AI: I have learned from you!" << endl;
    }

    return 0;
}
