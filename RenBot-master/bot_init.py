#first commit
import vk_api, vk
#import requests
from vk_api.longpoll import VkLongPoll, VkEventType
import vk_api.bot_longpoll
from vk_api.utils import get_random_id
from bot_class import VkBot
from config import token # из файла config.py импортирует переменную token - строка п.с: токен можно получить либо от сообщеста либо токен vkme страницы
import random
def write_msg(chat, message, chat_id):
    if message != 'False':
        if chat == 'local':
            vk.messages.send(user_id=chat_id,message=message, random_id=random.randint(10000, 99999))
        elif chat == 'global':
            vk.messages.send(chat_id=chat_id,message=message, random_id=random.randint(10000, 99999))


#session = requests.Session()
vk_session = vk_api.VkApi(token=token)
# #try:
#     vk_session.auth()
# except vk_api.AuthError as error_msg:
#     print(error_msg)
#longpoll = vk_api.bot_longpoll.VkBotLongPoll(vk_session, group_id=205405839)

longpoll = vk_api.bot_longpoll.VkBotLongPoll(vk_session, group_id=205405839)

vk = vk_session.get_api()
write_msg(chat='global', message='Бот успешно включён.\nНапишите слово /help - для доступа к командам.',chat_id=3) #.test
#write_msg(chat='local', message='Бот успешно включён.',chat_id=252939037) #Степан
print("Server started")

for event in longpoll.listen():
    if event.type == vk_api.bot_longpoll.VkBotEventType.MESSAGE_NEW:
        print(event)
        if event.from_chat:
            chat_id = event.chat_id
            bot = VkBot(event.object.from_id)
            # message = bot.new_message(event.object.text)
            message = event.object.text
            if message in '!Выебать' and  event.object.reply_message != None:
                print(event.object.reply_message)
                print(event.object['from_id'])
                from_id = event.object['from_id']
                to_id = event.object.reply_message['from_id']
                write_msg(chat='global', message=bot._sex(from_id=from_id, to_id=to_id), chat_id=chat_id)
            message = bot.new_message(event.object.text)
            write_msg(chat='global', message=message, chat_id=chat_id)
        #print(event.from_chat)
        #print(event.from_user)
    
    
    
    
    



    #то что ниже делалось для другого бота пока не трогаем 
    
    # if event.type == VkEventType.MESSAGE_NEW:
    #     print('Text: ', event.text)
    #     print('Text: ', event.message)
    #     if event.from_chat:
    #         print(event.text, event.chat_id)
    #         chat_id = int(event.chat_id)
    #         bot = VkBot(event.user_id)
    #         message = bot.new_message(event.text)
    #         vk.messages.send(random_id=get_random_id(), chat_id=chat_id, message=message)




        # if event.to_me:
        
        #     print('New message:')
        #     print(f'For me by: {event.user_id}', end='')
            
        #     bot = VkBot(event.user_id)
        #     try:
        #         if event.from_user:
        #             chat='local'
        #         elif event.from_chat:
        #             chat='global'
        #             print(event.text, event.chat_id)
        #         if chat == 'local':
        #             chat_id = event.user_id
        #         elif chat == 'global':
        #             chat_id = event.chat_id
        #         if "!ПОГОДА" in event.text.upper():
        #             write_msg(chat, 'Узнаю погоду в городе ' + str(event.text[8:]), chat_id=chat_id)
        #         message = bot.new_message(event.text)
        #         write_msg(chat, message, chat_id=chat_id)
        #     except:
        #         write_msg(chat, 'error', chat_id=chat_id)
        #         print('error')