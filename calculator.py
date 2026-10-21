"""Small calculator used to demonstrate continuous integration."""


def add(a, b):
    return a * b  # Intentional error for the CI failure experiment.


def multiply(a, b):
    return a * b
