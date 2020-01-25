import math
from spike import simulation

PRECISION = 10


def test_sphericalprojectionradians():
    x, y = simulation.Physics.radianprojecttoxy(1.0, 0.0)
    assert round(x, PRECISION) == 1.0 and round(y, PRECISION) == 0.0

    x, y = simulation.Physics.radianprojecttoxy(1.0, math.pi/2.0)
    assert round(x, PRECISION) == 0.0 and round(y, PRECISION) == 1.0

    x, y = simulation.Physics.radianprojecttoxy(2.0, 0.0)
    assert round(x, PRECISION) == 2.0 and round(y, PRECISION) == 0.0


def test_sphericalprojectiondegrees():
    x, y = simulation.Physics.degreeprojecttoxy(1.0, 0.0)
    assert round(x, PRECISION) == 1.0 and round(y, PRECISION) == 0.0

    x, y = simulation.Physics.degreeprojecttoxy(1.0, 90.0)
    assert round(x, PRECISION) == 0.0 and round(y, PRECISION) == 1.0

    x, y = simulation.Physics.degreeprojecttoxy(2.0, 0.0)
    assert round(x, PRECISION) == 2.0 and round(y, PRECISION) == 0.0
