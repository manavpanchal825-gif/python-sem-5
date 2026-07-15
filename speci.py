def my_fun():
    """Demostrete,docstring and does nothing Really."""
    return None


print("Using __doc__:")
print(my_fun.__doc__)

print("Using Help")
help(my_fun)
