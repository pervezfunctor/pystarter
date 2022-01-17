from dataclasses import dataclass
from typing import Any, Iterable, Optional


@dataclass
class Node:
    data: Any
    next: Optional["Node"] = None


class StackIterator:
    __current: Optional[Node]

    def __init__(self, current: Optional[Node]):
        self.__current = current

    def __next__(self):
        if self.__current is None:
            raise StopIteration

        current = self.__current
        self.__current = current.next
        return current.data


@dataclass
class Stack:
    head: Optional["Node"] = None

    def push(self, data: Any) -> None:
        self.head = Node(data, self.head)

    def pop(self) -> Optional[Any]:
        if self.head is None:
            return None
        data = self.head.data
        self.head = self.head.next
        return data

    def top(self) -> Optional[Any]:
        return self.head

    def is_empty(self) -> bool:
        return self.head is None

    def __iter__(self):
        return StackIterator(self.head)

    # def __iter__(self):
    #     while node := self.head:
    #         yield node.data
    #         node = node.next


def stack(iterable: Iterable[Any]) -> Stack:
    stack = Stack()
    for data in iterable:
        stack.push(data)
    return stack
