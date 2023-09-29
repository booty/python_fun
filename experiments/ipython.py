import numpy as np

# create a numpy array
a = np.array([1, 2, 3, 4, 5])

# do some cool stuff with numpy
print(a)
print(a.shape)


# a list of ANSI terminal colors
colors = [
    "\033[95m",
    "\033[94m",
    "\033[92m",
    "\033[93m",
    "\033[91m",
    "\033[0m",
    "\033[1m",
    "\033[4m",
]

# print those colors and their corresponding name
for color in colors:
    print(color + "Hello World!" + "\033[0m")
