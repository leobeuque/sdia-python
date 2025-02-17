import numpy as np
import pytest

from sdia_python.lab2.box_window import BoxWindow, UnitBoxWindow


def test_raise_type_error_when_something_is_called():
    with pytest.raises(TypeError):
        # call_something_that_raises_TypeError()
        raise TypeError()


@pytest.mark.parametrize(
    "bounds, expected",
    [
        (np.array([[2.5, 2.5]]), "BoxWindow: [2.5, 2.5]"),
        (np.array([[0, 5], [0, 5]]), "BoxWindow: [0, 5] x [0, 5]"),
        (
            np.array([[0, 5], [-1.45, 3.14], [-10, 10]]),
            "BoxWindow: [0.0, 5.0] x [-1.45, 3.14] x [-10.0, 10.0]",
        ),
    ],
)
def test_box_string_representation(bounds, expected):
    assert str(BoxWindow(bounds)) == expected


@pytest.fixture
def box_2d_05():
    return BoxWindow(np.array([[0, 5], [0, 5]]))


@pytest.mark.parametrize(
    "point, expected",
    [
        (np.array([0, 0]), True),
        (np.array([2.5, 2.5]), True),
        (np.array([-1, 5]), False),
        (np.array([10, 3]), False),
    ],
)
def test_indicator_function_box_2d(point, expected):
    box_2d_05 = BoxWindow(np.array([[0, 5], [0, 5]]))
    is_in = box_2d_05.indicator_function(point)
    # is_in = box_2d_05.__contains__(point)
    assert is_in == expected


# ================================
# ==== WRITE YOUR TESTS BELOW ====
# ================================


@pytest.mark.parametrize(
    "bounds, expected", [(np.array([[0, 1]]), 1), (np.array([[0, 5], [0, 5]]), 10),],
)
def test_length_box(bounds, expected):

    assert BoxWindow(bounds).__len__() == expected


@pytest.mark.parametrize(
    "bounds, expected",
    [
        (np.array([[1, 0]]), 1),
        (np.array([[0, 5], [0, 5]]), 2),
        (np.array([[0, 5], [-1, 3], [-10, 10]]), 3),
    ],
)
def test_dimension_box(bounds, expected):

    assert BoxWindow(bounds).dimension() == expected


@pytest.mark.parametrize(
    "bounds, expected",
    [
        (np.array([[2.5, 2.5]]), 0),
        (np.array([[0, 5], [0, 5]]), 25),
        (np.array([[0, 5], [-1, 3], [-10, 10]]), 400),
    ],
)
def test_volume_box(bounds, expected):

    assert BoxWindow(bounds).volume() == expected


@pytest.mark.parametrize(
    "bounds, expected",
    [
        (np.array([[2.5, 2.5]]), np.array([2.5])),
        (np.array([[1, 5], [1, 5]]), np.array([3.0, 3.0])),
        (np.array([[0, 2], [-1, 5], [-2, 6]]), np.array([1.0, 2.0, 2.0])),
    ],
)
def test_center_box(bounds, expected):

    assert np.all([BoxWindow(bounds).center_point() == expected])


@pytest.mark.parametrize(
    "center, dimension, expected",
    [
        (np.array([1, 3]), 2, np.array([[0.5, 1.5], [2.5, 3.5]])),
        (np.array([1]), 1, np.array([0.5, 1.5])),
        (np.array([-1.6, 2, 5.2]), 3, np.array([[-2.1, -1.1], [1.5, 2.5], [4.7, 5.7]])),
    ],
)
def test_unit_box(center, dimension, expected):

    assert np.all(UnitBoxWindow(center, dimension).bounds == expected)
