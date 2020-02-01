import pytest
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
    x, y = simulation.Physics.radianprojectxy(np.array([1.0, 0.0]))
    assert round(x, PRECISION) == 1.0 and round(y, PRECISION) == 0.0

    x, y = simulation.Physics.radianprojectxy(np.array([1.0, np.pi/2.0]))
    assert round(x, PRECISION) == 0.0 and round(y, PRECISION) == 1.0

    x, y = simulation.Physics.radianprojectxy(np.array([2.0, 0.0]))
    assert round(x, PRECISION) == 2.0 and round(y, PRECISION) == 0.0


def test_degreeprojectxy():
    x, y = simulation.Physics.degreeprojectxy(np.array([1.0, 0.0]))
    assert round(x, PRECISION) == 1.0 and round(y, PRECISION) == 0.0

    x, y = simulation.Physics.degreeprojectxy(np.array([1.0, 90.0]))
    assert round(x, PRECISION) == 0.0 and round(y, PRECISION) == 1.0

    x, y = simulation.Physics.degreeprojectxy(np.array([2.0, 0.0]))
    assert round(x, PRECISION) == 2.0 and round(y, PRECISION) == 0.0


def test_accelerate():
    zeros1 = np.zeros((2, 3))
    accel1 = np.array([1, 0])
    zeros1 = simulation.Physics.accelerate(zeros1, accel1)
    assert np.allclose(zeros1, np.array([(.5, 0., 0.), (0., 0., 0.)]))

    zeros2 = np.zeros((2, 3))
    accel2 = np.array([1, 90])
    zeros2 = simulation.Physics.accelerate(zeros2, accel2)
    assert np.allclose(zeros2, np.array([(0., 0., 0.), (.5, 0., 0.)]))

    zeros4 = np.zeros((2, 3))
    accel4 = np.array([0, 0])
    zeros4 = simulation.Physics.accelerate(zeros4, accel4)
    assert np.allclose(zeros4, np.array([(0., 0., 0.), (0., 0., 0.)]))


def test_displacement():
    disp_matrix = np.array([(0.5, 0, 0), (0, 0, 0)])
    heading = 0
    disp_matrix, heading = simulation.Physics.displacement(
                           disp_matrix, heading, dt=1)
    expected_result = np.array([(0.5, 1, 0.5), (0., 0., 0.)])
    assert np.allclose(disp_matrix, expected_result) and heading == 0

    disp_matrix = np.array([(0.0, 0, 0), (0.5, 0, 0)])
    heading = 0
    disp_matrix, heading = simulation.Physics.displacement(
                           disp_matrix, heading, dt=1)
    expected_result = np.array([(0., 0., 0.), (0.5, 1, 0.5)])
    assert np.allclose(disp_matrix, expected_result) and heading == np.pi / 2

    disp_matrix = np.array([(0.5, 0, 0), (0, 0, 0)])
    heading = np.pi
    disp_matrix, heading = simulation.Physics.displacement(
                           disp_matrix, heading, dt=1)
    expected_result = np.array([(0.5, -1, -0.5), (0., 0., 0.)])
    assert np.allclose(disp_matrix, expected_result) and heading == np.pi

    disp_matrix = np.array([(0., 0, 0), (0.5, 0, 0)])
    heading = np.pi / 2
    disp_matrix, heading = simulation.Physics.displacement(
                           disp_matrix, heading, dt=1)
    expected_result = np.array([(0., -1, -0.5), (0.5, 0., 0.)])
    assert np.allclose(disp_matrix, expected_result) and heading == np.pi

    disp_matrix = np.array([(0., 0, 0), (0.0, 0, 0)])
    heading = np.pi / 2
    disp_matrix, heading = simulation.Physics.displacement(
                           disp_matrix, heading, dt=1)
    expected_result = np.array([(0., 0., 0.), (0., 0., 0.)])
    assert np.allclose(disp_matrix, expected_result) and heading == np.pi / 2


@pytest.fixture()
def moveable():
    yield simulation.Moveable()


def test_moveable(moveable):
    for loc in moveable.move(5):
        assert loc == (0, 0)

    count = 0
    moveable.set_acceleration(np.array([1, 0]))
    locations = [(0.5*i*i, 0.0) for i in range(1, 6)]
    for loc in moveable.move(5, dt=1):
        print(count)
        assert loc == locations[count]
        count += 1
