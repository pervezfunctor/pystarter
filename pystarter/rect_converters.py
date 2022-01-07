from pydantic import validate_arguments

from pystarter.rect import Point, Rect, Rectangle, Size, SizedRect
from dataclasses import astuple

DELIMITER = ","


# @validate_arguments
def to_str(r: Rectangle) -> tuple[str, ...]:
    values = astuple(r)
    type = "Rect" if isinstance(r, Rect) else "SizedRect"
    return (type, *map(str, values))


@validate_arguments
def to_rect(line: str) -> Rectangle:
    type, *values = line.split(DELIMITER)

    assert len(values) == 4
    (x1, y1, x2, y2) = map(int, values)

    if type == "Rect":
        return Rect(Point(x1, y1), Point(x2, y2))

    assert type == "SizedRect"

    return SizedRect(Point(x1, y1), Size(x2, y2))


# geometry = Geometry(
#     shapes=[
#         SizedRect(size=Size(100, 200), top=Point(1, 2)),
#         Rect(bottom=Point(100, 200), top=Point(1, 2)),
#     ]
# )
