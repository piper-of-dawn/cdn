import pyautogui
import time
import random

while True:
    # Generate a random number between 1 and 10 (adjust the range as needed)
    random_interval = random.randint(1, 10)

    # Sleep for the random interval
    time.sleep(random_interval)
    print("KP")

    # Simulate pressing the F15 key
    pyautogui.press("f15")
