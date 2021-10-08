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

    def indicator_function(self, points):

        # ? how would you handle multiple points
        # todo readability consider using "point in self"
        if len(points.shape) == 1:
            return points in self
        else:
            verite_array = np.apply_along_axis(lambda x: x in self, 1, points)
            return np.all(verite_array)

    # def rand(self, rng=None):
    #     """Generate a point uniformly at random inside the :py:class:`BoxWindow`.

    #     Args:
    #         rng ([int], optional): Seed. Defaults to None.
    #     """
    #     rng = get_random_number_generator(rng)
    #     number_list = []
    #     # * exploit numpy, rng.uniform(a, b, size=n)
    #     # * consider for a, b in self.bounds
    #     for bound in self.bounds:
    #         number_list.append(rng.uniform(bound[0], bound[1]))
    #     return np.array(number_list)

    # def rand_n(self, n=1, rng=None):
    #     """Generate ``n`` points uniformly at random inside the :py:class:`BoxWindow`.

    #     Args:
    #         n (int, optional): Number of points to generate. Defaults to 1.
    #         rng ([int], optional): Seed. Defaults to None.
    #     """
    #     # * interesting way to decouple rand and rand_n
    #     # ? why passing a default n=1 argument if not calling self.rand when n=1
    #     return np.array(self.rand(rng) for i in range(n))
    #     # ? why returning a list and not an np.array


# ball_2d_rad5_center1_1 = BallWindow((1, 1), 5)
# print((lambda x: x ** 2)(5))
# print(ball_2d_rad5_center1_1.indicator_function(np.array([[4, 5], [1, 0], [1, 0]])))
