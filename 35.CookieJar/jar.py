class Jar:
    def __init__(self, capacity = 12):
        if isinstance(capacity, int) and capacity > 0:
            self._capacity = capacity
        else:
            raise ValueError("Capacity can't be non-negative")
        self._size = 0

    def __str__(self):
        return self.size * '🍪'


    def deposit(self, n):
        if n + self.size <= self.capacity:
            self._size += n
        else:
            raise ValueError('Exceed capacity')


    def withdraw(self, n):
        if n <= self.size:
            self._size -= n
        else:
            raise ValueError('Not enought cookies')


    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size


jar = Jar()
jar.deposit(5)
print(jar)
