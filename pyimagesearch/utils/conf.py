import json
class Conf:
    def __init__(self, loc):
       f=open(loc)
       self.data=json.load(f)
    def output(self):
        print(type(self.data))
        return self.data


       
