"""
Utility functions.
"""

from importlib import resources
from typing import Literal


def read_file(file_path: str, mode: Literal["r", "rb"] = "r") -> str | bytes:
    """
    Read a file resource as text.

    Parameters
    ----------
    file_path : str
        Relative path to the file from the package root.
    mode : Literal["r", "rb"]
        Mode can be 'r' or 'rb' to open as text or binary respectively.

    Returns
    -------
    content : str | bytes
        File content as string or bytes.
    """
    with resources.files("st_undp").joinpath(file_path).open(mode) as file:
        content = file.read()
    return content
