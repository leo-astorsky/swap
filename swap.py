#!/usr/bin/env python3

import argparse
import os
import pathlib
import shutil
import sys
import tempfile


def parse_args(args):
    parser = argparse.ArgumentParser()
    parser.add_argument('a', type=str, help='first file/dir to swap')
    parser.add_argument('b', type=str, help='2nd file/dir to swap')
    return parser.parse_args(args)


def main():
    args = parse_args(sys.argv[1:])
    tmp = os.path.join(tempfile.mkdtemp(), pathlib.PurePosixPath(args.a).name)
    shutil.move(args.a, tmp)
    shutil.move(args.b, args.a)
    shutil.move(tmp, args.b)


if __name__ == "__main__":
    main()
