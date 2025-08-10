# **Python Scripts for PC and Android Automations**

This repository contains Python scripts and HTML-based tools for automating interactions on both PC and Android devices using pyautogui for PC automation and ADB (Android Debug Bridge) for Android automation. The tools provided include a web-based interface for generating ADB and PyAutoGUI commands by interacting with screenshots or videos, and a Python script for automating tasks such as product data entry and file transfers between Android and PC.

## **Features**

*   **ADB Command Generator**: A web interface that allows users to upload a screenshot or video of an Android device, select interaction modes (tap, swipe, hold), and generate corresponding ADB commands for automation.
*   **PyAutoGUI Command Generator**: A similar web interface for generating PyAutoGUI commands for PC automation, supporting tap, swipe, hold, keyboard, and hotkey interactions.
*   **Automation Script**: A Python script (main.py) that combines pyautogui and ADB commands to automate tasks like navigating websites, entering product data, and transferring files between an Android device and a PC.
*   **Product Text Parsing**: The Python script parses product information from clipboard text, extracting fields like product name, description, and code for use in automation.

## **Prerequisites**

To use the tools and scripts in this repository, ensure you have the following:

*   **Python 3.x** installed on your PC.

**Required Python libraries**:  
pip install pyautogui pyperclip

*   **ADB (Android Debug Bridge)** installed and configured on your system. Ensure your Android device is connected and USB debugging is enabled.
*   A modern web browser (e.g., Chrome, Firefox) to run the HTML-based command generators.
*   A local server (e.g., python -m http.server) to serve the HTML files, as clipboard functionality requires HTTPS or localhost.

## **Installation**

Clone this repository:  
  
git clone https://github.com/afnan-nex/python-scripts-for-pc-and-android-automations.git

cd python-scripts-for-pc-and-android-automations

Install the required Python libraries:  
  
pip install pyautogui pyperclip

1.  Ensure ADB is installed and your Android device is connected:  
    *   Download and install ADB from the [Android Developer site](https://developer.android.com/tools/releases/platform-tools).
    *   Enable USB debugging on your Android device and connect it to your PC.

Verify the connection by running:  
adb devices

## **Usage**

### **1\. ADB Command Generator**

The adb\_command\_generator.html file provides a web interface to generate ADB commands for Android automation.

*   **How to use**:  
    

Serve the HTML file using a local server:  
python -m http.server 8000

*   *   Open http://localhost:8000/adb\_command\_generator.html in your browser.
    *   Upload a screenshot or video of your Android device's screen.
    *   Select an interaction mode (Tap, Swipe, or Hold) and interact with the media to generate ADB commands.
    *   Use the "Copy" button to copy commands or "Format" to generate a Python-compatible list of commands for use in scripts.
*   **Features**:  
    *   Supports tap, swipe, and hold interactions.
    *   Visual feedback for swipe and hold actions.
    *   Adjustable swipe and hold durations.
    *   Copy commands as plain text or formatted as a Python list.

### **2\. PyAutoGUI Command Generator**

The pyautogui\_command\_generator.html file provides a web interface to generate PyAutoGUI commands for PC automation.

*   **How to use**:  
    

Serve the HTML file:  
python -m http.server 8000

*   *   Open http://localhost:8000/pyautogui\_command\_generator.html in your browser.
    *   Upload a screenshot or video of your PC screen.
    *   Select an interaction mode (Tap, Swipe, Hold, Keyboard, or Hotkey) and interact with the media or input fields to generate PyAutoGUI commands.
    *   Copy or format the commands as needed.
*   **Features**:  
    *   Supports tap, swipe, hold, keyboard, and hotkey interactions.
    *   Visual feedback for swipe and hold actions.
    *   Key capture for keyboard and hotkey inputs.
    *   Formatted output for integration into Python scripts.

### **3\. Automation Script (main.py)**

The main.py script automates tasks by combining PC and Android interactions, such as navigating a website, entering product data, and transferring files.

*   **How to use**:  
    *   Ensure your Android device is connected via ADB and USB debugging is enabled.
    *   Copy product text (formatted with Product Name, Product Description, Product Details, etc.) to your clipboard.
    *   Edit the steps list in main.py to customize the automation steps (e.g., coordinates, commands).

Run the script:  
python main.py

*   **Features**:  
    *   Parses product text from the clipboard using regex.
    *   Executes a sequence of PC (pyautogui), Android (adb), wait, and Python script steps.
    *   Includes a fail-safe: move the mouse to the top-left corner to stop the script.
    *   Adds a uniform delay (STEP\_DELAY) between steps for stability.

**Example Step List**:  
  
steps = \[

('pc', lambda: pyautogui.click(131, 752)), # Click to focus browser

('android', 'adb shell input tap 182 728'), # Tap on Android app

('wait', 3), # Wait for 3 seconds

('py', r'C:\\Users\\Admin\\Desktop\\torunwithin.py'), # Run external Python script

\]

## **Notes**

*   **Security**: The HTML command generators require a secure context (HTTPS or localhost) for clipboard functionality. Use a local server to test.
*   **Coordinates**: The generated coordinates are based on the uploaded media's resolution. Ensure the media matches the actual device or screen resolution for accurate automation.
*   **Customization**: Modify the steps list in main.py to adapt the automation to your specific use case. Use the command generators to obtain accurate coordinates and commands.
*   **Dependencies**: Ensure external Python scripts referenced in the steps list (e.g., torunwithin.py) exist and are accessible.

## **Contributing**

Contributions are welcome! Please open an issue or submit a pull request with improvements or bug fixes.

## **License**

This project is licensed under the MIT License. See the [LICENSE](https://grok.com/chat/LICENSE) file for details.
