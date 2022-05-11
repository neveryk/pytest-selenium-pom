from configparser import ConfigParser

class Readini():

    def __init__(self):
        pass

    def load_ini(self,file_path):
        config=ConfigParser()
        config.read(file_path,encoding = 'utf-8')
        return config

data_ini=Readini()