def main(data:str):
    """
    The data is from the file. Return the str(non-digital) characters as a list type.
    Args:
        data: str
    Returns:
        list: return answer
    """
    
    a = []
    idx = 0
    while idx < len(data):
        if not data[idx].isdigit():
            a.append(data[idx])
        idx += 1    
    return a
# Read data from file