import argparse
from typing import Tuple

from cleaner import Cleaner


def get_args() -> Tuple[str, bool]:
    parser = argparse.ArgumentParser('dir_path')

    parser.add_argument('-d', '--dir', action='store', dest='path', help='Start dir path', required=True)
    parser.add_argument('-r', '--remove', action='store_true', dest='remove_empty_dir', help='Remove empty dir')
    args = parser.parse_args()

    if args.path[-1] != '/':
        args.path += '/'

    return args.path, args.remove_empty_dir


if __name__ == '__main__':
    try:
        path, remove_flag = get_args()
        Cleaner(path, remove_flag).remove()

    except AttributeError as err:
        print(err)
