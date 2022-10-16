import pyautogui


class Application:
    def __init__(self):
        from src.images import Images
        self.images = Images()

    def importLibs(self):
        from src.log import Log
        self.log = Log()

    def start(self):
        self.importLibs()
        pyautogui.FAILSAFE = False

        input('Press Enter to start the bot...\n')
        self.log.console('Starting bot...', color='green')

    def stop(self):
        exit()
