from types import TracebackType
from typing import ContextManager, Type


class CM(ContextManager[str]):
    def __enter__(self):
        print("enter")
        return "hello from context manager"

    def __exit__(
        self,
        __exc_type: Type[BaseException] | None,
        __exc_value: BaseException | None,
        __traceback: TracebackType | None,
    ):
        print("exit")


if __name__ == "__main__":
    with CM() as msg:
        print(msg)
