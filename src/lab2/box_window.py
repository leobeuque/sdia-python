from lab2.utils import get_random_number_generator
import numpy as np


class BoxWindow:
    """[Simple class describing a box]"""

    def __init__(self, bounds):
        """[initialization method]

        Args:
            args ([type]): [giving bounds as a list of segments defining bounds in each dimension]
        """
        self.bounds = np.array(bounds)

    def __str__(self):
        """BoxWindow: `[a_1, b_1] x [a_2, b_2] `

        Returns:
            [type]: [description]
        """
        bounds_list = []
        if len(self.bounds.shape) == 1:
            return "BoxWindow: " + str(self.bounds.tolist())

        A_list = self.bounds.tolist()
        to_print = ""
        for i in range(len(A_list)):
            if i != len(A_list) - 1:
                to_print = to_print + str(A_list[i]) + " x "
            else:
                to_print = to_print + str(A_list[i])

        return "BoxWindow: " + to_print

    def __len__(self):
        """[Returns the sum of the lengths of the different bounds]

        Returns:
            [type]: [description]
        """
        S = 0
        for segment in self.bounds:
            S += segment[1] - segment[0]
        return S

    def __contains__(self, point):

        for i in range(len(point)):
            if not (self.bounds[i][0] <= point[i] <= self.bounds[i][1]):
                return False
        return True

    def dimension(self):
        """[Returns the mathematical dimension of the box]"""
        return self.bounds.shape[0]

    def volume(self):
        produit = 1
        for segment in self.bounds:
            longueur = segment[1] - segment[0]
            produit *= longueur
        return produit

    def indicator_function(self, point):
        """[returns True if the box contains the point]

        Args:
            args ([type]): [the point must have the same dimension as the box]
        """
        verite = self.__contains__(point)
        return verite

    def rand(self, rng=None):
        """Generate a point uniformly at random inside the :py:class:`BoxWindow`.

        Args:
            rng ([type], optional): [description]. Defaults to None.
        """
        rng = get_random_number_generator(rng)
        number_list = []
        for bound in self.bounds:
            number_list.append(rng.uniform(bound[0], bound[1]))
        return np.array(number_list)

    def rand_n(self, n=1, rng=None):
        """Generate ``n`` points uniformly at random inside the :py:class:`BoxWindow`.

        Args:
            n (int, optional): [description]. Defaults to 1.
            rng ([type], optional): [description]. Defaults to None.
        """
        points_list = [self.rand(rng) for i in range(n)]
        return points_list


class UnitBoxWindow(BoxWindow):
    def __init__(self, center, dimension):
        """[summary]

        Args:
            dimension ([type]): [description]
            center ([type], optional): [description]. Defaults to None.
        """
        super(UnitBoxWindow, self).__init__(bounds)
