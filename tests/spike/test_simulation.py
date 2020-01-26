import numpy as np
from spike import simulation

PRECISION = 10


def test_rotateaxis():
    x, y = simulation.Physics.rotateaxis(np.array([1.0, 0.0]), 0)
    assert round(x, PRECISION) == 1.0 and round(y, PRECISION) == 0.0

    x, y = simulation.Physics.rotateaxis(np.array([0.0, 1.0]), 0)
    assert round(x, PRECISION) == 0.0 and round(y, PRECISION) == 1.0

    x, y = simulation.Physics.rotateaxis(np.array([1.0, 0.0]), np.pi / 2)
    assert round(x, PRECISION) == 0.0 and round(y, PRECISION) == 1.0

    x, y = simulation.Physics.rotateaxis(np.array([0.0, 1.0]), np.pi)
    assert round(x, PRECISION) == 0.0 and round(y, PRECISION) == -1.0


def test_radianprojectxy():
    x, y = simulation.Physics.radianprojectxy(np.array([1.0, 0.0]), heading=0)
    assert round(x, PRECISION) == 1.0 and round(y, PRECISION) == 0.0

    x, y = simulation.Physics.radianprojectxy(np.array([1.0, np.pi/2.0]),
                                              heading=0)
    assert round(x, PRECISION) == 0.0 and round(y, PRECISION) == 1.0

    x, y = simulation.Physics.radianprojectxy(np.array([2.0, 0.0]), heading=0)
    assert round(x, PRECISION) == 2.0 and round(y, PRECISION) == 0.0

    x, y = simulation.Physics.radianprojectxy(np.array([1.0, 0.0]),
                                              heading=np.pi/2)
    assert round(x, PRECISION) == 0.0 and round(y, PRECISION) == 1.0

    x, y = simulation.Physics.radianprojectxy(np.array([1.0, np.pi/2.0]),
                                              heading=np.pi)
    assert round(x, PRECISION) == 0.0 and round(y, PRECISION) == -1.0


def test_degreeprojectxy():
    x, y = simulation.Physics.degreeprojectxy(np.array([1.0, 0.0]), heading=0)
    assert round(x, PRECISION) == 1.0 and round(y, PRECISION) == 0.0

    x, y = simulation.Physics.degreeprojectxy(np.array([1.0, 90.0]), heading=0)
    assert round(x, PRECISION) == 0.0 and round(y, PRECISION) == 1.0

    x, y = simulation.Physics.degreeprojectxy(np.array([2.0, 0.0]), heading=0)
    assert round(x, PRECISION) == 2.0 and round(y, PRECISION) == 0.0

    x, y = simulation.Physics.degreeprojectxy(np.array([1.0, 0.0]),
                                              heading=np.pi/2)
    assert round(x, PRECISION) == 0.0 and round(y, PRECISION) == 1.0

    x, y = simulation.Physics.degreeprojectxy(np.array([1.0, 90]),
                                              heading=np.pi)
    assert round(x, PRECISION) == 0.0 and round(y, PRECISION) == -1.0


def test_accelerate():
    pass


def test_displacement():
    pass
