import os 

def get_config(instance=""):
    return Config()

class Config(object):
    def __init__(self):
        self.redishost = "localhost"
        self.redisdb = 2
        self.redisport = 6379
        

        self.credentials = {}
        self.credentials['host'] = '127.0.0.1'
        self.credentials['user'] = 'root'
        self.credentials['passwd'] = 'root'
        self.credentials['db'] = 'my_db'

        self.read_credentials = {}
        self.read_credentials['host'] = '127.0.0.1'
        self.read_credentials['user'] = 'root'
        self.read_credentials['passwd'] = 'root'
        self.read_credentials['db'] = 'my_db'