"""
Utility functions.
"""

from importlib import resources


def read_file(file_name: str, package: str = "st_undp") -> str:
    """
    Read a file resource as text.

    Parameters
    ----------
    file_name : str
        Name of the file, including the extension.
    package : str, optional
        Location of the file in the package. Defaults to the package root.

    Returns
    -------
    content : str
        File content as string
    """
    with resources.open_text(package, file_name) as file:
        content = file.read()
    return content
