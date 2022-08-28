import argparse

from .trkarekod import parse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('payload', type=str)

args = parser.parse_args()


def main():
    print(parse(args.payload).toJSON())
