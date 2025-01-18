#include <iostream>
#include <cstdlib>
#include <ctime>
#include <unistd.h>
#include <X11/Xlib.h>
#include <X11/keysym.h>
#include <X11/extensions/XTest.h>

// Function to simulate key press
void simulateKeyPress(Display* display, KeyCode keyCode) {
    // Simulate key press
    XTestFakeKeyEvent(display, keyCode, True, CurrentTime);
    XFlush(display);

    // Simulate key release
    XTestFakeKeyEvent(display, keyCode, False, CurrentTime);
    XFlush(display);
}

int main() {
    // Seed the random number generator
    std::srand(std::time(0));

    // Open connection to the X server
    Display* display = XOpenDisplay(nullptr);
    if (!display) {
        std::cerr << "Unable to open X display" << std::endl;
        return 1;
    }

    // Get the key code for F15
    KeyCode f15KeyCode = XKeysymToKeycode(display, XK_F15);
    if (f15KeyCode == 0) {
        std::cerr << "F15 key not found" << std::endl;
        XCloseDisplay(display);
        return 1;
    }

    while (true) {
        // Generate a random sleep time between 10 and 50 seconds
        int sleepTime = 10 + (std::rand() % 41); // 10-50 seconds
        std::cout << "Sleeping for " << sleepTime << " seconds..." << std::endl;
        sleep(sleepTime);

        // Simulate F15 key press
        simulateKeyPress(display, f15KeyCode);
        std::cout << "Had Coffee" << std::endl;
    }

    // Close the display (this will never be reached in this example)
    XCloseDisplay(display);
    return 0;
}