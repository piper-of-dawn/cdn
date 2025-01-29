#include <iostream>
#include <cstdlib>
#include <ctime>
#include <windows.h>

// Function to simulate key press
void simulateKeyPress(WORD keyCode) {
    // Simulate key down
    keybd_event(keyCode, 0, 0, 0);
    // Simulate key up
    keybd_event(keyCode, 0, KEYEVENTF_KEYUP, 0);
}

int main() {
    // Seed the random number generator
    std::srand(std::time(0));

    // Virtual key code for F15
    WORD f15KeyCode = VK_F15;

    while (true) {
        // Generate a random sleep time between 10 and 50 seconds
        int sleepTime = 10 + (std::rand() % 41); // 10-50 seconds
        std::cout << "Sleeping for " << sleepTime << " seconds..." << std::endl;
        Sleep(sleepTime * 1000); // Sleep uses milliseconds

        // Simulate F15 key press
        simulateKeyPress(f15KeyCode);
        std::cout << "Had Coffee" << std::endl;
    }

    return 0;
}
