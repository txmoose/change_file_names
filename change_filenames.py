#!/usr/bin/env python3

import argparse
from os import rename
from sys import exit

parser = argparse.ArgumentParser()
parser.add_argument("-c", dest='up_or_low', default='lower', type=str)
parser.add_argument("files",  nargs='+')

args = parser.parse_args()

if args.up_or_low.lower() == "lower":
    for curr_file in args.files:
        rename(curr_file, curr_file.lower())

elif args.up_or_low.lower() == "upper":
    for curr_file in args.files:
        rename(curr_file, curr_file.upper())

else:
    exit("{} is not a valid argument".format(args.up_or_low))
