from colorama import Fore

COLOR = {
    'blue': Fore.BLUE,
    'default': Fore.WHITE,
    'grey': Fore.LIGHTBLACK_EX,
    'yellow': Fore.YELLOW,
    'black': Fore.BLACK,
    'cyan': Fore.CYAN,
    'green': Fore.GREEN,
    'magenta': Fore.MAGENTA,
    'white': Fore.WHITE,
    'red': Fore.RED
}


class Log:
    def importLibs(self):
        from src.actions import Actions
        from src.date import Date
        self.actions = Actions()
        self.date = Date()
        self.log = Log()

    def console(self, message, color='default', end=False):
        self.importLibs()

        formatted_datetime = self.date.dateFormatted()
        console_message = "{} - {}".format(formatted_datetime, message)

        if end is False:
            print(console_message)
        else:
            print(console_message, end=end)

        return True
