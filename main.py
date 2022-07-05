# -*- coding: utf-8 -*-
import vk_api
import os.path
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from vk_api.utils import get_random_id

token = "vk1.a.OCRDmSMcVhjHIJl22DeJyjDQpiYr0qdecEbOgoxaAF5WGCmu14JbNYKwVDYs2CVJ-f-XqsZjkNbe1yYNIY6w9Sg3NlSIodd3Uo26QYaNNspAkTNEVz9e9zwjGhgv7LNDwKqZIFmILz6busOAWZbQux4Dl4Xh-1Y5bj6045DR_sZUBYJd4ADXT_dPcAQfqopC"


class Main:
    def __init__(self):
        self.vk_session = vk_api.VkApi(token=token)
        self.longpoll = VkBotLongPoll(self.vk_session, '214336365')
        self.vk_api = self.vk_session.get_api()

    def send_msg(self, send_id, msg):
        self.vk_api.messages.send(peer_id=send_id, message=msg, random_id=get_random_id())

    def events(self):
        while True:
            for event in self.longpoll.listen():
                if event.type == VkBotEventType.MESSAGE_NEW and event.object['message']:
                    message = event.obj['message']

                    id = event.object.message['from_id']
                    text = message['text']

                    if text.lower() == 'help':
                        main.send_msg(id,
                                      "Чат-бот создан для автоматической обработки документов с расширением .docx и .doc."
                                      "\nБот упростит вам жизнь и сам подправит ваш файл в соответствии с ГОСТом или любыми шаблонами на ваш вкус."
                                      "\n\nНа данный момент чат-бот поддерживает следующий список команд:"
                                      "\nprocess — начать процесс обработки документов;"
                                      "\npatterns — посмотреть список сохраненных шаблонов и шаблонов по умолчанию;"
                                      "\ncreate — создать и сохранить новый шаблон;"
                                      "\nsupport — вызов поддержки для решения проблем с работой чат-бота."
                                      "\n\nНам важна ваша конфиденциальность и эффективность работы бота. "
                                      "Бот не перенаправляет ваши файлы и данные другим пользователям и группам,"
                                      "а сообщения с готовыми файлами автоматически удаляются спустя сутки после оформления работы, при этом все шаблоны сохраняются.")
                    elif text.lower() == 'patterns':
                        fpath = "/home/Klopolupka/patterns/" + str(id)
                        if os.path.exists(fpath):
                            pattern = open(fpath, "r+")
                            main.send_msg(id, pattern.readline())
                            pattern.close()
                        else:
                            main.send_msg(id, "У Вас 0 сохраненных шаблонов. Введите 'add pattern', чтобы добавить новый шаблон.")
                    elif text.lower() == 'add pattern':
                            pattern = open(fpath, "w+")
                            pattern.close()
                    elif text.lower() == 'support':
                        main.send_msg(id, "Ваш запрос на техническую поддержку обрабатывается. В ближайшее время с вами свяжется технический специалист. Ожидайте...")
                        main.send_msg(208567150, "Поступил запрос на техническую поддержку от пользователя под id – " + str(id))
                    elif text.lower() == 'commands':
                        main.send_msg(id,
                        "\n\nНа данный момент чат-бот поддерживает следующий список команд:"
                        "\nprocess — начать процесс обработки документов;"
                        "\npatterns — посмотреть список сохраненных шаблонов и шаблонов по умолчанию;"
                        "\ncreate — создать и сохранить новый шаблон;"
                        "\nsupport — вызов поддержки для решения проблем с работой чат-бота.")
                    else:
                        main.send_msg(id, "Данная команда не найдена. Посмотреть список команд можно введя 'help' или 'commands'."
                        "\nЕсли Вы уверены, что ввели команду верно, вызовите техническую поддержку – 'support'.")


if __name__ == "__main__":
    main = Main()
    main.events()