"""
Utility functions.
"""

from importlib import resources


def read_file(file_name: str) -> str:
    """
    Read a file resource as text.

    Parameters
    ----------
    file_name : str
        Name of the file, including the extension.

    Returns
    -------
    content : str
        File content as string
    """
    with resources.open_text("st_undp", file_name) as file:
        content = file.read()
    return content
