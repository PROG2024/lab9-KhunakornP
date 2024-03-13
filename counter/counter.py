"""A singleton counter.

   counter = Counter()  get a reference to the counter. Initial count is 0.
   counter.count        property returns the current count
   counter.increment()  add 1 to current count and also return the new value

   Requirements:
   1. in Counter, do not use any static methods except __new__.
      You may not have a __new__ depending on how you implement the singleton.
"""


class Counter:
    __counter_instance = None

    def __init__(self):
        if not self.__started:
            self.__count = 0
            self.__started = True

    def __new__(cls, *args, **kwargs):
        if not cls.__counter_instance:
            cls.__counter_instance = super().__new__(cls, *args, *kwargs)
            cls.__counter_instance.__started = False
        return cls.__counter_instance

    def increment(self):
        self.__count += 1
        return self.count

    @property
    def count(self):
        return self.__count

    def __str__(self):
        return f"{self.__count}"
