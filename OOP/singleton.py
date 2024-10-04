class Singleton:
    _instance = None

    def __new__(cls, *arg, **kwagrs):
        if cls._instance == None:
            cls._instance = object.__new__(cls)
        return cls._instance
    
first = Singleton()
second = Singleton()
print(first is second)