from typing import Protocol

class Drawable(Protocol):
    def draw(self) -> str:
        ...

def render(shape: Drawable) -> None:
    print(shape.draw())

class NoSmile:
    def draw(self) -> str:
        return ":("

class Smile:
    def draw(self) -> str:
        return ":)"

render(NoSmile())
render(Smile())