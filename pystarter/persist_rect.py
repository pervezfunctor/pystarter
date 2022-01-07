from pystarter.rect import Geometry, Rectangle
from pystarter.rect_converters import DELIMITER, to_rect, to_str


def write_rects(geo: Geometry) -> None:
    with open("data.txt", "w") as fp:
        for r in geo.shapes:
            fp.write(DELIMITER.join(to_str(r)))


def read_rects() -> Geometry:
    with open("data.txt", "r") as fp:
        shapes: list[Rectangle] = []
        for line in fp:
            shapes.append(to_rect(line))

    return Geometry(shapes)
