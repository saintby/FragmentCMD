import requests, configparser
from colorama import Style, Fore
from datetime import datetime

time_format = '%d-%m-%Y %H:%M:%S'

class CustomConfigParser(configparser.ConfigParser):
    def optionxform(self, optionstr):
        return optionstr  # Оставляем регистр без изменений

config = CustomConfigParser()
config.read("config.ini")

def save_config():
    with open('config.ini', 'w') as config_file:
        config.write(config_file)

def buyStars(SEED):
    print(f"[{datetime.now().strftime(time_format)}] Впишите юзернейм, кому вы хотите купить звёзды.")
    print(f"[{datetime.now().strftime(time_format)}] Можно как t.me/..., так и @username или username.")
    username: str = input(f"[{datetime.now().strftime(time_format)}] >>> ")
    print(f"[{datetime.now().strftime(time_format)}] Замечательно! Теперь впиши количество звёзд для покупки.")
    print(f"[{datetime.now().strftime(time_format)}] Пиши целое число без каких-либо символов от 50 до 1,000,000")
    amount: int = int(input(f"[{datetime.now().strftime(time_format)}] >>> "))
    print(f"[{datetime.now().strftime(time_format)}] Теперь внимательно перепроверь данные ниже:")
    print(f"[{datetime.now().strftime(time_format)}] 👤 Юзернейм: {username}")
    print(f"[{datetime.now().strftime(time_format)}] ✨ Звёзды: {amount} шт.")
    print(f"[{datetime.now().strftime(time_format)}] Всё верно?")
    print(f"[{datetime.now().strftime(time_format)}] [1] Да")
    print(f"[{datetime.now().strftime(time_format)}] [2] Нет, исправить.")
    f: int = int(input(f"[{datetime.now().strftime(time_format)}] >>> "))
    if f == 1:
        url = "https://fragmentapi.nightstranger.space/buyStarsWithoutKYC"
        headers = {
            "Content-Type": "application/json"
        }

        data = {
            "username": username,
            "amount": amount,
            "seed": SEED
        }

        try:
            response = requests.post(url, headers=headers, json=data)

            if response.status_code == 200:
                result = response.json()
                if result.get("success"):
                    print(f"[{datetime.now().strftime(time_format)}] Покупка успешно завершена!")
                    print(f"[{datetime.now().strftime(time_format)}] 👤 Юзернейм: {username}")
                    print(f"[{datetime.now().strftime(time_format)}] ✨ Звёзды: {amount} шт.")
                else:
                    print(f"[{datetime.now().strftime(time_format)}] ⚠️ Покупка не удалась!")
                    print(
                        f"[{datetime.now().strftime(time_format)}] ❌ Причина: {result.get('message', 'Unknown error')}")

            elif response.status_code == 400:
                print("\n⚠️ Плохой запрос.")
                print(f"Message: {response.json().get('message', 'Invalid request data')}")
            elif response.status_code == 422:
                print("\n⚠️ Ошибка валидации.")
                print(f"Message: {response.json().get('message', 'Validation failed')}")
            elif response.status_code == 500:
                print("\n💥 Ошибка сервера.")
                print(f"Message: {response.json().get('message', 'Internal server error')}")
            else:
                print("\n❓ Неожиданный код ошибки:", response.status_code)
                print("Response:", response.json())

        except requests.RequestException as e:
            print("\n🚨 Запрос не удался:", str(e))

    if f == 2:
        buyStars(SEED)


def buyPremium(SEED):
    print(f"[{datetime.now().strftime(time_format)}] Впишите юзернейм, кому вы хотите подарить Premium.")
    print(f"[{datetime.now().strftime(time_format)}] Можно как t.me/..., так и @username или username.")
    username: str = input(f"[{datetime.now().strftime(time_format)}] >>> ")
    print(f"[{datetime.now().strftime(time_format)}] Замечательно! Теперь впиши длительность подписки.")
    print(f"[{datetime.now().strftime(time_format)}] Пиши целое число без каких-либо символов: 3, 6, 12.")
    duration: int = int(input(f"[{datetime.now().strftime(time_format)}] >>> "))
    print(f"[{datetime.now().strftime(time_format)}] Теперь внимательно перепроверь данные ниже:")
    print(f"[{datetime.now().strftime(time_format)}] 👤 Юзернейм: {username}")
    print(f"[{datetime.now().strftime(time_format)}] 🕙 Длительность: {duration} мес.")
    print(f"[{datetime.now().strftime(time_format)}] Всё верно?")
    print(f"[{datetime.now().strftime(time_format)}] [1] Да")
    print(f"[{datetime.now().strftime(time_format)}] [2] Нет, исправить.")
    f: int = int(input(f"[{datetime.now().strftime(time_format)}] >>> "))
    if f == 1:
        url = "https://fragmentapi.nightstranger.space/buyPremiumWithoutKYC"
        headers = {
            "Content-Type": "application/json"
        }

        data = {
            "username": username,
            "duration": duration,
            "seed": SEED
        }

        try:
            response = requests.post(url, headers=headers, json=data)

            if response.status_code == 200:
                result = response.json()
                if result.get("success"):
                    print(f"[{datetime.now().strftime(time_format)}] Покупка успешно завершена!")
                    print(f"[{datetime.now().strftime(time_format)}] 👤 Юзернейм: {username}")
                    print(f"[{datetime.now().strftime(time_format)}] 🕙 Длительность: {duration} мес.")
                else:
                    print(f"[{datetime.now().strftime(time_format)}] ⚠️ Покупка не удалась!")
                    print(
                        f"[{datetime.now().strftime(time_format)}] ❌ Причина: {result.get('message', 'Unknown error')}")

            elif response.status_code == 400:
                print("\n⚠️ Плохой запрос.")
                print(f"Message: {response.json().get('message', 'Invalid request data')}")
            elif response.status_code == 422:
                print("\n⚠️ Ошибка валидации.")
                print(f"Message: {response.json().get('message', 'Validation failed')}")
            elif response.status_code == 500:
                print("\n💥 Ошибка сервера.")
                print(f"Message: {response.json().get('message', 'Internal server error')}")
            else:
                print("\n❓ Неожиданный код ошибки:", response.status_code)
                print("Response:", response.json())

        except requests.RequestException as e:
            print("\n🚨 Запрос не удался:", str(e))

    elif f == 2:
        buyPremium(SEED)


def getBalance(SEED):
    url = "https://fragmentapi.nightstranger.space/getBalance"
    headers = {
        "Content-Type": "application/json"
    }
    data = {
        "seed": SEED
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        if response.status_code == 200:
            result = response.json()
            if result.get("success"):
                print(f"[{datetime.now().strftime(time_format)}] Запрос успешно отправлен!")
                print(f"[{datetime.now().strftime(time_format)}] 💸 Баланс кошелька: {result.get('balance')} TON")
            else:
                print(f"[{datetime.now().strftime(time_format)}] ⚠️ Покупка не удалась!")
                print(f"[{datetime.now().strftime(time_format)}] ❌ Причина: {result.get('message', 'Unknown error')}")

        elif response.status_code == 400:
            print("\n⚠️ Плохой запрос.")
            print(f"Message: {response.json().get('message', 'Invalid request data')}")
        elif response.status_code == 422:
            print("\n⚠️ Ошибка валидации.")
            print(f"Message: {response.json().get('message', 'Validation failed')}")
        elif response.status_code == 500:
            print("\n💥 Ошибка сервера.")
            print(f"Message: {response.json().get('message', 'Internal server error')}")
        else:
            print("\n❓ Неожиданный код ошибки:", response.status_code)
            print("Response:", response.json())

    except requests.RequestException as e:
        print("\n🚨 Запрос не удался:", str(e))

def getSeed():
    try:
        config.get('Main', 'SEED')
    except configparser.NoOptionError:
        print(
            f"[{datetime.now().strftime(time_format)}] Чтобы продолжить работу, введи Seed / Memo твоего TON-кошелька.")
        print(f"[{datetime.now().strftime(time_format)}] Инструкция, как его получить, есть в теме на Lolz.")
        s = input(f"[{datetime.now().strftime(time_format)}] >>> ")
        config["Main"]["SEED"] = s
        with open('config.ini', 'w') as config_file:
            config.write(config_file)
        print(f"[{datetime.now().strftime(time_format)}] Сохранено!")
        print(f"[{datetime.now().strftime(time_format)}] Настройка завершена!")
    return config["Main"]["SEED"]

def updateSeed():
    print(f"[{datetime.now().strftime(time_format)}] Чтобы продолжить работу, введи Seed / Memo твоего TON-кошелька.")
    print(f"[{datetime.now().strftime(time_format)}] Инструкция, как его получить, есть в теме на Lolz.")
    s = input(f"[{datetime.now().strftime(time_format)}] >>> ")
    config["Main"]["SEED"] = s
    with open('config.ini', 'w') as config_file:
        config.write(config_file)
    print(f"[{datetime.now().strftime(time_format)}] Сохранено!")
    print(f"[{datetime.now().strftime(time_format)}] Настройка завершена!")
    return config["Main"]["SEED"]


def main():
    logo = """)

▄████████    ▄████████     ███     
███    ███   ███    ███ ▀█████████▄ 
███    █▀    ███    █▀     ▀███▀▀██ 
▄███▄▄▄      ▄███▄▄▄         ███   ▀ 
▀▀███▀▀▀     ▀▀███▀▀▀         ███     
███          ███            ███     
███          ███            ███     
███          ███           ▄████▀   

"""
    VERSION = "\nv1.0"
    msg = f"""

{Fore.LIGHTWHITE_EX}{Style.BRIGHT} * Telegram: {Fore.LIGHTRED_EX} t.me/maybewearedxxd
{Fore.LIGHTWHITE_EX}{Style.BRIGHT} * VK: {Fore.LIGHTRED_EX} vk.com/christyoursaver
{Fore.LIGHTWHITE_EX}{Style.BRIGHT} * GitHub: {Fore.LIGHTRED_EX} github.com/saintby
{Fore.LIGHTWHITE_EX}{Style.BRIGHT} * Lolz: {Fore.LIGHTRED_EX} lolz.live/members/6469293/
{Fore.LIGHTWHITE_EX}{Style.BRIGHT} * FunPay: {Fore.LIGHTRED_EX} funpay.com/users/2763155/
"""
    print(logo + VERSION + msg)
    print(f"[{datetime.now().strftime(time_format)}] Привет!")
    SEED = getSeed()
    while True:
        print(f"[{datetime.now().strftime(time_format)}] Выбери следующее действие:")
        print(f"[{datetime.now().strftime(time_format)}] [1] Купить звёзды")
        print(f"[{datetime.now().strftime(time_format)}] [2] Купить Premium")
        print(f"[{datetime.now().strftime(time_format)}] [3] Узнать баланс кошелька")
        print(f"[{datetime.now().strftime(time_format)}] [4] Обновить данные")
        print(f"[{datetime.now().strftime(time_format)}] P.S. Данные необходимо обновлять каждые 24 часа!")
        print(f"[{datetime.now().strftime(time_format)}] [5] Выйти из программы")
        c: int = int(input(f"[{datetime.now().strftime(time_format)}] >>> "))

        if c == 1:
            buyStars(SEED)

        elif c == 2:
            buyPremium(SEED)

        elif c == 3:
            getBalance(SEED)

        elif c == 4:
            SEED = updateSeed()

        elif c == 5:
            print(f"[{datetime.now().strftime(time_format)}] Спасибо за использование!")
            print(f"[{datetime.now().strftime(time_format)}] Завершаю процесс")
            exit()

if __name__ == "__main__":
    main()
