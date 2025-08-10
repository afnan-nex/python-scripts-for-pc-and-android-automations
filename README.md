# **PyAutoGUI Command Generator**

A web-based tool for generating **PyAutoGUI** commands from screenshots or videos, paired with a Python script for automating product data entry using PyAutoGUI and ADB.

## **📖 Table of Contents**

*   Overview
*   Features
*   Prerequisites
*   Installation
*   Usage
    *   Web Interface
    *   Python Automation Script
*   How It Works
*   Contributing
*   License

## **🌟 Overview**

This project combines two powerful components:

*   **Web Interface** – Generate PyAutoGUI commands by interacting with uploaded media.
*   **Python Script** – Automate product data entry with PyAutoGUI for PC and ADB for Android.

Not just for simple tasks, this tool supports **complex automation workflows** across PC and mobile devices.

## **✨ Features**

### **Web Interface**

*   Upload screenshots or videos to create PyAutoGUI commands.
*   Interaction modes: **Tap, Swipe, Hold, Keyboard, Hotkey**.
*   Visual feedback for swipe and hold with custom durations.
*   Copy raw or formatted commands to clipboard.
*   Clear or format commands for script integration.

### **Python Script**

*   Parses product data (name, description, code) from clipboard.
*   Automates browser tasks with PyAutoGUI.
*   Controls Android devices via ADB commands.
*   Runs external Python scripts in the workflow.
*   Configurable delays for reliable execution.

## **🛠 Prerequisites**

### **Web Interface**

*   A modern browser (Chrome, Firefox, Edge, etc.).

### **Python Script**

*   Python 3.6+.
*   Required packages:  
    pip install pyautogui pyperclip
*   ADB (Android Debug Bridge) installed and configured.
*   Android device with USB debugging enabled.
*   PyAutoGUI fail-safe enabled (move mouse to top-left to stop).

## **⚙️ Installation**

Clone the repository:  
git clone https://github.com/yourusername/pyautogui-command-generator.git

1.  cd pyautogui-command-generator

Install Python dependencies:  
```
pip install -r requirements.txt
```
**requirements.txt**:  
pyautogui

1.  pyperclip
2.  Install ADB and add to system PATH:
    *   Download from Android Developer site.
    *   Enable USB debugging on your Android device.

## **🚀 Usage**

### **Web Interface**

1.  Open index.html in a browser.
2.  Upload a screenshot or video.
3.  Choose an interaction mode:
    *   **Tap**: Click to generate pyautogui.click(x, y).
    *   **Swipe**: Drag for pyautogui.moveTo and pyautogui.dragTo.
    *   **Hold**: Click for mouse hold with duration.
    *   **Keyboard**: Press a key and click Add for pyautogui.press.
    *   **Hotkey**: Enter two keys for pyautogui.hotkey.
4.  Copy commands with **Copy** or format with **Format**.
5.  Clear commands with **Clear**.

### **Python Automation Script**

1.  Connect your Android device and configure ADB.

Copy product text to clipboard:  
```
\*Product Name\*: Example Product

\*Product Description\*: Sample description.

\*Product Details\*: Product details.
```
Note: Additional notes.

1.  Product Code: ABC123
2.  Update steps in automation.py with web interface commands.
3.  Run the script:  
    python automation.py  
    The script will:
    *   Parse clipboard text.
    *   Execute PyAutoGUI commands (PC).
    *   Run ADB commands (Android).
    *   Execute external Python scripts.

## **🔍 How It Works**

### **Web Interface**

*   Built with HTML, CSS, and JavaScript.
*   Scales coordinates to match original media resolution.
*   Generates commands in a list, with copy or format as tuples.

### **Python Script**

*   Uses pyperclip to read clipboard text.
*   Parses data with regex.
*   Adds delays to PyAutoGUI for reliability.
*   Supports PC (PyAutoGUI), Android (ADB), wait, and Python script steps.

## **🤝 Contributing**

1.  Fork the repository.
2.  Create a branch: git checkout -b feature-name.
3.  Commit changes: git commit -m "Add feature".
4.  Push branch: git push origin feature-name.
5.  Open a pull request with a clear description.

## **📜 License**

### **MIT License. See LICENSE for details.**

# **PyAutoGUI Command Generator**

A web-based tool for generating **PyAutoGUI** commands from screenshots or videos, paired with a Python script for automating product data entry using PyAutoGUI and ADB.

## **📖 Table of Contents**

*   Overview
*   Features
*   Prerequisites
*   Installation
*   Usage
    *   Web Interface
    *   Python Automation Script
*   How It Works
*   Contributing
*   License

## **🌟 Overview**

This project combines two powerful components:

*   **Web Interface** – Generate PyAutoGUI commands by interacting with uploaded media.
*   **Python Script** – Automate product data entry with PyAutoGUI for PC and ADB for Android.

Not just for simple tasks, this tool supports **complex automation workflows** across PC and mobile devices.

## **✨ Features**

### **Web Interface**

*   Upload screenshots or videos to create PyAutoGUI commands.
*   Interaction modes: **Tap, Swipe, Hold, Keyboard, Hotkey**.
*   Visual feedback for swipe and hold with custom durations.
*   Copy raw or formatted commands to clipboard.
*   Clear or format commands for script integration.

### **Python Script**

*   Parses product data (name, description, code) from clipboard.
*   Automates browser tasks with PyAutoGUI.
*   Controls Android devices via ADB commands.
*   Runs external Python scripts in the workflow.
*   Configurable delays for reliable execution.

## **🛠 Prerequisites**

### **Web Interface**

*   A modern browser (Chrome, Firefox, Edge, etc.).

### **Python Script**

*   Python 3.6+.
*   Required packages:  
    pip install pyautogui pyperclip
*   ADB (Android Debug Bridge) installed and configured.
*   Android device with USB debugging enabled.
*   PyAutoGUI fail-safe enabled (move mouse to top-left to stop).

## **⚙️ Installation**

Clone the repository:  
git clone https://github.com/afnan-nex/python-scripts-for-pc-and-android-automations.git

1.  cd pyautogui-command-generator

Install Python dependencies:  
```
pip install -r requirements.txt
``` 
**requirements.txt**:  
pyautogui

1.  pyperclip
2.  Install ADB and add to system PATH:
    *   Download from Android Developer site.
    *   Enable USB debugging on your Android device.

## **🚀 Usage**

### **Web Interface**

1.  Open index.html in a browser.
2.  Upload a screenshot or video.
3.  Choose an interaction mode:
    *   **Tap**: Click to generate pyautogui.click(x, y).
    *   **Swipe**: Drag for pyautogui.moveTo and pyautogui.dragTo.
    *   **Hold**: Click for mouse hold with duration.
    *   **Keyboard**: Press a key and click Add for pyautogui.press.
    *   **Hotkey**: Enter two keys for pyautogui.hotkey.
4.  Copy commands with **Copy** or format with **Format**.
5.  Clear commands with **Clear**.

### **Python Automation Script**

1.  Connect your Android device and configure ADB.

Copy product text to clipboard:  
'''
\*Product Name\*: Example Product

\*Product Description\*: Sample description.

\*Product Details\*: Product details.
'''
Note: Additional notes.

1.  Product Code: ABC123
2.  Update steps in automation.py with web interface commands.
3.  Run the script:  
    python automation.py  
    The script will:
    *   Parse clipboard text.
    *   Execute PyAutoGUI commands (PC).
    *   Run ADB commands (Android).
    *   Execute external Python scripts.

## **🔍 How It Works**

### **Web Interface**

*   Built with HTML, CSS, and JavaScript.
*   Scales coordinates to match original media resolution.
*   Generates commands in a list, with copy or format as tuples.

### **Python Script**

*   Uses pyperclip to read clipboard text.
*   Parses data with regex.
*   Adds delays to PyAutoGUI for reliability.
*   Supports PC (PyAutoGUI), Android (ADB), wait, and Python script steps.

## **🤝 Contributing**

1.  Fork the repository.
2.  Create a branch: git checkout -b feature-name.
3.  Commit changes: git commit -m "Add feature".
4.  Push branch: git push origin feature-name.
5.  Open a pull request with a clear description.

## **📜 License**

### **MIT License. See LICENSE for details.**
