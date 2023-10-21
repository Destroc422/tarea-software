import pyautogui
import time
import subprocess

# Abre Notepad (o la aplicación que desees)
subprocess.Popen(["notepad.exe"])

# Espera un momento para que Notepad se abra
time.sleep(2)

# Escribe un mensaje en Notepad
mensaje = "¡Hola, esto es una automatización desde Visual Studio Code!"
pyautogui.typewrite(mensaje, interval=0.1)  # Intervalo de escritura

# Guarda el archivo
pyautogui.hotkey('ctrl', 's')
time.sleep(1)

# Escribe un nombre de archivo
nombre_archivo = "mi_archivo.txt"
pyautogui.typewrite(nombre_archivo, interval=0.1)
time.sleep(1)

# Confirma el nombre del archivo
pyautogui.press('enter')
time.sleep(1)

# Cierra Notepad
pyautogui.hotkey('alt', 'f4')

# Confirmación de cierre (si aparece)
# pyautogui.press('enter')
