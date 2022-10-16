from cv2 import cv2
from os import listdir


class Images:
    def __init__(self, theme='default'):
        self.theme = theme

    def image(self, image, theme=False, newPath=None):
        path = './images/themes/default/'
        if theme == True:
            path = './images/themes/' + self.theme + '/'

        if newPath != None:
            path = newPath

        return cv2.imread(path + image + '.png')

    def loadImages(self, folder):
        dir_name = folder
        file_names = listdir(dir_name)
        targets = {}
        for file in file_names:
            path = dir_name + file
            targets[self.remove_suffix(file, '.png')] = cv2.imread(path)

        return targets

    def remove_suffix(self, input_string, suffix):
        if suffix and input_string.endswith(suffix):
            return input_string[:-len(suffix)]
        return input_string
