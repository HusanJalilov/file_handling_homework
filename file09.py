def main(data:str):
    """
    The data is from the file. Find the smallest of the numeric characters.
    Args:
        data: str
    Returns:
        int: return answer
    """
    idx = 0
    min = 0
    while idx < len(data):
        if data[idx].isdigit():
            if int(data[idx]) < min:
                min = int(data[idx])
        idx += 1    
    return min
