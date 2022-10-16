from cv2 import cv2

import pyautogui
import random
import time


class Actions:
    def importLibs(self):
        from src.actions import Actions
        from src.images import Images
        from src.log import Log
        from src.recognition import Recognition
        self.actions = Actions()
        self.images = Images()
        self.log = Log()
        self.recognition = Recognition()

    def click(self, x, y, movementInSeconds=0.5, forceTime=False):
        self.importLibs()
        if forceTime == False:
            movementInSeconds = 0.2
        pyautogui.click(x, y, duration=movementInSeconds)

    def doubleClick(self, x, y, movementInSeconds=0.5, interval=0.0, forceTime=False):
        self.importLibs()
        if forceTime == False:
            movementInSeconds = 0.2
        pyautogui.doubleClick(
            x, y, duration=movementInSeconds, interval=interval)

    def clickButton(self, image, name=None, timeout=3, threshold=None):
        self.importLibs()
        if(threshold == None):
            threshold = 0.8

        if not name is None:
            pass

        start = time.time()
        clicked = False
        while(not clicked):
            matches = self.recognition.positions(image, threshold=threshold)
            if(matches is False):
                hast_timed_out = time.time()-start > timeout
                if(hast_timed_out):
                    if not name is None:
                        pass
                    return False
                continue

            x, y, w, h = matches[0]
            self.click(int(x+(w/2)), int(y+(h/2)))
            return True

    def closeModal(self):
        self.importLibs()

        close_01 = self.images.image('close_01')
        close_01_positions = self.recognition.positions(close_01, threshold=0.88)
        print('close_01_positions', close_01_positions)
        if close_01_positions is not False:
            self.actions.clickButton(close_01, threshold=0.88)
            return True

        close_02 = self.images.image('close_02')
        close_02_positions = self.recognition.positions(close_02, threshold=0.88)
        print('close_02_positions', close_02_positions)
        if close_02_positions is not False:
            self.actions.clickButton(close_02, threshold=0.88)
            return True

        close_03 = self.images.image('close_03')
        close_03_positions = self.recognition.positions(close_03, threshold=0.6)
        print('close_03_positions', close_03_positions)
        if close_03_positions is not False:
            self.actions.clickButton(close_03, threshold=0.6)
            return True

        close_04 = self.images.image('close_04')
        close_04_positions = self.recognition.positions(close_04, threshold=0.9)
        print('close_04_positions', close_04_positions)
        if close_04_positions is not False:
            self.actions.clickButton(close_04, threshold=0.9)
            return True

        close_05 = self.images.image('close_05')
        close_05_positions = self.recognition.positions(close_05, threshold=0.92)
        print('close_05_positions', close_05_positions)
        if close_05_positions is not False:
            self.actions.clickButton(close_05, threshold=0.92)
            return True

        close_06 = self.images.image('close_06')
        close_06_positions = self.recognition.positions(close_06, threshold=0.88)
        print('close_06_positions', close_06_positions)
        if close_06_positions is not False:
            self.actions.clickButton(close_06, threshold=0.88)
            return True

        close_07 = self.images.image('close_07')
        close_07_positions = self.recognition.positions(close_07, threshold=0.8)
        print('close_07_positions', close_07_positions)
        if close_07_positions is not False:
            self.actions.clickButton(close_07, threshold=0.8)
            return True

        close_08 = self.images.image('close_08')
        close_08_positions = self.recognition.positions(close_08, threshold=0.7)
        print('close_08_positions', close_08_positions)
        if close_08_positions is not False:
            self.actions.clickButton(close_08, threshold=0.7)
            return True

        close_09 = self.images.image('close_09')
        close_09_positions = self.recognition.positions(close_09, threshold=0.88)
        print('close_09_positions', close_09_positions)
        if close_09_positions is not False:
            self.actions.clickButton(close_09, threshold=0.88)
            return True

        close_10 = self.images.image('close_10')
        close_10_positions = self.recognition.positions(close_10, threshold=0.78)
        print('close_10_positions', close_10_positions)
        if close_10_positions is not False:
            self.actions.clickButton(close_10, threshold=0.78)
            return True

        close_11 = self.images.image('close_11')
        close_11_positions = self.recognition.positions(close_11, threshold=0.88)
        print('close_11_positions', close_11_positions)
        if close_11_positions is not False:
            self.actions.clickButton(close_11, threshold=0.88)
            return True

        button_back_google = self.images.image('button_back_google')
        button_back_google_positions = self.recognition.positions(
            button_back_google)
        print('button_back_google_positions', button_back_google_positions)
        if button_back_google_positions is not False:
            self.actions.clickButton(button_back_google)
            return True

        google_play = self.images.image('google_play')
        google_play_positions = self.recognition.positions(google_play, threshold=0.7)
        print('google_play_positions', google_play_positions)
        if google_play_positions is not False:
            button_back_bluestack = self.images.image('button_back_bluestack')
            button_back_positions = self.recognition.positions(
                button_back_bluestack, threshold=0.75)
            print('button_back_positions', button_back_positions)
            if button_back_positions is not False:
                x, y, _, _ = button_back_positions[0]
                self.actions.click(int(x+10), int(y+10))
            return True


        button_ok = self.images.image('button_ok')
        button_ok_positions = self.recognition.positions(button_ok, threshold=0.78)
        print('button_ok_positions', button_ok_positions)
        if button_ok_positions is not False:
            self.actions.clickButton(button_ok, threshold=0.78)
            return True

        getting_video = self.images.image('getting_video')
        getting_video_positions = self.recognition.positions(getting_video)
        print('getting_video_positions', getting_video_positions)
        if getting_video_positions is not False:
            close_shop = self.images.image('close_shop')
            self.actions.clickButton(close_shop)
            return True

    def closeAlert(self):
        self.importLibs()
        close_button = self.images.image('close_button')
        self.actions.clickButton(close_button)
        self.sleep(0.5, 0.5, forceTime=True)

    def move(self, x, y, movementInSeconds=1, forceTime=False):
        self.importLibs()
        if forceTime == False:
            movementInSeconds = 0.2
        pyautogui.moveTo(x, y, movementInSeconds,
                         tween=pyautogui.easeInOutQuad)

    def sleep(self, min, max, forceTime=False):
        self.importLibs()
        sleep = random.uniform(min, max)
        if forceTime == False:
            sleep = 0
        return time.sleep(sleep)

    def refreshPage(self):
        self.importLibs()
        self.log.console('Refreshing page', color='green')
        pyautogui.hotkey('ctrl', 'shift', 'r')
        self.actions.sleep(1, 1, forceTime=True)
        reload = self.images.image(
            'reload', newPath='./images/themes/default/errors/')
        reload_positions = self.recognition.positions(reload)
        if reload_positions is not False:
            self.actions.clickButton(reload)

    def show(self, img):
        cv2.imshow('img', img)
        cv2.waitKey(0)
