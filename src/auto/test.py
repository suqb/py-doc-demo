import pyautogui

# image_path = 'F:/workspace/python/doc_demo/src/auto/google.png'
image_path = './google.png'

try:
    x, y = pyautogui.locateOnScreen(image_path)
except pyautogui.ImageNotFoundException:
    print('未找到指定图像')
