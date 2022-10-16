class Errors:
    def importLibs(self):
        from src.actions import Actions
        from src.recognition import Recognition
        from src.images import Images
        from src.log import Log

        self.actions = Actions()
        self.recognition = Recognition()
        self.images = Images()
        self.log = Log()

    def verify(self):
        self.importLibs()
        errors = False

        error_01 = self.images.image('error_01')
        error_01_positions = self.recognition.positions(error_01, threshold=0.7)
        if error_01_positions is not False:
            errors = True

        try_again_later = self.images.image('try_again_later')
        try_again_later_positions = self.recognition.positions(try_again_later, threshold=0.7)
        if try_again_later_positions is not False:
            errors = True

        if errors is True:
            self.log.console('Error detected, trying to resolve', color='red')

            if error_01_positions is not False:
                self.actions.clickButton(error_01)
                self.actions.sleep(3, 3, forceTime=True)

            if try_again_later_positions is not False:
                close_shop = self.images.image('close_shop')
                self.actions.clickButton(close_shop)
                self.actions.sleep(3, 3, forceTime=True)
