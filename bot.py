import vk_api
from course import getCourse
from starwars import get_max_diametr, get_max_speed
from vk_api.longpoll import VkEventType,VkLongPoll
import random
token = "123"

vk_session = vk_api.VkApi(token=token)
vk = vk_session.get_api()
longpoll= VkLongPoll(vk_session)

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        message=event.text.lower()
        user_id = event.user_id
        random_id = random.randint(1, 10000000)
        if message == "курс":
            response = f"{getCourse('R01235')}"
            vk.messages.send(user_id=user_id, random=random_id, message=response)
        if message == "Корабль":
            response = f"{get_max_speed()}"
            vk.messages.send(user_id=user_id, random=random_id, message=response)
        if message == "Планета":
            response = f"{get_max_diametr()}"
            vk.messages.send(user_id=user_id, random=random_id, message=response)
