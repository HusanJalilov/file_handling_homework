def main(data:str):
    """
    The data is from the file. Find the each row length and return the largest row.
    Args:
        data: str
    Returns:
        int: return answer
    """
    list1 = data.split()
    idx = 0
    max = 0
    while idx < len(list1):
        if max < len(list1[idx]):
            max = len(list1[idx])
        idx += 1
        
    return max
        

# Read data from file