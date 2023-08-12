import configparser

config = configparser.RawConfigParser()
filepath = "D:\sudhir\software testing\Automation Pytest Selenium Practice\pythonProject\Configuration\config.ini"
config.read(filepath)

class Readconfig:
    @staticmethod
    def GetClinic():
        clinic = config.get('common data', 'Clinic')
        return clinic


    @staticmethod
    def GetUserName():
        username = config.get('common data', 'Username')
        return username

    @staticmethod
    def GetPassword():
        password = config.get('common data', 'Password')
        return password