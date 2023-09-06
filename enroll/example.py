import random
from PIL import ImageGrab
import pyautogui
import pybase64
import pygetwindow as gw
from PIL import ImageGrab

# Get the active window


 

def random_number():
    return random.randint(1, 10)

def Screenshot2(request):
    screen_width, screen_height = pyautogui.size()
    screenshot = ImageGrab.grab(bbox=(0, 0, screen_width, screen_height))
    screenshot.save("screenshot1.png")
    print(screenshot)
    screenshot_bytes = screenshot.tobytes() 
    # Encode the bytes as a base64 string
    screenshot_base64 = pybase64.b64encode(screenshot_bytes).decode('utf-8') 
    print(screenshot_base64) 

def Screenshot(request):
    active_window = gw.getWindowsWithTitle(gw.getActiveWindowTitle())[0]

    # Get the coordinates of the active window
    left, top, right, bottom = active_window.left, active_window.top, active_window.right, active_window.bottom

    # Capture the active screen
    screenshot = ImageGrab.grab(bbox=(left, top, right, bottom))

    # Save the screenshot to a file (optional)
    screenshot.save('screenshot.png')

    # Display the screenshot (optional)
    screenshot.show()

    print(screenshot)
    screenshot_bytes = screenshot.tobytes() 
    # Encode the bytes as a base64 string
    screenshot_base64 = pybase64.b64encode(screenshot_bytes).decode('utf-8') 
    print(screenshot_base64) 

