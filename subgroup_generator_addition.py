#!/usr/bin/env python3
import argparse
def subgroup_generator(m):
    improper_subgroup = set()

    for i in range(m):
        improper_subgroup.add(i)

    for i in range(m):
        a = set()
        for j in range(m):
            a.add((j*i)%m)
        if a == {0}:
            print('Trivial subgroup :')
        if a == improper_subgroup:
            print('Improper subgroup :')
        if a != improper_subgroup and a != {0}:
            print('Proper subgroup :')
        print("<{}> = {}".format(i, a), end="\n\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='This script calculates subgroups')
    parser.add_argument('m', type=int,
                        help='input m')
    args = parser.parse_args()
    subgroup_generator(args.m)
