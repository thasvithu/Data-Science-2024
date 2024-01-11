import numpy as np

# Create a NumPy array using np.array()
arr = np.array([1, 2, 3, 4, 5])

# Checking the type of arr
print(type(arr))  # This will print <class 'numpy.ndarray'>

# Explicitly create an ndarray instance
ndarr = np.ndarray(shape=(5,), dtype=int, buffer=np.array([1, 2, 3, 4, 5]))

# Checking the type of ndarr
print(type(ndarr))  # This will also print <class 'numpy.ndarray'>






class MyClass:
    def __init__(self, value):
        self.value = value

def create_instance(val):
    return MyClass(val)

# Using the function to create an instance of MyClass
instance = create_instance(10)

# Accessing the instance attribute
print(instance.value)  # Output: 10
















