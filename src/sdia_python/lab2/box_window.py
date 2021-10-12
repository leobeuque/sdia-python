import numpy as np

# from sdia_python.lab2.utils import get_random_number_generator


# todo write and clean up the docstrings [ ]
# todo write and run tests
class BoxWindow:
    """[Simple class describing a box] The box is defined by its bounds"""

    def __init__(self, bounds):
        """[initialization method]

        Args:
            args ([numpy array]): giving bounds as a list of segments defining bounds in each dimension
        """
        self.bounds = np.array(bounds)

    def __str__(self):
        """BoxWindow: `[a_1, b_1] x [a_2, b_2] `

        Returns:
            [str]: A description of the given box with its corresponding bounds
        """
        bounds_list = []
        if len(self.bounds.shape) == 1:
            return "BoxWindow: " + f"{self.bounds.tolist()}"

        A_list = self.bounds.tolist()
        to_print = ""
        for i in range(len(A_list)):
            if i != len(A_list) - 1:
                to_print += f"{A_list[i]}" + " x "
            else:
                to_print += f"{A_list[i]}"

        return "BoxWindow: " + to_print

    def __len__(self):
        """[summary]
        Returns the sum of the lengths of the different bounds

        Returns:
            [int]: Returns the sum of the lengths of the different bounds
        """
        length = 0
        for segment in self.bounds:
            length += segment[1] - segment[0]
        return length

    def __contains__(self, point):
        """Test if the point passed as argument is in the box

        Args:
            point ([tuple]): The point we want to test

        Returns:
            [bool]: Return True if the point is in the box, False if it is outside the box
        """
        # * consider for (a, b), x in zip(self.bounds, point)
        # * or exploit numpy vectorization power
        for i in range(len(point)):
            if not (self.bounds[i][0] <= point[i] <= self.bounds[i][1]):
                return False
        return True

    def dimension(self):
        """Returns the mathematical dimension of the box

        Returns:
            [int]: Dimension of the box
        """
        return self.bounds.shape[0]

    def volume(self):
        """Returns the volume of the box with respect to the euclidian norm

        Returns:
            [float]: volume of the box
        """
        volume = 1  # ? naming: produit -> volume
        for segment in self.bounds:
            longueur = segment[1] - segment[0]
            volume *= longueur
        return volume

    def indicator_function(self, point):
        """Returns True if the box contains the point

        Args:
            args ([tuple]): the point must have the same dimension as the box

        Returns:
            [bool]: True or False regarding wether the point is in the box or not
        """
        # ? how would you handle multiple points
        # todo readability consider using "point in self"
        verite = self.__contains__(point)
        return verite

    def rand(self, rng=None):
        """Generate a point uniformly at random inside the :py:class:`BoxWindow`.

        Args:
            rng ([int], optional): Seed. Defaults to None.
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
            n (int, optional): Number of points to generate. Defaults to 1.
            rng ([int], optional): Seed. Defaults to None.
        """
        # * interesting way to decouple rand and rand_n
        # ? why passing a default n=1 argument if not calling self.rand when n=1
        return np.array(self.rand(rng) for i in range(n))
        # ? why returning a list and not an np.array


# todo class UnitBoxWindow and BallWindow not defined


class UnitBoxWindow(BoxWindow):
    def __init__(self, center, dimension):
        """[Description] Create a box

        Args:
            dimension ([int]): [description]
            center ([tuple], optional): The center of the box with respect to the euclidian norm. Defaults to None.
        """
        super(BoxWindow, self).__init__(bounds)
