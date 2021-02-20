import argparse
import pathlib


def main(args):
    pass


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('--load', required=True, type=pathlib.Path)
    parser.add_argument('--save', required=True, type=pathlib.Path)
    parser.add_argument('-o', action='store_true')
    parser.add_argument('-r', action='count', default=0)
    parser.add_argument('-t', action='store_true')
    parser.add_argument('-g', action='store_true')
    parser.add_argument('-s', action='store_true')
    parser.add_argument('-b', action='store_true')

    args = parser.parse_args()

    main(args)
