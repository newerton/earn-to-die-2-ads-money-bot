import sys


class MultiAccount:
    def __init__(self):
        from src.log import Log
        self.log = Log()

    def importLibs(self):
        from src.actions import Actions
        from src.application import Application
        from src.errors import Errors
        from src.images import Images
        from src.recognition import Recognition

        self.actions = Actions()
        self.application = Application()
        self.errors = Errors()
        self.images = Images()
        self.recognition = Recognition()

    def start(self):
        self.importLibs()
        self.botSingle()

    def botSingle(self):
        while True:
            self.steps()

    def steps(self):
        currentScreen = self.recognition.currentScreen()
        print('currentScreen', currentScreen)

        self.errors.verify()
        self.actions.closeModal()

        if currentScreen == "garage":
            self.clickAds()

        if currentScreen == "shop":
            self.clickAds()

        sys.stdout.flush()
        self.actions.sleep(1, 1, forceTime=True)

    def clickAds(self):
        button_open_ads = self.images.image('button_open_ads')
        if self.actions.clickButton(button_open_ads, threshold=0.8) is True:
            self.log.console("Opening ads", color="green")

        button_open_ads_double = self.images.image('button_open_ads_double')
        if self.actions.clickButton(button_open_ads_double, threshold=0.8) is True:
            self.log.console("Opening ads - double reward", color="green")
