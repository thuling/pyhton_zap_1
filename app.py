import pywhatkit
import keyboard
import time
from datetime import datetime

contatos = ['+5581985057129']

while len(contatos) >= 1:
    pywhatkit.sendwhatmsg(contatos[0],'TESTE PYTHON', datetime.now().hour, datetime.now().minute + 1)
    del contatos[0]
    time.slep(10)
    keyboard.press_and_release('ctrl')