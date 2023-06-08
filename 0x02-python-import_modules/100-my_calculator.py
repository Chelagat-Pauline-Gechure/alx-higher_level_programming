#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    from calculator_1 import add, sub, mul, div
    if len(argv) != 4:
        print("Usage:", argv[0], "<a> <operator> <b>")
        exit(1)

    operation = argv[2]
    op_function = {'+': add, '-': sub, '*': mul, '/': div}
    if operation not in op_function:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)

    a = int(argv[1])
    b = int(argv[3])
    print('{:d} {:s} {:d} = {:d}'.format(a, operation, b, op_function[operation](a, b)))
