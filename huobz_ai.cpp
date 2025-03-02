#include <iostream>
#include <string>
#include <unordered_map>
#include <vector>
#include <algorithm>

std::unordered_map<std::string, std::vector<std::string>> responses = {
    {"greeting", {"Hello!", "Hi there!", "Hey! How are you?"}},
    {"wellbeing", {"I'm doing well, thank you!", "I am an AI, but I appreciate the question!"}},
    {"farewell", {"Goodbye!", "See you later!", "Take care!"}},
    {"default", {"I'm still learning. Could you rephrase that?"}}
};

// Function to classify intent
std::string classify_intent(std::string user_input) {
    std::transform(user_input.begin(), user_input.end(), user_input.begin(), ::tolower);
    if (user_input.find("hi") != std::string::npos || user_input.find("hello") != std::string::npos)
        return "greeting";
    else if (user_input.find("how are you") != std::string::npos)
        return "wellbeing";
    else if (user_input.find("bye") != std::string::npos || user_input.find("goodbye") != std::string::npos)
        return "farewell";
    else
        return "default";
}

int main() {
    std::string user_input;
    std::cout << "Huobz AI: Ask me anything! (Type 'exit' to quit)\n";

    while (true) {
        std::cout << "\nYou: ";
        std::getline(std::cin, user_input);
        
        if (user_input == "exit") {
            std::cout << "Huobz AI: Goodbye!\n";
            break;
        }

        std::string intent = classify_intent(user_input);
        std::cout << "Huobz AI: " << responses[intent][rand() % responses[intent].size()] << "\n";
    }

    return 0;
}
