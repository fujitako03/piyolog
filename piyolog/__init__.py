__version__ = '0.1.0'
from .src.piyolog import Piyolog

def read_log(
    data: str,
) -> Piyolog:
    """Piyologの出力から

    Args:
        data (str): Path of the dirctory in which the Piyolog files are stored.

    Returns:
        Piyolog: Preprocessed Piyolog data
    """
    piyo = Piyolog()
    return piyo