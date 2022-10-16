from colorama import init, Fore, Style

from src.application import Application
from src.log import Log
from src.multi_account import MultiAccount

init()

banner = """
********************************************************************
** EARN TO DIE 2 - ADS MONEY - BOT
**
** Please consider buying me a coffee :)
** PIX (Brazil Payment): 08912d17-47a6-411e-b7ec-ef793203f836
********************************************************************
** Press CTRL + C to kill the bot.
** Some configs can be found in the
********************************************************************
"""

print(Fore.GREEN + banner + Style.RESET_ALL)

application = Application()
log = Log()
multi_account = MultiAccount()


def main():
    application.start()
    multi_account.start()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        log.console('Shutting down the bot', color='red')
        exit()
