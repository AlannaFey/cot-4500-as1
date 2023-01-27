# Assignment 1
# COT4500 Spring 2023
# Alanna Hill, al538601

# This function takes a binary number, and returns the decimal
# representation of the number
def get_decimal_number(binary_num):
    while len(binary_num) < 64:
        binary_num += "0"

    s = int(binary_num[0])
    
    c = int(binary_num[1:12], 2)

    f = 0
    for i in range(12, 64):
        if binary_num[i] == "1":
            f += 1 / (2 ** (i - 11))

    return ((-1) ** s) * (2 ** (c - 1023)) * (1 + f)

# This function takes a number and a precision and returns the
# number truncated to that precision
def get_truncated_number(number, precision):
    mult = 1;
    while number < 10 ** (precision):
        number *= 10
        mult *= 10

    while number > 10 ** (precision):
        number /= 10
        mult /= 10

    number = int(number)
    number *= mult
    return number

# This function takes a number and a precision and returns the
# number rounded to that precision
def get_rounded_number(number, precision):
    mult = 1;
    while number < 10 ** (precision):
        number *= 10
        mult *= 10

    while number > 10 ** (precision):
        number /= 10
        mult /= 10

    number = int(number + 0.5)
    number *= mult
    return number

# This function takes an actual value and the aproximated value
# and returns the absolute error between the actual and aproximated
def get_absolute_error(actual, aprox):
    return abs(actual - aprox)

# This function takes an actual value and the aproximated value
# and returns the relative error between the actual and aproximated
def get_relative_error(actual, aprox):
    if actual == 0:
        return -1
    return abs(actual - aprox) / abs(actual)

# This function takes in an x value and an acceptable error and
# returns the number of steps to calculate the specified function
# to the given error
def calc_function(x, error):
    total = 0
    for k in range(1, 10000):
        curr = total + ((-1) ** k) * (x ** k) / (k ** 3)
        if abs(curr - total) < error:
            return k - 1
        total = curr
    return -1

# This is our given function
def f(x):
    return (x ** 3) + (4 * (x ** 2)) - 10

# This is the derivative of our given function
def df(x):
    return 3 * (x ** 2) + 8 * x

# This function takes in two starting values, and an acceptable error
# and returns the number of steps it takes to get within the error
# using the bisection method
def find_zero_bi(s1, s2, error):
    low, high = 0, 0
    if f(s1) < f(s2):
        low = s1
        high = s2
    else:
        low = s2
        high = s1
    max_iter = 100000
    i = 0
    mid = (low + high) / 2 
    while abs(high - low) > error and i < max_iter:
        i += 1
        mid = (low + high) / 2
        if (f(low) < 0 and f(mid) > 0) or (f(low) > 0 and f(mid) < 0):
            high = mid
        else:
            low = mid
    return i 

# This function takes in a starting x and an acceptable error
# and returns the number of steps it takes to get within the error
# using the newton-raphson method
def find_zero_newton(x0, error):
    max_iter = 10000
    i = 0
    while i < max_iter:
        i += 1
        x1 = x0 - (f(x0) / df(x0))
        if abs(f(x1) - f(x0)) < error:
            return i
        x0 = x1
    return -1

# main function for calling everything and output
def main():
    # getting all of the values
    binary_num = "010000000111111010111001"
    decimal_num = get_decimal_number(binary_num)
    truncated_num = get_truncated_number(decimal_num, 3)
    rounded_num = get_rounded_number(decimal_num, 3)
    abs_rounding_error = get_absolute_error(decimal_num, rounded_num)
    rel_rounding_error = get_relative_error(decimal_num, rounded_num)
    f1 = calc_function(1, 1e-4)
    function_zero_bi = find_zero_bi(-4, 7, 1e-4)
    function_zero_newton = find_zero_newton(-4, 1e-4)

    # printing with the specified format
    print(decimal_num, truncated_num, rounded_num, sep="\r\n\r\n", end="\r\n\r\n")
    print(abs_rounding_error, "{:.31f}".format(rel_rounding_error), sep="\r\n", end="\r\n\r\n")
    print(f1, function_zero_bi, function_zero_newton, sep="\r\n\r\n", end="\r\n\r\n")

# calling main if this file is run as the main function
if __name__ == "__main__":
    main()
