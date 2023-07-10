import webbrowser
import pyperclip
import pyautogui
import time

Path = input("Enter the path of the code that you want to traslate: ")
OldLanguaje = str(input("Enter the old languaje: "))
NewLanguaje = str(input("Enter the new languaje: "))

Text = "Traslate this code from "+OldLanguaje+" to "+NewLanguaje+":"
OldFile = open(Path,'r')
OldCode = OldFile.read()
pyperclip.copy(OldCode)

webbrowser.open_new("https://chat.openai.com/")
time.sleep(3)
pyautogui.press("backspace") #Quit traslate alert
pyautogui.write(Text)
pyautogui.hotkey('shift', 'enter')
pyautogui.hotkey('ctrl', 'v')
pyautogui.press("enter")