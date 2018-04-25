import random
import string


class URLShortener():
    '''Implementation of a URL shortener.

    >>> shorty = URLShortener()
    >>> shortened = shorty.shorten("https://google.com")
    >>> shorty.recover(shortened)
    'https://google.com'
    '''
    def __init__(self):
        self.__store = {}

    @staticmethod
    def random_path(size=6):
        return ''.join(random.choices(string.ascii_letters + string.digits, k=size))

    def shorten(self, url):
        short = self.random_path()
        assert short not in self.__store, 'short already in store'
        self.__store[short] = url
        return short

    def recover(self, short):
        return self.__store.get(short)
