import math
from cadquery import func as cf

def clutch_brick(length, width, height, stud_d, stud_h, spacing):
    body = cf.box(length, width, height)
    stud = cf.cylinder(d=stud_d, h=stud_h)

    result = body

    for row in range(2):
        for col in range(4):
            x = (col - 1.5) * spacing
            y = (row - 0.5) * spacing

            positioned_stud = stud.moved(x=x, y=y, z=height)
            result = result + positioned_stud

    return result


brick = clutch_brick(31.6, 15.6, 9.6, 4.8, 1.7, 8.0)

expected = (
    31.6 * 15.6 * 9.6
    + 8 * math.pi * (4.8 / 2) ** 2 * 1.7
)

assert abs(brick.Volume() - expected) < 0.5

print("Valid brick:", brick.isValid())
print("Volume:", round(brick.Volume(), 2))

brick.exportStl("brick.stl")
