import numpy as np

from sdia_python.lab2.utils import get_random_number_generator


class BallWindow:
    """Simple class describing a ball"""

    def __init__(self, center, radius):
        """initialization method

        Args:
            center ([type]: np.array): vector giving the coordinates of the center of the ball
            radius ([type]: float): radius of the ball
        """
        self.center = np.array(center)
        self.radius = radius

    def __contains__(self, point):
        """returns True if and only if the given point is located inside the ball"""
        return np.linalg.norm(self.center - point) <= self.radius

    def dimension(self):
        """Returns the mathematical dimension of the box"""
        return len(self.center)

    def volume(self):
        """returns the volume of the ball if its dimension is < 3

        Returns:
            float
        """
        dim = self.dimension()
        if dim == 1:
            return 2 * self.radius
        if dim == 2:
            return np.pi * (self.radius ** 2)
        if dim == 3:
            return 4 / 3 * np.pi * (self.radius ** 3)
        return "unimplemented volume"
