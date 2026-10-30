def merge_sorted_lists(list1: list, list2: list) -> list:
    """
    Merges two already sorted lists into a single sorted list 
    without using built-in sort/sorted functions.
    """
    merged_list = []
    i, j = 0, 0
    
    # Compare elements from both lists and append the smaller one
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1
            
    while i < len(list1):
        merged_list.append(list1[i])
        i += 1
        
    while j < len(list2):
        merged_list.append(list2[j])
        j += 1
        
    return merged_list

if __name__ == "__main__":
    # Example usage
    l1 = [1, 3, 5, 7]
    l2 = [2, 4, 6, 8]
    print(f"List 1: {l1}")
    print(f"List 2: {l2}")
    print(f"Merged List: {merge_sorted_lists(l1, l2)}")