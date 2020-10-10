"""
    This is a directories creating tool that i use for initializing 
    my design projects folders, it creates:
    - Main project directory with the given argument as dir name,
    - Sub-dir for Assets, where i put svg, png, jpg...etc, assets that i use,
    - Sub-dir for JPG, the final exporting format.
"""

import os


def init_dir(path):
    """Creates a directory with the given name, and appends 2 sub-dirs
    to it, Assets and JPG.

    Args:
        path (str): the name for the dir (project).
    """
    try:
        # Creating the project directory
        os.mkdir(path)
        # Creating directory for assets
        os.mkdir(os.path.join(path, 'Assets'))
        # Creating directory for jpg final pictures
        os.mkdir(os.path.join(path, 'JPG'))
    except FileExistsError:
        print('# File already exists!')


init_dir('event-poster')
