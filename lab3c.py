#!/usr/bin/env python3

def operate(a, b, op):
    if op == "add":
        return str(a + b)
    elif op == "subtract":
        return str(a - b)
    elif op == "multiply":
        return str(a * b)
    else:
        return 'Error: function operator can be "add", "subtract", or "multiply"'

if __name__ == "__main__":
    print(operate(10, 5, 'add'))
    print(operate(10, 5, 'subtract'))
    print(operate(10, 5, 'multiply'))
    print(operate(10, 5, 'divide'))  # shows error
