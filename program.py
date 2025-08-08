import pyautogui
import time
import pyperclip
# Wait 3 seconds before starting so you can switch to the correct screen
time.sleep(3)

# Step 1: Click the icon at (1030, 1053)
pyautogui.click(x=1030, y=1053)
time.sleep(1)  # wait for the app to open

# Step 2: Drag to select text from (438, 116) to (1897, 967)
pyautogui.moveTo(644, 213)
pyautogui.dragTo(1821,1012, duration=0.5,button='left')  # Smooth drag


# Step 3: Copy selected text (Ctrl + C)
pyautogui.hotkey('ctrl', 'c')
pyautogui.click(1821,1012)
time.sleep(0.5)

# Step 4: Get copied text from clipboard
copied_text = pyperclip.paste()

# Step 5: Print or use the variable
print("Copied Text:")
print(copied_text)
