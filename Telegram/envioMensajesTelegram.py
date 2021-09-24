
from pip._vendor import requests

#el ID del usuario se encuentra consultando a @userinfobot
id_User = "657651205"
Mensage_to_send = "Alarma activa"


requests.post('https://api.telegram.org/bot2001629979:AAEIlHZKdiTjSFdXXPvLy1uytUJsx5Nu_A8/sendMessage',
              data={'chat_id': id_User, 'text': Mensage_to_send})