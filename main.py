# Function to calculate the dot product of two vectors
def dot_product(vector1, vector2):
    if len(vector1) != len(vector2):
        raise ValueError("Vectors must have the same dimension")

    # Calculate dot product
    dot_prod = sum([vector1[i] * vector2[i] for i in range(len(vector1))])
    return dot_prod


# Example vectors
vector1 = [1, 2, 3]
vector2 = [4, 5, 6]

# Calculate and print the dot product
try:
    result = dot_product(vector1, vector2)
    print(f"The dot product of {vector1} and {vector2} is: {result}")
except ValueError as e:
    print(e)
