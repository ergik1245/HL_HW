from typing import Protocol

class Drawable(Protocol):
    def draw(self) -> str:
        ...

def render(shape: Drawable) -> None:
    print(shape.draw())

class not_smile:
    def draw(self) -> str:
        return ":("

class smile:
    def draw(self) -> str:
        return ":)"

render(not_smile())
render(smile())