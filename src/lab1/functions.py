def is_unique(x):
    """

    This function aims to tell the user if the list contains duplicates or not.

    Args:
        x ([list]): The list you want to test

    Returns:
        [bool]: True if every element in the list occurs only once, False if there is any duplicate in the list.
    """
    L = []
    verite = False
    for elem in x:
        verite = verite or (elem in L)
        L.append(elem)
    return not verite


def is_unique_bis(x):
    """Do exactly what is_unique() does.

    Args:
        x ([list]): The list you want to test

    Returns:
        [bool]: True if every element in the list occurs only once
    """
    return len(set(x)) == len(x)


def triangle_shape(height):
    """
    Display a traingle shape made of x with a certain height

    Args:
        height ([int]): The desired height for the shape

    Returns:
        [str]: A triangle shape made of x
    """
    triangle = ""
    nbEspaces = height - 1
    for indice in range(height):
        triangle += nbEspaces * " "
        triangle += "x" * (indice * 2 + 1)
        triangle += nbEspaces * " "
        if indice < (height - 1):
            triangle += "\n"
        nbEspaces += -1
    return triangle
