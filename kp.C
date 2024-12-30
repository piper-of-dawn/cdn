#include <windows.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>
#include <unistd.h> // For sleep function
#include <conio.h> // For _kbhit and _getch
// Function to simulate F16 key press
void pressF16Key() {
    // Create a key press event
    INPUT input = {0};
    input.type = INPUT_KEYBOARD;
    input.ki.wVk = VK_F16; // Virtual key code for F16

    // Simulate key press
    SendInput(1, &input, sizeof(INPUT));

    // Simulate key release
    input.ki.dwFlags = KEYEVENTF_KEYUP;
    SendInput(1, &input, sizeof(INPUT));
}

int main() {
    srand((unsigned int)time(NULL));
    printf("Starting F16 key presser... Press 'q' to quit.\n");

    while (1) {
        if (_kbhit()) { // Check for keyboard input
            char c = _getch();
            if (c == 'q' || c == 'Q') {
                printf("Exiting F16 key presser.\n");
                break;
            }
        }

        int randomSeconds = rand() % 15 + 12;
        printf("Pressing F16 key. Next press in %d seconds.\n", randomSeconds);
        pressF16Key();
        sleep(randomSeconds);
    }
    return 0;
}
