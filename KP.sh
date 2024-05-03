#!/bin/bash

while true; do
    # Generate a random number between 1 and 10 (adjust the range as needed)
    random_interval=$(( (RANDOM % 10) + 1 ))
    
    # Sleep for the random interval
    sleep $random_interval
    
    # Simulate pressing the F15 key using xdotool
    xdotool key F15
done

