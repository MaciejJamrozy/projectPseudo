from typing import TypeVar, Generic

T = TypeVar('T')

class Stack(Generic[T]):
    def __init__(self):
        self._items: list[T] = []
        self.depth: int = -1

    def push(self, item: T) -> None:
        self._items.append(item)
        self.depth += 1
        if self.depth > 19:
            raise Exception("Error: Stack overflow!")

    def pop(self) -> T:
        if not self.is_empty():
            self.depth -= 1
            return self._items.pop()
        raise Exception("pop from empty stack")

    def peek(self) -> T:
        if not self.is_empty():
            return self._items[-1]
        raise Exception("peek from empty stack")

    def is_empty(self) -> bool:
        return len(self._items) == 0

    def size(self) -> int:
        return len(self._items)