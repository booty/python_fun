from emoji import is_emoji


def normalize(s):
    return ("".join([c for c in s if c.isalnum() or is_emoji(c)])).lower()


def ispalindrome_leet_edition(s):
    s = normalize(s)

    return s == s[::-1]


def ispalindrome_pythonic(s):
    s = normalize(s)
    return s == "".join(reversed(s))


def ispalindrome_pointers(s):
    s = normalize(s)
    i = 0
    j = len(s) - 1

    while i < j:
        if s[i] != s[j]:
            return False

        i += 1
        j -= 1

    return True


test_strings = [
    "Able was I, ere I saw Elba",
    "raceCAR",
    "Madam, I'm Adam",
    "🍕",
    "🍕racecar🍕🍕",
]

functions = [
    ispalindrome_leet_edition,
    ispalindrome_pythonic,
    ispalindrome_pointers,
]

for f in functions:
    for s in test_strings:
        print(f"{f.__name__:<{30}}{s:<{55}}{f(s)}")


def squares_generator():
    for n in range(10**8 + 1):
        yield n**2


def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


noice = fibonacci_generator()
for _ in range(10):
    print(next(noice))


def day_of_week_generator(current_day="Monday"):
    all_days = [
        "Monday",
        "Tuesday",
        "Wednesday",
        "Thursday",
        "Friday",
        "Saturday",
        "Sunday",
    ]
    # return current_day_index, or 0 if not found
    current_day_index = all_days.index(current_day) if current_day in all_days else 0

    while True:
        current_day_index += 1
        if current_day_index > 6:
            current_day_index = 0
        yield (all_days[current_day_index])


dow_gen = day_of_week_generator(current_day="Tuesday")
for _ in range(10):
    print(next(dow_gen))


squares = squares_generator()

# get the first 10 squares
for i in range(10):
    print(f"{i}: {next(squares)}")
