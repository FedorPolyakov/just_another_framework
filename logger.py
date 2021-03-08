from patterns.singletone import Singletone
from time import gmtime, time


class Logger(metaclass=Singletone):

    def __init__(self, name):
        self.name = name

    def log(self, text):
        print(f'{gmtime().tm_year}.{gmtime().tm_mon}'
              f'.{gmtime().tm_mday} - {gmtime().tm_hour}'
              f':{gmtime().tm_min}:{gmtime().tm_sec} -> {text}')

#
class Debug:
    def __call__(self, func):
        def decorated(*args, **kwargs):
            start = time()
            wrap = func(*args, **kwargs)
            end = time()
            print(f'DEBUG -> {func.__name__}, {end - start}')
            return wrap
        return decorated
