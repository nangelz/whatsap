# whatsap

## Descripción general

`whatsap` es un proyecto simple de automatización con Python que envía mensajes repetidos a través del campo de texto activo en cualquier aplicación (por ejemplo, WhatsApp Web, Telegram o cualquier chat con foco de entrada). El script hace uso de la librería `pyautogui` para escribir y enviar mensajes automáticamente.

## Archivo principal

- `MeAuto.py`: script principal que solicita datos de usuario, espera un pequeño tiempo de preparación y luego envía mensajes de forma iterativa.

## Requisitos

- Python 3
- Librería `pyautogui`

Instalación:

```bash
pip install pyautogui
```

## Cómo usarlo

1. Abre el chat objetivo (por ejemplo, WhatsApp Web en el navegador).
2. Ejecuta:

```bash
python MeAuto.py
```

3. Ingresa:
- `Cantidad de mensajes`: número total de mensajes a enviar.
- `Mensaje`: texto a enviar (puede incluir emojis y caracteres especiales).
- `Delay entre mensajes`: segundos de espera entre envíos.

4. Coloca el cursor de texto en el campo de entrada del chat.
5. El script empieza en 3 segundos y comienza a enviar.

## Funcionamiento del código

1. Importa `pyautogui` como `pt` y `time`.
2. Pide al usuario:
   - `limit` (número de mensajes).
   - `message` (mensaje a enviar).
   - `delay` (espera en segundos entre cada envío).
3. Muestra un mensaje de preparación y espera 3 segundos.
4. En un bucle `while` hasta `limit`:
   - `pt.write(message, interval=0.05)` escribe el mensaje en el campo activo.
   - `time.sleep(float(delay))` espera antes de enviar.
   - `pt.press("enter")` envía el mensaje.
   - `time.sleep(0.2)` breve pausa post-envío.
   - Incrementa el contador.
5. Al terminar, imprime una confirmación: `¡Completado! Se enviaron {i} mensajes.`

## Nota de seguridad y uso responsable

- Solo envía mensajes a contactos que permitan recibirlos.
- No uses el script para spam o actividades que violen los términos de servicio de la plataforma.
- El enfoque automatizado depende de que el campo de texto esté activo y visible.

