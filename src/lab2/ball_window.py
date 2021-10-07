import numpy as np

from lab2.utils import get_random_number_generator


class BallWindow:
    """Simple class describing a ball"""

    def __init__(self, center, radius):
        """initialization method

        Args:
            center ([type]): [description]
            radius ([type]): [description]
        """
        self.center = np.array(center)
        self.radius = radius

    def __contains__(self, point):

        return np.linalg.norm(self.center - point) <= self.radius

    def dimension(self):
        """[Returns the mathematical dimension of the box]"""
        return len(self.center)

    def volume(self):
        dim = self.dimension()
        if dim == 1:
            return 2 * self.radius
        if dim == 2:
            return np.pi * (self.radius ** 2)
        if dim == 3:
            return 4 / 3 * np.pi * (self.radius ** 3)
        return "unimplemented volume"

    def indicator_function(self, point):
        """[returns True if the box contains the point]

        Args:
            args ([type]): [the point must have the same dimension as the box]
        """
        # ? how would you handle multiple points
        # todo readability consider using "point in self"
        verite = self.__contains__(point)
        return verite

    def rand(self, rng=None):
        """Generate a point uniformly at random inside the :py:class:`BoxWindow`.

        Args:
            rng ([type], optional): [description]. Defaults to None.
        """
        rng = get_random_number_generator(rng)
        number_list = []
        # * exploit numpy, rng.uniform(a, b, size=n)
        # * consider for a, b in self.bounds
        for bound in self.bounds:
            number_list.append(rng.uniform(bound[0], bound[1]))
        return np.array(number_list)

    def rand_n(self, n=1, rng=None):
        """Generate ``n`` points uniformly at random inside the :py:class:`BoxWindow`.

        Args:
            n (int, optional): [description]. Defaults to 1.
            rng ([type], optional): [description]. Defaults to None.
        """
        # * interesting way to decouple rand and rand_n
        # ? why passing a default n=1 argument if not calling self.rand when n=1
        points_list = [self.rand(rng) for i in range(n)]
        return points_list
        # ? why returning a list and not an np.array


ball_2d_rad5_center1_1 = BallWindow((1, 1), 1)
print(ball_2d_rad5_center1_1.volume())
