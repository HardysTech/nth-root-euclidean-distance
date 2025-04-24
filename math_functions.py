import math

def nth_root(number, n):
    """
    Calculate the nth root of a number.
    
    Args:
        number: The number to find the root of
        n: The degree of the root (e.g., 2 for square root)
    
    Returns:
        The nth root of the number
    """
    return number ** (1/n)

def euclidean_distance(point1, point2):
    """
    Calculate the Euclidean distance between two points in n-dimensional space.
    
    Args:
        point1: First point as a list/tuple of coordinates
        point2: Second point as a list/tuple of coordinates
    
    Returns:
        The Euclidean distance between the points
    """
    if len(point1) != len(point2):
        raise ValueError("Points must have the same number of dimensions")
    
    squared_diff = sum((a - b) ** 2 for a, b in zip(point1, point2))
    return math.sqrt(squared_diff)

# Example usage
if __name__ == "__main__":
    # nth root examples
    print("8^(1/3) =", nth_root(8, 3))  # Cube root of 8
    print("16^(1/4) =", nth_root(16, 4))  # 4th root of 16
    
    # Euclidean distance examples
    point_a = (1, 2, 3)
    point_b = (4, 5, 6)
    print(f"Distance between {point_a} and {point_b}: {euclidean_distance(point_a, point_b)}")
    
    point_c = (0, 0)
    point_d = (3, 4)
    print(f"Distance between {point_c} and {point_d}: {euclidean_distance(point_c, point_d)}")