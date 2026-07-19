class Character:
    def __init__(self, name: str, max_hp: int):
        self.name = name
        self._max_hp = max_hp
        self._hp = max_hp

    @property
    def hp(self) -> int:
        """Не лезь, оно тебя сожрет."""
        return self._hp

    def take_damage(self, amount: int) -> None:
        if amount < 0:
            raise ValueError("Хмм, интересно, отрицательный урон? Не, так не пойдет")
        self._hp = max(0, self._hp - amount)

    def heal(self, amount: int) -> None:
        if amount < 0:
            raise ValueError("Хмм, отравился что ли? отрицательное лечение? Не, так не пойдет")
        self._hp = min(self._max_hp, self._hp + amount)

    def is_alive(self) -> bool:
        return self._hp > 0
    


c = Character("Млекопитающее", max_hp=100)
print(c.hp)

c.take_damage(30)
print(c.hp)

c.heal(1000)
print(c.hp)

c.take_damage(1000)
print(c.hp)
print(c.is_alive())