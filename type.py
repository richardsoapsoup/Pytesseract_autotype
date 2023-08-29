import pyscreenshot as ImageGrab
import time
import cv2
import numpy as nm
import keyboard
import pyautogui
import pytesseract
from PIL import Image
# part of the screen
achar = False
lig = True

while True:    
    if keyboard.is_pressed('0'):
        achar = True

    if keyboard.is_pressed('1'):
        lig = False
                           
        
    def pegarImagem():
        
        pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract'
        while achar == True:        
                    
            time.sleep(2)
            im=ImageGrab.grab(bbox=(200,320,1200,500))            
            texto = pytesseract.image_to_string(
                        cv2.cvtColor(nm.array(im), cv2.COLOR_BGR2GRAY), 
                        lang ='eng')
            texto = texto.replace("\n", " ")
            pyautogui.write(texto, interval = 0.02)
            break

    def pegarImagem2():
        
        pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files (x86)\\Tesseract-OCR\\tesseract'
        while achar == True:                    
           
            im=ImageGrab.grab(bbox=(200,360,1200,500))            
            texto = pytesseract.image_to_string(
                        cv2.cvtColor(nm.array(im), cv2.COLOR_BGR2GRAY), 
                        lang ='eng')
            texto = texto.replace("\n", " ")
            pyautogui.write(texto, interval = 0.02)
            break

    if lig == False:
        break
                

          
    pegarImagem()
    pegarImagem2()


