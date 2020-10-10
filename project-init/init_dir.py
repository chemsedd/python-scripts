"""
    This is a directories creating tool that i use for initializing
    my design projects folders, it creates:
    - Main project directory with the given name and path,
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

    parser.add_argument(
        'name', type=str, help='The name and path where to init the project (default path: the current directory with the given name).')
    parser.add_argument('-a', '--assets', action='store_true',
                        help='creates a Assets directory if specified.')
    parser.add_argument('-j', '--jpg', action='store_true',
                        help='creates a JPG directory if specified.')
    parser.add_argument('-p', '--png', action='store_true',
                        help='creates a PNG directory if specified.')

    return parser


def init_dir(path, assets, jpg, png):
    """Creates a directory with the given name, and appends sub-dirs
    to it, if specified (Assets, JPG, and PNG).

    Args:
        path (str): path and name for the main directory (project).
        assets (boolean): if True, creates a Assets directory.
        jpg (boolean): if True, creates a JPG directory.
        png (boolean): if True, creates a PNG directory.
    """
    try:
        # Creating the project directory
        os.mkdir(path)
        print("- Project folder created ✔")
        # Creating directory for assets
        if assets:
            os.mkdir(os.path.join(path, 'Assets'))
            print("   + Assets created ✔")
        # Creating directory for jpg
        if jpg:
            os.mkdir(os.path.join(path, 'JPG'))
            print("   + JPG created ✔")
        # Creating directory for png
        if png:
            os.mkdir(os.path.join(path, 'PNG'))
            print("   + PNG created ✔")
        print('-' * 27)
    except FileExistsError:
        # In case of error
        print('# File already exists ❌')


if __name__ == "__main__":
    # create arguments
    parser = init_args()
    args = parser.parse_args()
    init_dir(args.name, args.assets, args.jpg, args.png)
