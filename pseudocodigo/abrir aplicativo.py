
import pyautogui
import time

# Abrir o bloco de notas
pyautogui.press("win")
time.sleep(3)
pyautogui.write("notepad")
time.sleep(3)
pyautogui.press("enter")

# Esperar o bloco de notas abrir
time.sleep(8)

# Digitar o texto
pyautogui.write("i love you")