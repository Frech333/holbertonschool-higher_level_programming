#!/usr/bin/python3
def no_c(my_string):
    result = []
    for char in my_string:
        if char != 'c' and char != 'C':
            result.append(char)
    return "".join(result)
input_string = "This is a test string with some Cs and Cs."
output_string = no_c(input_string)
print(output_string)
