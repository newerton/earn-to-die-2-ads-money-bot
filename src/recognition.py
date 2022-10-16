from cv2 import cv2

import numpy as np
import time


class Recognition:
    def importLibs(self):
        from src.actions import Actions
        from src.desktop import Desktop
        from src.images import Images
        from src.recognition import Recognition
        self.actions = Actions()
        self.desktop = Desktop()
        self.images = Images()
        self.recognition = Recognition()

    def positions(self, target, threshold=None, baseImage=None, returnArray=False, debug=False):
        self.importLibs()
        if threshold == None:
            threshold = 0.8

        if baseImage is None:
            img = self.desktop.printScreen()
        else:
            img = baseImage

        w = target.shape[1]
        h = target.shape[0]

        result = cv2.matchTemplate(img, target, cv2.TM_CCOEFF_NORMED)

        yloc, xloc = np.where(result >= threshold)

        rectangles = []
        for (x, y) in zip(xloc, yloc):
            rectangles.append([int(x), int(y), int(w), int(h)])
            rectangles.append([int(x), int(y), int(w), int(h)])

        rectangles, _ = cv2.groupRectangles(rectangles, 1, 0.2)

        if debug is True:
            img2 = img.copy()
            for r in rectangles:
                cv2.rectangle(img2, (r[0], r[1]),
                              (r[0]+w, r[1]+h), (0, 0, 255), 2)
            cv2.imshow("detected", img2)
            cv2.waitKey(0)
            self.actions.sleep(2, 2, forceTime=True)

        if returnArray is False:
            if len(rectangles) > 0:
                return rectangles
            else:
                return False
        else:
            return rectangles

    def waitForImage(self, images, timeout=30, threshold=0.85, multiple=False):
        self.importLibs()
        start = time.time()
        while True:
            if multiple is not False:
                for img in images:
                    matches = self.recognition.positions(
                        img, threshold=threshold)
                    if matches is False:
                        hast_timed_out = time.time()-start > timeout
                        if hast_timed_out is not False:
                            return False
                        continue
                    return True
            else:
                matches = self.recognition.positions(
                    images, threshold=threshold)
                if matches is False:
                    hast_timed_out = time.time()-start > timeout
                    if hast_timed_out is not False:
                        return False
                    continue
                elif matches is not False:
                    return True
                else:
                    return False

    def currentScreen(self):
        self.importLibs()

        garage_go = self.images.image('garage_go')
        shop_title = self.images.image('shop_title')

        if self.recognition.positions(garage_go, threshold=0.70) is not False:
            return "garage"
        elif self.recognition.positions(shop_title, threshold=0.70) is not False:
            return "shop"
        else:
            return "unknown"
