import pyautogui
import subprocess
import time
import pyperclip
import re

# Optional: uniform delay after each step
STEP_DELAY = 2

# Function to parse product text
def parse_product_text(text):
    # Remove the #### delimiters if present
    text = text.strip('#').strip()
    
    # Extract Product Name
    name_match = re.search(r'\*Product Name\*:\s*(.*?)\n', text)
    product_name = name_match.group(1).strip() if name_match else ""
    
    # Extract Product Code
    code_match = re.search(r'Product Code:\s*(\w+)', text)
    product_code = code_match.group(1).strip() if code_match else ""
    
    # Extract Product Description (without label, stop before Product Code)
    desc_match = re.search(r'\*Product Description\*:\s*(.*?)(?=\*Product Details\*|Product Code:|\Z)', text, re.DOTALL)
    product_description = desc_match.group(1).strip() if desc_match else ""
    
    # Extract Product Details (without label, stop before Product Code or Note)
    details_match = re.search(r'\*Product Details\*:\s*(.*?)(?=Product Code:|Note:|\Z)', text, re.DOTALL)
    product_details = details_match.group(1).strip() if details_match else ""
    
    # Extract Note (if present, stop before Product Code)
    note_match = re.search(r'Note:.*?(?=Product Code:|\Z)', text, re.DOTALL)
    note = note_match.group(0).strip() if note_match else ""
    
    # Format the combined description with specific spacing, excluding product code
    combined_description = product_description
    if product_details:
        combined_description += "\n\n" + product_details
    if note:
        combined_description += "\n\n" + note
    
    return product_name, combined_description, product_code

# Wrap pyautogui for automatic delay
def setup_pyautogui_wrappers():
    def delayed(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            time.sleep(STEP_DELAY)
            return result
        return wrapper

    pyautogui.click = delayed(pyautogui.click)
    pyautogui.moveTo = delayed(pyautogui.moveTo)
    pyautogui.dragTo = delayed(pyautogui.dragTo)
    pyautogui.write = delayed(pyautogui.write)

def run_steps(step_list):
    setup_pyautogui_wrappers()
    for step_type, command in step_list:
        if step_type == 'pc':
            print("Running PC command...")
            command()  # Call the lambda function
        elif step_type == 'android':
            print(f"Running ADB: {command}")
            result = subprocess.run(command, shell=True, capture_output=True, text=True)
            if result.returncode != 0:
                print(f"ADB Error: {result.stderr}")
            else:
                print(result.stdout)
            time.sleep(STEP_DELAY)
        elif step_type == 'wait':
            print(f"Waiting for {command} seconds...")
            time.sleep(command)
        elif step_type == 'py':
            print(f"Running Python script: {command}")
            try:
                result = subprocess.run(['python', command], capture_output=True, text=True)
                if result.returncode != 0:
                    print(f"Python Script Error: {result.stderr}")
                else:
                    print(result.stdout)
            except Exception as e:
                print(f"Error running Python script: {e}")
            time.sleep(STEP_DELAY)
        else:
            print(f"Unknown step type: {step_type}")
    print("All steps done.")

if __name__ == '__main__':
    # Enable fail-safe (move mouse to top-left to stop script)
    pyautogui.FAILSAFE = True
    
    # Get product text from clipboard
    product_text = pyperclip.paste()
    
    # Parse the product text
    product_name, combined_description, product_code = parse_product_text(product_text)
    
    # Print extracted values for verification
    print(f"Product Name: {product_name}")
    print(f"Combined Description: {combined_description}")
    print(f"Product Code: {product_code}")
    
    # Step list with mixed types, including the new 'py' step
    steps = [
        ('pc', lambda: pyautogui.click(131, 752)),  # Click to focus browser
        ('wait', 3),
        ('pc', lambda: pyautogui.click(1042, 65)),  # Click address bar
        ('pc', lambda: pyautogui.write('www.google.com')),
        ('pc', lambda: pyautogui.press('enter')),
        ('wait', 10),
        ('pc', lambda: pyautogui.click(58, 677)),  # Navigate to Products
        ('wait', 3),
        ('pc', lambda: pyautogui.click(326, 220)),  # Click Add New Product
        ('wait', 3),
        # product 11111111
        ('android', 'adb shell input tap 182 728'), #open 1st product
        ('wait', 3),
        ('android', 'adb shell input tap 645 934'), #click on download button
        ('wait', 10),
        ('android', 'adb shell input tap 563 1556'), #click on share button in the botton right corner
        ('android', 'adb shell input tap 343 1527'), #click on green color share button
        ('wait', 10), #wait to download all the files to share
        ('android', 'adb shell input swipe 637 1301 128 1296 300'), #swipe to search for local send
        ('android', 'adb shell input tap 267 1174'), #click on local send icon
        ('wait', 2), # wait to open local send with files
        ('android', 'adb shell input tap 326 613'), #click on my windows device
        ('wait', 10), #wait till the transfer completes
        ('pc', lambda: pyautogui.click(2, 2)), # to hide the local send 
        ('android', 'adb shell input swipe 340 1606 343 1321 100'), #go to home screen
        ('android', 'adb shell input swipe 340 1606 343 1321 100'), #again go to home screen
        ('android', 'adb shell input tap 631 1505'), #click on local send
        ('android', 'adb shell input tap 354 1524'), #same send and cancel button in local send
        ('android', 'adb shell input tap 394 223'), #click on paste button in local send
        ('android', 'adb shell input tap 326 613'), #click on my windows device
        ('pc', lambda: pyautogui.click(703, 504)), #it will click copy button on pc adjsted local send buy using the interface of chatgpt
        ('pc', lambda: pyautogui.click(2, 2)), # to hide the local send
        ('android', 'adb shell input swipe 340 1606 343 1321 100'), #go to home screen
        ('android', 'adb shell input swipe 340 1606 343 1321 100'), #again go to home screen
        ('android', 'adb shell input swipe 676 672 165 675 300'), #swipe from right to left
        ('android', 'adb shell input tap 436 429'), #click on markaz app
        ('android', 'adb shell input tap 366 525'), #click to hide sharing options
        ('android', 'adb shell input tap 69 150'), #click on back icon to go back to select 2nd product
        ('pc', lambda: pyautogui.click(246, 268)),  # Click Product Title field
        #('pc', lambda: pyautogui.write(product_name)),  # Paste Product Name
        #('pc', lambda: pyautogui.click(385, 514)),  # Click Product Description field
        #('pc', lambda: pyautogui.write(combined_description)),  # Paste Combined Description
        ('py', r'C:\Users\Admin\Desktop\torunwithin.py'),  # Run the external Python script
        #('pc', lambda: pyautogui.moveTo(1362, 278)),  # Scroll to Inventory tab
        #('pc', lambda: pyautogui.dragTo(1362, 697, duration=0.3)),
        #('pc', lambda: pyautogui.click(550, 427)),  # Click product code section
        #('pc', lambda: pyautogui.write(product_code)),  # Paste Product Code
    ]
    
    # Run the automation steps

    run_steps(steps)
