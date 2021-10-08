import numpy as np
import pytest

from sdia_python.lab2.ball_window import BallWindow


def test_raise_type_error_when_something_is_called():
    with pytest.raises(TypeError):
        # call_something_that_raises_TypeError()
        raise TypeError()


@pytest.mark.parametrize(
    "point, expected",
    [
        (np.array([1, 1]), True),
        (np.array([4, 5]), True),
        (np.array([4, 6]), False),
        (np.array([10, 3]), False),
    ],
)
def test_contains_function_ball_2d(point, expected):
    ball_2d_rad5_center1_1 = BallWindow((1, 1), 5)
    is_in = point in ball_2d_rad5_center1_1
    assert is_in == expected


@pytest.mark.parametrize(
    "center, expected",
    [
        (np.array([0]), 2),
        (np.array([0, 0]), np.pi),
        (np.array([0, 0, 0, 0]), "unimplemented volume"),
    ],
)
def test_volume_boule_unite(center, expected):
    ball_2d_rad5_center1_1 = BallWindow(center, 1)
    assert ball_2d_rad5_center1_1.volume() == expected
