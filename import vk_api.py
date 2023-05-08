import vk_api
from config import token
from vk_api.longpoll import VkLongPoll, VkEventType
from parse import getCource
import random

def main():
    vk_session = vk_api.VkApi(token = token)
    vk = vk_session.get_api() #Получение api for session
    longpoll = VkLongPoll(vk_session)

    for event in longpoll.listen():

        if event.type == VkEventType.MESSAGE_NEW and event.to_me:

            msg = event.text.lower()

    user_id = event.user_id

    randim_id = random.randint(1,10**10)

    print(f'Юзер {user_id} написал {msg}')

    if msg == '-к':
        responce = f'{getCource("R01235")} рублей за 1 доллар\n{getCource("R01239")} за 1 евро'

        vk.messages.send(user_id = user_id, random_id = randim_id,message = responce)

main()
 