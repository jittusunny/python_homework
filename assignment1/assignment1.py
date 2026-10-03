# Write your code here.
# Task1
def hello():
    return "Hello!"

# Task2
def greet(name):
   return f"Hello, {name}!" 
print(greet("Jittu"))

# Task 3
def calc(a, b, operation="multiply"):
    try:
        if operation == "multiply":
            return a * b
        elif operation == "add":
            return a + b
        elif operation == "subtract":
            return a - b
        elif operation == "divide":
            return a / b
        elif operation == "modulo":
            return a % b
        elif operation == "int_divide":
            return a // b
        elif operation == "power":
            return a ** b

    except ZeroDivisionError:
        return "You can't divide by 0!"
    except TypeError:
        return f"You can't {operation} those values!"
    except ValueError:
        return f"Unknown operation: {operation}"
print(calc(4, 2))

# Task4
def data_type_conversion(value, target_type):
    try:
        if target_type == "int":
            return int(value)
        elif target_type == "float":
            return float(value)
        elif target_type == "str":
            return str(value)
        else:
            return f"Unknown target type: {target_type}"
    except ValueError:
        return f"You can't convert {value} into a {target_type}."


value = "hi"
output_value = data_type_conversion(value, "float")
print(f"data_type_conversion({value}, 'float') = {output_value}")


# Task5
def grade(*args):
    try:
        average = sum(args)/len(args)
        if average >= 90:
            return "A"
        elif average >= 80:
            return "B"
        elif average >= 70:
            return "C"
        elif average >= 60:
            return "D"
        else:
            return "F"
    except (ValueError, TypeError):
        return "Invalid data was provided."

print(grade("a", 80, 70))


# Task6
def repeat(string, count):
    result = ""

    for i in range(count):
        result += string

    return result


print(repeat("Hello", 3))

# Task7
def student_scores(score, **kwargs):
    for key, value in kwargs.items():
        if score=="best":
            max_score = max(kwargs.values())
            if value == max_score:
                return key
        elif score=="mean":
            mean_score = sum(kwargs.values()) / len(kwargs)
            return mean_score
        else:
            return f"Unknown score type: {score}"   

print(student_scores("best", Alice=85, Bob=92, Charlie=78))
print(student_scores("mean", Alice=85, Bob=92, Charlie=78))
    
# Task8
def titleize(string):
    words = string.split()

    new_words = []

    for i, word in enumerate(words):
        if word.lower() in {"a", "an", "the", "and", "of", "is", "in", "on"} and 0 < i < len(words) - 1:
            new_words.append(word.lower())
        else:
            new_words.append(word.capitalize())

    return " ".join(new_words)


print(titleize("War and Peace"))

# task 9
def hangman(word, guesses):
    display = ["_" for _ in word]
    for guess in guesses:
        for i, letter in enumerate(word):
            if letter == guess:
                display[i] = letter
    return "".join(display)

print(hangman("hangman", ["a", "n", "g"]))

#task 10
def pig_latin(string):
    words = string.split()
    new_words = []

    vowels = "aeiou"

    for word in words:
        i = 0

        while i < len(word) and word[i] not in vowels:
            i += 1

        # Special case: qu
        if i < len(word) and word[i] == "u" and i > 0 and word[i - 1] == "q":
            i += 1

        if i == 0:
            new_word = word + "ay"
        else:
            new_word = word[i:] + word[:i] + "ay"

        new_words.append(new_word)

    return " ".join(new_words)

print(pig_latin("hello world"))
print(pig_latin("apple"))
print(pig_latin("string"))
print(pig_latin("quiet"))