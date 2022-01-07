from utils import dataclass


@dataclass(frozen=True)
class Point:
    x: int = 0
    y: int = 0


@dataclass(frozen=True)
class Size:
    width: int = 0
    height: int = 0


@dataclass(frozen=True)
class Rect:
    top: Point
    bottom: Point


@dataclass(frozen=True)
class SizedRect:
    top: Point
    size: Size


Rectangle = Rect | SizedRect


@dataclass(frozen=True)
class Geometry:
    shapes: list[Rectangle]
