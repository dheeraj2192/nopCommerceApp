import configparser

config=configparser.RawConfigParser()
config.read(".\\Configurations\\config.ini")


class ReadConfig:
    @staticmethod
    def getApplicationURL():
        applicationURL=config.get("common setup","baseURL")
        return applicationURL

    @staticmethod
    def getUserName():
        useremail=config.get("common setup","username")
        return useremail

    @staticmethod
    def getPassword():
        pwd = config.get("common setup", "password")
        return pwd