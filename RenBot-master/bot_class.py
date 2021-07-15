import requests
from time import strftime
import bs4
import random
from pyowm import OWM
from pyowm.utils import config as cfg
from vk_api.audio import VkAudio
import vk_api
from config import token
from itertools import islice

class VkBot():

    def __init__(self, user_id):
    
        print("Создан объект бота!")

        self._token = token

        self._vk_session = vk_api.VkApi(token=self._token)

        self._USER_ID = user_id

        self._USERNAME = self._get_user_name_from_vk_id(user_id)

        self._USERSUBNAME = self._get_user_subname_from_vk_id(user_id)

        self._shot_or_not = ['Попадание!','Промах!']

        self._COMMANDS = ["/HELP","!ПРИВЕТ", "!ПОГОДА", "!ВРЕМЯ", "!ПОКА", "!ОГОНЬ", "!ДУЭЛЬ", "!РУЛЕТКА"]

        self._OWM_CFG = cfg.get_default_config()

        self._OWM_CFG['language'] = 'ru'

        #self._Audio = VkAudio(self._vk_session)

        self._OWM = OWM('3ca6b38cb2e2ccdedfe19cee422ef28c', self._OWM_CFG) 


    @staticmethod
    def _clean_all_tag_from_str(string_line):
        """
        Очистка строки stringLine от тэгов и их содержимых
        :param string_line: Очищаемая строка
        :return: очищенная строка
        """
        result = ""
        not_skip = True
        for i in list(string_line):
            if not_skip:
                if i == "<":
                    not_skip = False
                else:
                    result += i
            else:
                if i == ">":
                    not_skip = True
        
        return result

    # Достать имя страницы
    def _get_user_name_from_vk_id(self, user_id):
        request = requests.get("https://vk.com/id"+str(user_id))
        bs = bs4.BeautifulSoup(request.text, "html.parser")
        user_name = self._clean_all_tag_from_str(bs.findAll("title")[0])
        return user_name.split()[0]
    
    # Достать фамилию страницы
    def _get_user_subname_from_vk_id(self, user_id):
        request = requests.get("https://vk.com/id"+str(user_id))
        bs = bs4.BeautifulSoup(request.text, "html.parser")
        user_subname = self._clean_all_tag_from_str(bs.findAll("title")[0])
        return user_subname.split()[1]


# Получение времени:
    def _get_time(self):
        t = strftime('%H:%M:%S')
        return t

    # Получение погоды
    def _get_weather(self, message):
        mgr = self._OWM.weather_manager()
        observation = mgr.weather_at_place(message[8:])
        w = observation.weather
        temp = str(w.temperature('celsius')["temp"])
        result = 'Сейчас в городе ' + str(message[8:]) + ' ' + str(temp[:-3]) + ' градусов.'
        return result


    #Получение музыки
    def _get_music(self, message):
        audio = self._Audio.search(q=message[8:], count=20)
        print(audio)
        for i in islice(audio):
            print(i)
        return 'Посмотри в консоль!'
    
    def _sex(self, from_id, to_id):
        from_user = self._get_user_name_from_vk_id(from_id)
        to_user = self._get_user_name_from_vk_id(to_id) 
        result = f'@id{from_id}({from_user}) выебал @id{to_id}({to_user})'
        return result 

    #определение отсылаемого сообщения
    def new_message(self, message):
        # Меню команд
        if message.upper() == self._COMMANDS[0]:
            return f"Привет, @id{self._USER_ID} ({self._USERNAME+' '+self._USERSUBNAME})!\nСпасибо что начал использовать данного бота.\n\nКОМАНДЫ:\n\n1) !Погода %город_нейм% - Показывает погоду в нужном городе.\n2) !Время - Показывает точное время отправителя.\n3) !Дуэль - Постреляшки!!1!(WIP)\n4) !Рулетка - Попробуйте русскую рулетку!(WIP)"
        # Привет
        elif message.upper() == self._COMMANDS[1]:
            return f"Привет-привет, @id{self._USER_ID} ({self._USERNAME})!"
            
        # Погода
        elif "!ПОГОДА" in message.upper():
            return self._get_weather(message=message)

        # Музыка 
        elif '!МУЗЫКА' in message.upper():
            return self._get_music(message=message)
            
        # Время
        elif message.upper() == self._COMMANDS[3]:
            return self._get_time()
            
        # Пока
        elif message.upper() == self._COMMANDS[4]:
            return f"Пока-пока, @id{self._USER_ID} ({self._USERNAME})!"
        
        # Огонь
        elif message.upper() == self._COMMANDS[5]:
            return f"@id{self._USER_ID} ({self._USERNAME}) делает выстрел..\n\nИтог - {random.choice(self._shot_or_not)}\nШанс попадания - {random.randint(0,100)}%"
        
        # Дуэль
        elif message.upper() == self._COMMANDS[6]:
            return f"@id{self._USER_ID} ({self._USERNAME+' '+self._USERSUBNAME}) хочет организовать дуэль.\n\nПротивник - .\n\nОСНОВНЫЕ КОМАНДЫ:\n!Огонь - для выстрела.\n"
        
        # Рулетка
        elif message.upper() == self._COMMANDS[7]:
            return f"@id{self._USER_ID} ({self._USERNAME+' '+self._USERSUBNAME}) приглашает на русскую рулетку.\n\nПРАВИЛА:\nВ барабане всегда 1/6 патронов.\n!Выстрел - для выстрела."
        

        
        else:
            return 'False'
