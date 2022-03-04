import sys, argparse
from wordlehelpersolver import wordlehelpersolve

def main():
    parser = argparse.ArgumentParser(description='Wordle Helper')

    parser.add_argument('-dopos', action='store_true', help='Match Positions', required=False)
    parser.add_argument('-docolors', action='store_true', help='Match Colors', required=False)
    parser.add_argument('-MinMatches', help='Min Matches on Positions', default=2, type=int, required=False)
    parser.add_argument('-MaxMatches', help='Max Matches on Positions', default=100, type=int, required=False)
    parser.add_argument('-matchpos', nargs='+', help='Matching Positions', type=int, default=[], required=False)
    parser.add_argument('-notmatchpos', nargs='+', help='Not Matching Positions', type=int, default=[], required=False)
    parser.add_argument('-grey', nargs='?', default='', help='Grey String', required=False)
    parser.add_argument('-green', nargs='?', default='', help='Green String', required=False)
    parser.add_argument('-yellow', nargs='?', default='', help='Yellow String', required=False)
    parser.add_argument('-greenpos', nargs='+', help='Green Positions', type=int, default=[], required=False)
    parser.add_argument('-yellowpos', nargs='+', help='Yellow Positions', type=int, default=[], required=False)

    args1 = parser.parse_args()
    args = vars(args1)
    result = wordlehelpersolve(args)
    print(result)

main()
