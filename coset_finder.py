import argparse


def coset_finder(z, subgroup):
    z = range(0, z)
    print(z, subgroup)
    for i in z:
        elements = set()
        for j in subgroup:
            elements.add("{}".format((i + j)%8))
        elements = list(elements)
        elements.sort()
        print(f"{i}"+" + H = "+'{'+', '.join(elements)+'}')



if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='This program finds the coset of Z/(m)')
    parser.add_argument('z', type=int,
                        help='value of n in Zn')
    parser.add_argument('subgroup', type=int, nargs='+',
                        help='input subgroup elements')
    args = parser.parse_args()
    coset_finder(args.z, args.subgroup)
