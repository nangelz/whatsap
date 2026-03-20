import pyautogui as pt
import time

limit = input("Cantidad de mensajes: ")
message = input("Mensaje: ")
delay = input("Delay entre mensajes (segundos): ")
i = 0

print("El script iniciará en 3 segundos... ¡Prepárate!")
time.sleep(3)

while i < int(limit):
    pt.write(message, interval=0.05)  # write() maneja mejor caracteres especiales
    time.sleep(float(delay))  # Espera entre cada mensaje
    pt.press("enter")
    time.sleep(0.2)  # Pequeña pausa después de enter
    i += 1

print(f"¡Completado! Se enviaron {i} mensajes.")
