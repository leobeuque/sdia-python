def is_unique(x):
<<<<<<< HEAD
    """[summary]

    Args:
        x ([type]): [ouooui]

    Returns:
        [type]: [description]
    """
    L = []
    verite = False
    for elem in x:
        verite = verite or (elem in L)
        L.append(elem)
    return not verite


def is_unique_bis(x):
    return len(set(x)) == len(x)


def triangle_shape(height):
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
=======
    """Check that ``x`` has no duplicate elements.

    Args:
        x (list): elements to be compared.

    Returns:
        bool: True if ``x`` has duplicate elements, otherwise False
    """
    return len(set(x)) == len(x)


def triangle_shape(n, fillchar="x", spacechar=" "):
    """Return a string made of ``fillchar`` and ``spacechar``representing a triangle shape of height ``n``.

    For n=0, return ``""``.

    .. testcode::

        from lab1.functions import triangle_shape
        print(triangle_shape(6, fillchar="x", spacechar="_"))

    .. testoutput::

        _____x_____
        ____xxx____
        ___xxxxx___
        __xxxxxxx__
        _xxxxxxxxx_
        xxxxxxxxxxx

    Args:
        n (int): height of the triangle.
        fillchar (str, optional): Defaults to "x".
        spacechar (str, optional): Defaults to " ".

    Returns:
        str: string representation of the triangle.
    """
    width = 2 * n - 1
    return "\n".join(
        (fillchar * (2 * i + 1)).center(width, spacechar) for i in range(n)
    )
>>>>>>> b3c697b0cef6e29f9d6feff78d7cc83350a3b846
