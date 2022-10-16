import numpy as np
import mss

class Desktop:
    def printScreen(self):
        with mss.mss() as sct:
            monitorToUse = 1
            monitor = sct.monitors[monitorToUse]
            sct_img = np.array(sct.grab(monitor))
            return sct_img[:, :, :3]
