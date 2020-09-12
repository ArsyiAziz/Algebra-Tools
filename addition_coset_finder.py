import argparse

def addition_coset_finder(upper_bound, num_elements):
    for i in range(upper_bound):
        elements = []
        for j in range(-num_elements, num_elements):
            elements.append("{}".format(i + upper_bound*j ))
        print("{} + {}Z = {}".format(i,  upper_bound, '{... ,'+', '.join(elements)+', ...}'))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='This program finds the coset of Z/(m)')
    parser.add_argument('m', type=int,
                        help='value of m')
    parser.add_argument('num_elements', type=int,
                        help='The number elements to be displayed (num_elements*2 + 1)')
    args = parser.parse_args()
    addition_coset_finder(args.m, args.num_elements)
