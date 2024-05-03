while ($true) {
    # Generate a random number between 1 and 10 (adjust the range as needed)
    $randomInterval = Get-Random -Minimum 1 -Maximum 11
    
    # Sleep for the random interval
    Start-Sleep -Seconds $randomInterval
    echo "Pressing"
    # Simulate pressing the F15 key using SendKeys
    [System.Windows.Forms.SendKeys]::SendWait("{F15}")
}
