# Keyboard Listener Project

This Python script listens for keyboard events and performs actions based on the keys pressed.

## Features

- Listens for keyboard events in a separate thread.
- Prints the current position of the mouse cursor when the space bar is pressed.
- Stops the keyboard listener and terminates the program when the 'esc' key is pressed.

## Usage

Run the `main.py` script:

```bash
python main.py
```

Press the space bar to print the current position of the mouse cursor. Press the 'esc' key to stop the script.

## Dependencies

This project uses the `pynput` and `pyautogui` libraries. Install them with pip:

```bash
pip install pynput pyautogui
```
