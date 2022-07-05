# -*- coding: utf-8 -*-
import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.utils import get_random_id

token = "vk1.a.OCRDmSMcVhjHIJl22DeJyjDQpiYr0qdecEbOgoxaAF5WGCmu14JbNYKwVDYs2CVJ-f-XqsZjkNbe1yYNIY6w9Sg3NlSIodd3Uo26QYaNNspAkTNEVz9e9zwjGhgv7LNDwKqZIFmILz6busOAWZbQux4Dl4Xh-1Y5bj6045DR_sZUBYJd4ADXT_dPcAQfqopC"


class Main:
    def __init__(self):
        self.vk_session = vk_api.VkApi(token=token)
        self.longpoll = VkBotLongPoll(self.vk_session, '214336365')
        self.vk_api = self.vk_session.get_api()

    def send_msg(self, send_id, msg, rand):
        if rand == 1:
            self.vk_api.messages.send(peer_id=send_id, message=msg, random_id=rand)
        else:
            self.vk_api.messages.send(peer_id=send_id, message=msg, random_id=get_random_id())

    def events(self):
        while True:
            for event in self.longpoll.listen():
                if event.type == VkBotEventType.MESSAGE_NEW and event.object['message'] and event.from_chat or event.type == VkBotEventType.MESSAGE_NEW and event.object['message']:
                    message = event.obj['message']

                    peer = event.object.message['peer_id']
                    id = event.object.message['from_id']
                    text = message['text']

                    main.send_msg(peer,
                    "Приветствую&#128400;, я чат-бот, который поможет тебе оформить документ в соответствии с ГОСТом."
                    "\nОтправь сообщение \"help\", чтобы я смог рассказать правила пользования чат-ботом.", 1)

                    if text.lower() == 'help':
                        main.send_msg(id,
                                      "Чат-бот создан для автоматической обработки документов с расширением .docx и .doc."
                                      "\nБот упростит вам жизнь и сам подправит ваш файл в соответствии с ГОСТом или любыми шаблонами на ваш вкус."
                                      "\n\nНа данный момент чат-бот поддерживает следующий список команд:"
                                      "\nprocess — начать процесс обработки документов;"
                                      "\npatterns — посмотреть список сохраненных шаблонов и шаблонов по умолчанию;"
                                      "\ncreate — создать и сохранить новый шаблон;"
                                      "\nsupport — вызов поддержки для решения проблем с работой чат-бота."
                                      "\n\nНам важна ваша конфиденциальность и эффективность работы бота. Бот не перенаправляет ваши файлы и данные другим пользователям и группам, а сообщения с готовыми файлами автоматически удаляются спустя сутки после оформления работы.", 0)
                    elif text.lower() == 'settings':
                        main.send_msg(id, "Чат-бот предоставляет возможность настроить свою работу для вашего удобства."
                                          "\n\nНастройки:"
                                          "\nbuttons — включить/отключить систему кнопок;"
                                          "\nadvise — включить/отключить подсказки.", 0)
                    elif text.lower() == 'support':
                        vk = self.vk_session.get_api()
                        main.send_msg(id, "Ваш запрос на техническую поддержку обрабатывается. В ближайшее время с вами свяжется технический специалист. Ожидайте...", 0)
                        main.send_msg(208567150, "Поступил запрос на техническую поддержку от пользователя под id – " + str(id), 0)


if __name__ == "__main__":
    main = Main()
    main.events()
