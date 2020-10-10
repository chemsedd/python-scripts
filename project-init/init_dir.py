"""
    This is a directories creating tool that i use for initializing
    my design projects folders, it creates:
    - Main project directory with the given name and path (optional),
    - Sub-dir for Assets, for svg, eps, png, jpg...etc, assets that i use,
    - Sub-dir for JPG, for exportings jpg pictures.
    - Sub-dir for PNG, for exporting png pictures (logos, icon, etc).
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
                        help='creates a Assets directory if specified.')
    parser.add_argument('-j', '--jpg', action='store_true',
                        help='creates a JPG directory if specified.')
    parser.add_argument('-p', '--png', action='store_true',
                        help='creates a PNG directory if specified.')

    return parser


def init_dir(path, name, assets, jpg, png):
    """Creates a directory with the given name, and appends sub-dirs
    to it, if specified (Assets, JPG, and PNG).

    Args:
        path (str): path for the main directory (project).
        name (str): the name of the directory (project).
        assets (boolean): if True, creates a Assets directory.
        jpg (boolean): if True, creates a JPG directory.
        png (boolean): if True, creates a PNG directory.
    """
    try:
        # Creating the project directory
        os.mkdir(os.path.join(path, name))
        print("- Project folder created ✔")
        # Creating directory for assets
        if assets:
            os.mkdir(os.path.join(path, name, 'Assets'))
            print("\t+ Assets created ✔")
        # Creating directory for jpg
        if jpg:
            os.mkdir(os.path.join(path, name, 'JPG'))
            print("\t+ JPG created ✔")
        # Creating directory for png
        if png:
            os.mkdir(os.path.join(path, name, 'PNG'))
            print("\t+ PNG created ✔")
        print('-' * 27)
    except FileExistsError:
        # In case of error
        print('# File already exists ❌')


if __name__ == "__main__":
    # create arguments
    parser = init_args()
    args = parser.parse_args()
    init_dir(args.PATH, args.name, args.assets, args.jpg, args.png)
