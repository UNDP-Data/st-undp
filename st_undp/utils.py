"""
Utility functions.
"""

from importlib import resources


def read_file(file_path: str) -> str:
    """
    Read a file resource as text.

    Parameters
    ----------
    file_path : str
        Relative path to the file from the package root.

    Returns
    -------
    content : str
        File content as string
    """
    with resources.files("st_undp").joinpath(file_path).open("r") as file:
        content = file.read()
    return content
