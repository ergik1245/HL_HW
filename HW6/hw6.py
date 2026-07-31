class CandyStash:

    MAX_CAPACITY = 50

    @staticmethod
    def validate_amount(value):
        if not isinstance(value, int):
            raise ValueError("Кількість цукерок повинна бути цілим числом")
        if value < 0:
            raise ValueError("Кількість цукерок не може бути від'ємною")
        return value

    def __init__(self, count):
        self.validate_amount(count)
        self._count = min(count, self.MAX_CAPACITY)

    @classmethod
    def full_stash(cls):
        return cls(cls.MAX_CAPACITY)

    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, value):
        self.validate_amount(value)
        self._count = min(value, self.MAX_CAPACITY)

    def __str__(self):
        return f"CandyStash({self._count}/{self.MAX_CAPACITY})"

    def __repr__(self):
        return self.__str__()

    def __add__(self, other):
        amount = other.count if isinstance(other, CandyStash) else other
        self.validate_amount(amount)
        new_count = min(self._count + amount, self.MAX_CAPACITY)
        return CandyStash(new_count)

    def __sub__(self, other):
        amount = other.count if isinstance(other, CandyStash) else other
        self.validate_amount(amount)
        new_count = max(self._count - amount, 0)
        return CandyStash(new_count)

    def __eq__(self, other):
        if isinstance(other, CandyStash):
            return self._count == other.count
        return self._count == other


if __name__ == "__main__":
    stash1 = CandyStash(12)
    stash2 = CandyStash(45)
    full = CandyStash.full_stash()

    print(stash1)          # CandyStash(12/50)
    print(repr(stash2))    # CandyStash(45/50)
    print(full)            # CandyStash(50/50)

    combined = stash1 + stash2
    print(combined)        # CandyStash(50/50), бо обрізано по MAX_CAPACITY

    eaten = stash1 - 20
    print(eaten)            # CandyStash(0/50), бо обрізано по нулю

    print(stash1 == CandyStash(12))  # True
    print(stash1 == 12)              # True
    print(stash1 == stash2)          # False

    try:
        CandyStash(-5)
    except ValueError as e:
        print("Помилка:", e)

    try:
        CandyStash("12")
    except ValueError as e:
        print("Помилка:", e)