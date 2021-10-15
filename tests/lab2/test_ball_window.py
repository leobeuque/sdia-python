import numpy as np
import pytest

from sdia_python.lab2.ball_window import BallWindow, UnitBallWindow


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


@pytest.mark.parametrize(
    "points, expected",
    [
        (np.array([1, 1]), True),
        (np.array([[1, 1]]), True),
        (np.array([[4, 5], [1, 1], [1, 0]]), True),
        (np.array([4, 6]), False),
        (np.array([[1, 1], [10, 3], [1, 1]]), False),
    ],
)
def test_indicator_function_ball_2d(points, expected):
    ball_2d_rad5_center1_1 = BallWindow((1, 1), 5)

    assert ball_2d_rad5_center1_1.indicator_function(points) == expected


@pytest.mark.parametrize("n", [1, 5, 20, 100])
def test_rand_n_in_ball(n):
    ball_2d_rad5_center1_1 = BallWindow((1, 1), 5)
    points = ball_2d_rad5_center1_1.rand_n(n, rng=5)

    assert ball_2d_rad5_center1_1.indicator_function(points)


@pytest.mark.parametrize("n", [1, 5, 20, 100])
def test_rand_n_different_generated_points(n):
    # On teste si les points generes sont bien differents
    ball_2d_rad5_center1_1 = BallWindow((1, 1), 5)
    points = ball_2d_rad5_center1_1.rand_n(n)

    assert (
        points.shape[0]
        == len(set(points.flatten())) // ball_2d_rad5_center1_1.dimension()
    )


@pytest.mark.parametrize(
    "center, dimension, expected_radius, expected_center",
    [(np.array([1, 3]), 2, 1, np.array([1, 3])), (np.array([1]), 1, 1, np.array([1])),],
)
def test_unit_box(center, dimension, expected_radius, expected_center):
    unit_ball = UnitBallWindow(center, dimension)
    assert unit_ball.radius == expected_radius and np.all(
        unit_ball.center == expected_center
    )
