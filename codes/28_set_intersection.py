def find_intersection(list1: list, list2: list) -> list:
    """
    Finds the intersection of two lists without using built-in set intersection methods.
    Returns a sorted list of unique common elements.
    """
    intersection = []
    for item in list1:
        # Check if the element is present in the second list and not already added to avoid duplicates
        if item in list2 and item not in intersection:
            intersection.append(item)
    return sorted(intersection)

if __name__ == "__main__":
    # Example usage
    l1 = [1, 2, 2, 3, 4]
    l2 = [2, 2, 4, 6]
    print(f"List 1: {l1}")
    print(f"List 2: {l2}")
    print(f"Intersection: {find_intersection(l1, l2)}")