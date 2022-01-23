def main(data:str):
    """
    The data is from the file. Return the numbers as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    
    x = []
    idx = 0
    while idx < len(data):
        if data[idx].isdigit():
            x.append(data[idx])
        idx += 1
    
    return x
    
# Read data from file