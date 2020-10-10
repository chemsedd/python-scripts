"""
    This is a directories creating tool that i use for initializing 
    my design projects folders, it creates:
    - Main project directory with the given argument as dir name,
    - Sub-dir for Assets, where i put svg, png, jpg...etc, assets that i use,
    - Sub-dir for JPG, the final exporting format.
"""

import os
import argparse


def init_args():
    """Defines command line arguments.

    Returns:
        ArgumentParser: argument parser that contains the specified arguments.
    """
    helper = 'Initializes a project directory for design work, by creating a main directory with the given name, and sub-dirs (Assets, JPG, etc).'
    parser = argparse.ArgumentParser(description=helper)

    parser.add_argument('name', type=str, help='The name of the project')
    parser.add_argument('-P', '--path', default='.', type=str, dest='PATH',
                        help='The path where to init the project (default: the current directory).')
    parser.add_argument('-a', '--assets', action='store_true',
                        help='Creates a Assets directory if specified.')
    parser.add_argument('-j', '--jpg', action='store_true',
                        help='Creates a JPG directory if specified.')
    parser.add_argument('-p', '--png', action='store_true',
                        help='Creates a PNG directory if specified.')

    return parser


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


if __name__ == "__main__":
    # create arguments
    parser = init_args()
    args = parser.parse_args()
    print(args)
    # init_dir('event-poster')
