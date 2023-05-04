import webbrowser
import datetime
import time

# URL 
url = "https://sia.estacio.br/sianet/Logon"

# Hora
hora = datetime.time(hour=21, minute=50)  

while True:
    agora = datetime.datetime.now().time()
    if agora >= hora:
        break
    time.sleep(60)

webbrowser.open(url)