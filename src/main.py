from pynput.keyboard import Listener as KeyboardListener
from pyautogui import position as cursor_position
import threading
import time

# Create an event to signal the main thread to stop
stop_event = threading.Event()


def handle_space_bar_press(key: str) -> bool | None:
    """
    This function is called whenever a key press event is detected.
    If the key pressed is the space bar, it gets the current position of the mouse cursor
    and prints it in a formatted string.

    :param key: The key that was pressed

    :return: False if the key pressed was the escape key, None otherwise


    NOTE:
        This function runs in a separate thread from the main thread.
        If the 'esc' key is pressed, it signals the main thread to stop by setting
        the stop_event, and stops the listener by returning False.
    """
    if str(key) == "Key.esc":
        # Stop listener and signal main thread to stop
        stop_event.set()
        return False

    elif str(key) == "Key.space":
        cursor_pos = cursor_position()
        print(f"\t# The cursor is at: (x={cursor_pos[0]}, y={cursor_pos[1]})")


def start_keyboard_listener():
    """
    This function starts a keyboard listener that listens for key press events.
    The listener runs in a separate thread and calls the handle_space_bar_press function
    every time a key is pressed.

    Note:
        It uses a separate thread to avoid blocking the main thread that listens for
        the keyboard interrupt signal (Ctrl + C).
    """
    with KeyboardListener(on_press=handle_space_bar_press) as listener:
        print("==> [Started listening for coordinates input]")
        listener.join()


if __name__ == "__main__":
    # Create a new thread that runs the keyboard listener
    keyboard_listener_thread = threading.Thread(target=start_keyboard_listener)
    keyboard_listener_thread.daemon = True  # Make the listener thread a daemon thread
    keyboard_listener_thread.start()

    try:
        # Infinite loop to keep the main thread running
        while not stop_event.is_set():
            time.sleep(1)  # Reduce CPU usage
    except Exception as unexpected_error:
        print(f"==> [An error occurred]: {unexpected_error}")
    finally:
        print("==> [Stopped listening for coordinates input]")
