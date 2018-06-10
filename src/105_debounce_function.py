from datetime import datetime, timedelta


def debounce(f, N):
    '''Returns a debounced version of f.

    As long as f keeps getting called, the result stays the same for N milliseconds.

    >>> a = debounce(lambda x: x + 1, 1000)
    >>> a(1)
    2
    >>> a(2)
    2
    >>> a("cows")
    2

    When the time expires, a new result can be loaded.
    >>> from time import sleep
    >>> sleep(1)
    >>> a(7)
    8
    >>> a(1)
    8
    '''

    def inner(*args, **kwargs):
        if inner.last_call is None or inner.last_call + inner.delta < datetime.now():
            inner.last_call = datetime.now()
            inner.result = f(*args, **kwargs)
        return inner.result

    inner.last_call = None
    inner.delta = timedelta(milliseconds=N)
    inner.f = f
    return inner
