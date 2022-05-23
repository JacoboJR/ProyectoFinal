import win32com
from win32com.client import Dispatch
import os 

def MemoriaTotal():
††† global total_memory2
††† total_memory = os.popen('systeminfo | findstr /C:"Cantidad total de memoria f√≠sica"').read()
††† total_memory2 = total_memory[-10:]
††† total_memory2 = total_memory2.replace("M", "")
††† total_memory2 = total_memory2.replace("B", "")
††† total_memory2 = total_memory2.replace(",", "")


def MemoriaUsada():
††† free_memory = os.popen('systeminfo |find "Memoria f√≠sica disponible"').read()
††† free_memory2 = free_memory[-10:]
††† free_memory2 = free_memory2.replace("M", "")
††† free_memory2 = free_memory2.replace("B", "")
††† free_memory2 = free_memory2.replace(",", "")
††† porciento = (int(free_memory2) * 100) / int(total_memory2)
††† print("RAM memory % used:", 100 - porciento)
††† return 100 - porciento


if _name_ == '_main_':
††† MemoriaTotal()
††† x = MemoriaUsada()
††† while (x < 70):
††††††† w = win32com.client.DispatchEx('Word.Application')
††††††† x = MemoriaUsada()