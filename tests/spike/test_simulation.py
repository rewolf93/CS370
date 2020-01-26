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
    zeros1 = np.zeros((2, 3))
    accel1 = np.array([1, 0])
    simulation.Physics.accelerate(zeros1, accel1, heading=0)
    assert np.allclose(zeros1, np.array([(.5, 0., 0.), (0., 0., 0.)]))

    zeros2 = np.zeros((2, 3))
    accel2 = np.array([1, 90])
    simulation.Physics.accelerate(zeros2, accel2, heading=0)
    assert np.allclose(zeros2, np.array([(0., 0., 0.), (.5, 0., 0.)]))

    zeros3 = np.zeros((2, 3))
    accel3 = np.array([1, 0])
    simulation.Physics.accelerate(zeros3, accel3, heading=np.pi / 2)
    assert np.allclose(zeros3, np.array([(0., 0., 0.), (.5, 0., 0.)]))

    zeros4 = np.zeros((2, 3))
    accel4 = np.array([1, 90])
    simulation.Physics.accelerate(zeros4, accel4, heading=np.pi / 2)
    assert np.allclose(zeros4, np.array([(-.5, 0., 0.), (0., 0., 0.)]))


def test_displacement():
    pass
