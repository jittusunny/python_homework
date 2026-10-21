from functools import wraps


# Task 2: Create a decorator that takes an output type as an argument.
def type_converter(type_of_output):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            x = func(*args, **kwargs)
            return type_of_output(x)

        return wrapper

    return decorator


# Task 2: Convert the returned integer 5 to a string.
@type_converter(str)
def return_int():
    return 5


# Task 2: Attempt to convert "not a number" to an integer.
@type_converter(int)
def return_string():
    return "not a number"


# Task 2: Verify the decorator using the exact provided mainline code.
y = return_int()
print(type(y).__name__) # This should print "str"
try:
   y = return_string()
   print("shouldn't get here!")
except ValueError:
   print("can't convert that string to an integer!") # This is what should happen