class Bot:
    def __init__(self):
        self.__tagged = []
        self.__got = []
        self.__contained = []

    def input(self, data):
        self.process(data)

    def process(self, data):
        for got in self.__got:
            got(data)
        for tagged, _data in self.__tagged:
            if '@' + _data in data:
                tagged(data)
        for contained, _data in self.__contained:
            if _data in data:
                contained(data)

    def Got(self):
        def wrapper(method):
            self.__got.append(method)
        return wrapper

    def Tagged(self, data):
        def wrapper(method):
            self.__tagged.append((method, data))
        return wrapper

    def Contained(self, data):
        def wrapper(method):
            self.__contained.append((method, data))
        return wrapper
