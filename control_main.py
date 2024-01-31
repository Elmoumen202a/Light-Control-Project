# Import necessary modules
import keyboard
import time

# Define a function to control the light
def control_light():
    # Print instructions for the user
    print("Press Ctrl to control the light. Press 'q' to quit.")
    
    # Infinite loop to continuously check for key presses
    while True:
        # Check if 'Ctrl' key is pressed
        if keyboard.is_pressed('ctrl'):
            # Simulate turning the light on/off
            print("Light ON")
            time.sleep(0.5)  # To avoid rapid toggling, adjust the delay if needed
        # Check if 'q' key is pressed
        elif keyboard.is_pressed('q'):
            # Quit the program when 'q' is pressed
            print("Exiting...")
            break

# Check if the script is being run as the main program
if __name__ == "__main__":
    # Call the control_light function when the script is executed
    control_light()
