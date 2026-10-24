
import logging
from functools import wraps

# Set up logging to write to decorator.log
logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)

file_handler = logging.FileHandler("./decorator.log", "a")
logger.addHandler(file_handler)


# Task 1: Create the decorator
def logger_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Call the original function and save its return value
        value = func(*args, **kwargs)

        # Use "none" if no arguments were passed
        positional = args if args else "none"
        keyword = kwargs if kwargs else "none"

        # Write the function details to the log file
        logger.info(
            f"function: {func.__name__}\n"
            f"positional parameters: {positional}\n"
            f"keyword parameters: {keyword}\n"
            f"return: {value}\n"
        )

        # Give the original return value back
        return value

    return wrapper


# Task 1: Function that takes no parameters and returns nothing
@logger_decorator
def say_hello():
    print("Hello, World!")


# Task 1: Function that accepts any number of positional arguments
@logger_decorator
def check_arguments(*args):
    return True


# Task 1: Function that accepts any number of keyword arguments
@logger_decorator
def get_decorator(**kwargs):
    return logger_decorator


# Mainline code: Call all three functions
if __name__ == "__main__":
    say_hello()

    result = check_arguments("apple", 10, True)
    print(result)

    decorator = get_decorator(name="John", age=12)
    print(decorator)
